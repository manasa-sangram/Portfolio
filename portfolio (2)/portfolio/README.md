# Manasa's portfolio

One black page with giant lowercase titles, little computer-style windows and nine numbered sections, with a slim menu on the left.
Built with plain Python (FastAPI), HTML, CSS and a little JavaScript. No build step.

## Run it on your laptop

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000. `--reload` refreshes the site whenever you save a file.

## What to edit

| I want to change...                      | Edit this                                        |
|------------------------------------------|--------------------------------------------------|
| Any text, link, book, lesson, milestone  | `content.py` (search for `TODO`)                 |
| Photos                                   | put JPGs in `static/photos/` (names are in `content.py`); `me.jpg` becomes your sidebar portrait |
| Resume button                            | put `Manasa_Resume.pdf` in `static/` (the button appears by itself) |
| German level                             | `GERMAN` in `content.py` (change a level's `state`) |
| Skills list (the skills.json window)     | `HIGHLIGHTS` -> `skills` in `content.py`         |
| My Corner windows (file names, entries)  | `CORNER` in `content.py`                         |
| One section's layout                     | `templates/sections/<name>.html`                 |
| The sidebar                              | `templates/_sidebar.html`                        |
| Colours                                  | the `:root` block at the top of `static/style.css` (the visitor can also press the "accent" button in the menu) |
| Comment section behaviour                | `main.py` and `templates/_comments.html`         |

## Project map

```
content.py              all the words and links
main.py                 the Python backend (the page + the comment section)
requirements.txt        the Python packages to install
templates/
  index.html            the page: head, sidebar, the 9 sections, footer
  _sidebar.html         the menu sidebar
  _photos.html          draws a list of polaroid photos
  _comments.html        draws the list of comments
  sections/*.html       one file per section
static/
  style.css             the look and every animation
  app.js                scroll reveal, rotating words, tabs, menu highlight, clock, accent button, mouse dot
  photos/               your pictures
```

## The guestbook ("Write to me")

Visitors write a name and a comment; it is saved in a small SQLite file
(`comments.db`) and shown to everyone under the form. It is created by itself
on first start and is ignored by git, so it never lands on GitHub.

**Deleting a comment (you only):** set a secret word as the environment variable
`ADMIN_KEY` on your host, then open your site as `https://yoursite.com/?key=YOUR_SECRET`.
A small "delete" link appears next to each comment. Without the key nobody sees it.

**Email me about new comments (optional):** set `SMTP_HOST`, `SMTP_PORT`,
`SMTP_USER`, `SMTP_PASSWORD`, `CONTACT_TO` on your host. For Gmail use an
"app password". Every comment is also printed to the server log (Render: Logs tab).

**Important on Render's free plan:** the disk is wiped on every redeploy and
restart, so the comments would disappear. Two fixes:
1. a paid Render "persistent disk", then set `DB_FILE=/var/data/comments.db`; or
2. later switch to a free hosted database (I can help with that).

**Moderation and privacy:** the comments are public, so look at them now and
then. Since you live in Germany, a public page that stores visitors' names
should have a short privacy notice and an Impressum (legal notice). This is a
heads-up, not legal advice: check the current rules or ask an expert.

## Deploy on Render

1. Push the project to a GitHub repository (`.gitignore` keeps passwords out).
2. On render.com: New -> Web Service -> pick the repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Under Environment add `ADMIN_KEY` (and the email variables if you want them).

Update routine afterwards: `git add .`, `git commit -m "what changed"`, `git push`.
Render redeploys by itself.

## Privacy

Your phone number and email are intentionally not on the site (bots scrape
them). Comment authors give only a name (no email).
