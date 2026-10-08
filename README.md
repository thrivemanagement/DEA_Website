# DEA Website components

## Topic Orbit (`topic-orbit-wordpress.html`)

One center image with 8 topics arranged in a circle (4 per side). Hovering a topic previews its description in a panel below; clicking keeps it open.

### Add it to WordPress
1. Edit the page and add a **Custom HTML** block (`+` → search "Custom HTML").
2. Paste the entire contents of `topic-orbit-wordpress.html`.
3. Click **Preview** to see it working (the block editor itself only shows the code).

Notes:
- Your WordPress user needs the Administrator role (or the `unfiltered_html` permission), or WordPress strips the `<script>`.
- WordPress.com sites need a Business plan or higher to run scripts. Self-hosted WordPress has no such limit.
- Use one Topic Orbit per page.

### Customize
Everything editable is in the `EDIT HERE` section of the `<script>` at the bottom:
- `CENTER_IMAGE`: URL of the center photo (Media Library → image → "Copy URL to clipboard").
- `TOPICS`: title, description, bullet points, button link, and color (`hue`, 0–360) for each of the 8 topics.

The heading text is in the `<header>` near the top. For a dark version, change `class="topic-orbit"` to `class="topic-orbit to-dark"`.
