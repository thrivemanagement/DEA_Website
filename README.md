# DEA Website components

## ONE Platform (`one-platform-wordpress.html`)

The ONE Platform disc in the center with 8 areas around it, 4 per side, joined by dotted connectors. Hovering or clicking an area opens its description card below the diagram. On phones the areas stack into a list and the description opens directly under the tapped area.

### Add it to WordPress
1. Edit the page and add a **Custom HTML** block (`+` → search "Custom HTML").
2. Paste the entire contents of `one-platform-wordpress.html`.
3. Click **Preview** to see it working (the block editor itself only shows the code).

Notes:
- Your WordPress user needs the Administrator role (or the `unfiltered_html` permission), or WordPress strips the `<script>`.
- WordPress.com sites need a Business plan or higher to run scripts. Self-hosted WordPress has no such limit.
- Use one per page.

### Customize
Everything editable is in the `EDIT HERE` section of the `<script>` at the bottom:
- `AREAS`: for each of the 8 areas, the pill label (`name`), second line / card title (`sub`), description (`text`), colors, and an optional `link` button, e.g. `link: { text: "Learn more", href: "/young-people" }`.
- `CENTER_IMAGE`: optional URL of an image to use in the center instead of the built-in ONE Platform logo and globe.

## Full ONE Platform page for Elementor (`one-platform-page-elementor.html`)

The complete https://drugeducators.org/one-platform/ page with the interactive ecosystem diagram in the "Bringing It All Together" section, replacing the static ecosystem image and the 8 cards below it. Everything else on the page is unchanged.

To install: edit the page with Elementor, open the existing HTML widget, select all of its code, and replace it with the full contents of this file. Then click **Update**.

## Home page with ONE Platform teaser (`home-page-elementor.html`)

The complete home page with a new "ONE Platform" section between "Programs, Training & Initiatives" and "The Real Cost". It uses the same interactive diagram, tuned as a teaser: every description card and the center disc link to `/one-platform/`, and the section ends with an "Explore ONE Platform" button.

To install: edit the home page with Elementor, open the HTML widget, replace all of its code with the full contents of this file, and click **Update**.
