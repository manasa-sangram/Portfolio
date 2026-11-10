// app.js - the only JavaScript on the site. Five small jobs.
//
// Quick vocabulary, in plain words:
//   const / let   give a name to a value (const never changes, let can change)
//   function      a named block of code you can run whenever you want
//   document.querySelector("...")  finds ONE element in the page by its CSS selector
//   document.querySelectorAll("...") finds ALL matching elements
//   element.classList.add("x")  adds the CSS class "x" (style.css then styles it)


// ---------------------------------------------------------------------------
// JOB 1: REVEAL ON SCROLL
// "IntersectionObserver" is a browser feature that tells us when an element
// scrolls into view. Then we add the class "show", and style.css fades it in.
// ---------------------------------------------------------------------------
const revealObserver = new IntersectionObserver(function (entries) {
  for (const entry of entries) {
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
      revealObserver.unobserve(entry.target);   // only reveal once
    }
  }
}, { threshold: 0.15 });                        // 15% of the element must be visible

for (const element of document.querySelectorAll(".reveal")) {
  revealObserver.observe(element);
}


// ---------------------------------------------------------------------------
// JOB 2: THE ROTATING WORDS ("I love ...")
// The words come from content.py. They are written in the HTML as data-words,
// separated by "|".
// ---------------------------------------------------------------------------
const rotator = document.getElementById("rotator");
const words = rotator.dataset.words.split("|");
let wordNumber = 0;

setInterval(function () {
  rotator.style.opacity = 0;                          // fade out
  setTimeout(function () {
    wordNumber = (wordNumber + 1) % words.length;     // next word, back to the first at the end
    rotator.textContent = words[wordNumber];
    rotator.style.opacity = 1;                        // fade in
  }, 300);
}, 2500);                                             // every 2.5 seconds


// ---------------------------------------------------------------------------
// JOB 3: TABS (Work / Projects and Travel / New things)
// A button and a panel with the same data-group belong together.
// Clicking a button shows the panel whose data-panel matches its data-tab.
// ---------------------------------------------------------------------------
for (const button of document.querySelectorAll(".tab")) {
  button.addEventListener("click", function () {
    const group = button.dataset.group;

    // 1. highlight only the clicked button
    for (const other of document.querySelectorAll('.tab[data-group="' + group + '"]')) {
      other.classList.remove("on");
    }
    button.classList.add("on");

    // 2. show only the matching panel
    for (const panel of document.querySelectorAll('.panel[data-group="' + group + '"]')) {
      panel.hidden = (panel.dataset.panel !== button.dataset.tab);
    }
  });
}


// ---------------------------------------------------------------------------
// JOB 4: MARK THE SECTION YOU ARE READING IN THE MENU
// On every scroll we find which section is on screen and give its menu link
// the class "active" (style.css draws the little peach line next to it).
// ---------------------------------------------------------------------------
const menuLinks = document.querySelectorAll(".quest-link");

// the ids of all sections, in menu order: ["highlights", "work", ...]
const sectionIds = [];
for (const link of menuLinks) {
  sectionIds.push(link.dataset.quest);
}

// which section is the visitor reading?
// = the LAST section whose top edge is above 35% of the screen height.
function findCurrentSection() {
  let current = sectionIds[0];
  for (const id of sectionIds) {
    const top = document.getElementById(id).getBoundingClientRect().top;
    if (top < window.innerHeight * 0.35) {
      current = id;
    }
  }
  // at the very bottom of the page, count the last section as current
  if (window.innerHeight + window.scrollY >= document.body.scrollHeight - 4) {
    current = sectionIds[sectionIds.length - 1];
  }
  return current;
}

let lastCurrent = "";

function onScroll() {
  const current = findCurrentSection();
  for (const link of menuLinks) {
    link.classList.toggle("active", link.dataset.quest === current);   // add the class if true, remove if false
  }

  // on a phone the menu swipes sideways: slide it so the active link sits in the middle.
  // (We move only the menu itself. Moving the whole page here would cancel the smooth scroll.)
  if (current !== lastCurrent) {
    lastCurrent = current;
    const menu = document.getElementById("quest-nav");
    const link = document.querySelector('[data-quest="' + current + '"]');
    menu.scrollLeft = link.offsetLeft - menu.clientWidth / 2 + link.clientWidth / 2;
  }
}

window.addEventListener("scroll", onScroll);   // run every time the visitor scrolls
onScroll();                                    // and once when the page loads


// ---------------------------------------------------------------------------
// JOB 5: SMALL EXTRAS: the clock, the accent button, the mouse dot, the dance styles
// ---------------------------------------------------------------------------

// The time in Rostock, shown in the menu (updates every 30 seconds)
const clock = document.getElementById("clock");
function showTime() {
  if (!clock) { return; }
  clock.textContent = new Date().toLocaleTimeString("en-GB", { timeZone: "Europe/Berlin", hour: "2-digit", minute: "2-digit" });
}
showTime();
setInterval(showTime, 30000);

// The accent button: each click picks the next colour and sets it as --accent for the whole page
const ACCENTS = [
  { name: "peach", color: "#ff9e7d" },
  { name: "blue", color: "#5b8def" },
  { name: "lavender", color: "#c9b6ff" },
  { name: "mint", color: "#9be8c8" },
];
let accentNumber = 0;
const modeButton = document.getElementById("mode");
if (modeButton) {
  modeButton.addEventListener("click", function () {
    accentNumber = (accentNumber + 1) % ACCENTS.length;
    document.documentElement.style.setProperty("--accent", ACCENTS[accentNumber].color);
    modeButton.textContent = "accent: " + ACCENTS[accentNumber].name;
  });
}

// The dot that follows the mouse. It grows over links, buttons and lines you can click.
const cursorDot = document.getElementById("cursor");
if (cursorDot) {
  window.addEventListener("mousemove", function (event) {
    cursorDot.style.opacity = 1;
    cursorDot.style.transform = "translate(" + event.clientX + "px, " + event.clientY + "px)";
    cursorDot.classList.toggle("big", Boolean(event.target.closest("a, button, summary")));
  });
}

// The "now grooving" line in the menu: the dance styles take turns every 3 seconds
const groove = document.getElementById("groove");
if (groove) {
  const styles = groove.dataset.words.split("|");
  let styleNumber = 0;
  setInterval(function () {
    groove.style.opacity = 0;                              // fade out
    setTimeout(function () {
      styleNumber = (styleNumber + 1) % styles.length;     // next style, back to the first at the end
      groove.textContent = styles[styleNumber];
      groove.style.opacity = 1;                            // fade in
    }, 300);
  }, 3000);
}
