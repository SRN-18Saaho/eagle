CampusConnect (VESIT) - project files

Campus_Connect_Dashboard.html   The finished app. One file, images embedded. Double-click to open (needs internet for Tailwind, React and fonts).
source/app.src.html             Same app, readable: the two images are placeholders (__LOGO_IMG__, __CAMPUS_IMG__).
source/app.jsx                  Only the React code (the script part of the page).
assets/vesit-logo.jpg           Logo used in the top bar, sign-in page and tab icon.
assets/campus.jpg               Photo used on the sign-in page.
tests/                          Browser smoke test (Playwright) and the helper that builds its offline test page.
tools/apply_fixes.py            The script that applied the bug fixes to the earlier version.

To edit: change source/app.src.html, then replace __LOGO_IMG__ and __CAMPUS_IMG__ with data:image/jpeg;base64,... of the two images in assets/.
