"""
main.py - the Python part of your website (the "backend").

What happens when someone opens your site:
  1. Their browser asks for "/".
  2. FastAPI runs the function `home` below.
  3. `home` reads the comments from the database and fills templates/index.html
     with them and with the text from content.py.
  4. The finished page goes back to the browser. style.css and app.js make it
     look good and move.

There is one page. Besides showing it, this file does three more things:
  - saves a new comment      (POST /comments)
  - deletes a comment        (GET  /delete/<id>?key=...   only for you)
  - emails you about new comments (optional)

Run it on your laptop:   uvicorn main:app --reload
"""

import os
import smtplib
import sqlite3
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import content  # your content.py file: all the text of the site

# The folder this file lives in, so the app finds its files from any start folder.
BASE_DIR = Path(__file__).parent

app = FastAPI()

# Everything in the "static" folder (style.css, app.js, photos, resume) is
# available in the browser under the address /static/...
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Jinja2 fills the HTML templates with data.
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def static_exists(path):
    """Is there a file at static/<path>?
    The templates use this to show a photo only when the file exists, and to
    show the Resume button only when your PDF is there."""
    return (BASE_DIR / "static" / path).exists()


# Make the function above usable inside the HTML templates.
templates.env.globals["static_exists"] = static_exists


# ---------------------------------------------------------------------------
# The database (where the comments are stored)
# ---------------------------------------------------------------------------
# SQLite is a database that lives in ONE file (comments.db). Python can use it
# without installing anything. You can set DB_FILE on your host to store the file
# somewhere else (for example on a persistent disk).
DB_FILE = os.getenv("DB_FILE", str(BASE_DIR / "comments.db"))

# A secret word that only you know. With it you can delete comments (see /delete below).
# Set it on your host as ADMIN_KEY. If it is empty, deleting is switched off.
ADMIN_KEY = os.getenv("ADMIN_KEY", "")


def open_db():
    db = sqlite3.connect(DB_FILE)
    db.row_factory = sqlite3.Row   # rows can be read like dictionaries: row["name"]
    return db


def create_table():
    """Create the comments table the first time the app starts (does nothing if it exists)."""
    db = open_db()
    db.execute(
        "CREATE TABLE IF NOT EXISTS comments ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, message TEXT, created TEXT)"
    )
    db.commit()
    db.close()


create_table()


def get_comments():
    """The newest 100 comments, newest first."""
    db = open_db()
    rows = db.execute("SELECT id, name, message, created FROM comments ORDER BY id DESC LIMIT 100").fetchall()
    db.close()
    return [dict(row) for row in rows]


# ---------------------------------------------------------------------------
# The page
# ---------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Only you see the "delete" links: open your site as  yoursite.com/?key=YOUR_ADMIN_KEY
    key = request.query_params.get("key", "")
    admin_key = key if (ADMIN_KEY and key == ADMIN_KEY) else ""

    # In the templates, `content` is your content.py file, so you can write
    # things like {{ content.HIGHLIGHTS.headline }}
    return templates.TemplateResponse(
        request,
        "index.html",
        {"content": content, "comments": get_comments(), "admin_key": admin_key},
    )


# ---------------------------------------------------------------------------
# The comment section
# ---------------------------------------------------------------------------
def comments_html(request, note="", note_kind="ok"):
    """Draw just the comment list (templates/_comments.html) with an optional message on top.
    The browser puts this piece into the page without reloading it (HTMX does that)."""
    return templates.TemplateResponse(
        request,
        "_comments.html",
        {"comments": get_comments(), "note": note, "note_kind": note_kind},
    )


def send_email(name, message):
    """Email you about a new comment, but only if the settings below are set.

    The settings are "environment variables" (set on your host, e.g. Render),
    so your password is never written in the code or pushed to GitHub:
        SMTP_HOST  SMTP_PORT  SMTP_USER  SMTP_PASSWORD  CONTACT_TO
    """
    host = os.getenv("SMTP_HOST")
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    to = os.getenv("CONTACT_TO")
    if not (host and user and password and to):
        return  # not set up yet: that is fine while testing on your laptop

    mail = EmailMessage()
    mail["Subject"] = "New comment on your website from " + name
    mail["From"] = user
    mail["To"] = to
    mail.set_content(name + " wrote:\n\n" + message)

    try:
        with smtplib.SMTP(host, int(os.getenv("SMTP_PORT", "587"))) as server:
            server.starttls()
            server.login(user, password)
            server.send_message(mail)
    except Exception as error:
        print("Could not send email:", error)


@app.post("/comments", response_class=HTMLResponse)
def add_comment(
    request: Request,
    name: str = Form(...),
    message: str = Form(...),
    website: str = Form(""),  # the "honeypot", explained below
):
    # Honeypot: the form has an extra field that people cannot see. Spam bots
    # fill in every field, so if it is not empty we quietly ignore the comment.
    if website:
        return comments_html(request)

    # Clean the text and cut it to a sensible length.
    name = name.strip()[:40]
    message = message.strip()[:500]
    if not name or len(message) < 2:
        return comments_html(request, "please write your name and a note.", "error")

    # Save the comment. The ? marks are placeholders: the database puts the values
    # in safely. NEVER build this text by joining strings yourself, because that
    # lets attackers sneak in their own SQL commands ("SQL injection").
    db = open_db()
    db.execute(
        "INSERT INTO comments (name, message, created) VALUES (?, ?, ?)",
        (name, message, datetime.now().strftime("%d %b %Y")),
    )
    db.commit()
    db.close()

    # print() writes to the server log (on Render: the "Logs" tab).
    print("NEW COMMENT from", name, ":", message)
    send_email(name, message)
    return comments_html(request, "thank you! your entry is in the guestbook.", "ok")


@app.get("/delete/{comment_id}")
def delete_comment(comment_id: int, key: str = ""):
    """Delete one comment. Works only with your secret ADMIN_KEY.
    (This is enough for a small personal site. A bigger site would use a real login.)"""
    if ADMIN_KEY and key == ADMIN_KEY:
        db = open_db()
        db.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
        db.commit()
        db.close()
        return RedirectResponse("/?key=" + key + "#contact", status_code=303)
    return RedirectResponse("/#contact", status_code=303)
