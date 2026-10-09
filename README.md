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

## Home page (`home-page-elementor.html`)

The complete home page, organized around visitors finding their own path:

1. **Hero** over the stage photo (tablets and computers; phones get the plain blue background).
2. **"Who are you? Start here."** buttons for Parents, Teachers & Schools, Driver Educators, Law Enforcement & Courts, Community & Youth Leaders, Teens and Workplace Drug Education (coming soon).
3. **Track record**: verified numbers that count up when they scroll into view, named testimonials, teacher survey quotes and a scrolling strip of organization logos in color, each linking to that organization's site (with a pause button; it sits still for visitors who turn off motion).
4. **Drug Educator Certification** (now enrolling).
5. **Drug information** cards and a "Need help now?" box with 911, Poison Control, 988 and SAMHSA.
6. **What we're building next**: the interactive ONE Platform diagram (every card and the center disc link to `/one-platform/`), then cards for The Real Cost, the First-Time Offender Program and the national campaign.
7. **Support** buttons.

### Install
Paste `home-page-elementor-compact.html` into the home page's Elementor HTML widget, replacing all of its code, and click **Update**.

**If saving gives a 403 error**, the host's security firewall is blocking the save. Use the three files in `home-page-split/` instead; they keep the `<style>` and `<script>` code out of the page:
1. `1-styles.css` → **Appearance → Customize → Additional CSS** (all rules are scoped to this page's sections, so they don't affect other pages).
2. `2-page.html` → the home page's Elementor HTML widget.
3. `3-scripts.html` → a code snippet plugin such as WPCode, as an HTML snippet in the site footer, shown on the front page only.

### Before publishing
- The **Driver Educators** button links to `/drug-educator-certification/` until a Driver Educators page exists; then change its link (marked with a comment).

### SEO
- Yoast handles the page title, meta description, canonical URL, social sharing tags and the Organization / WebSite / WebPage structured data. This file doesn't repeat any of them.
- The page has exactly one `<h1>`, in the hero. In Elementor, keep **Hide Title** turned on for the home page so the theme doesn't add a second one.
- The file adds structured data for the Drug Educator Certification course, linked to Yoast's organization. Update its `price` and `validThrough` when the Q4 special ends.
- The counting numbers are also in the page as plain text for search engines and screen readers.

### Customize
- **Hero photo**: change the image address in the `.dea-hero` CSS rule and in the `preload` link at the top of the hero.
- **Logos**: each logo is one `<li>` line in the "Organizations we've trained" list, with its website link. Add, remove or reorder lines there; the scrolling copy is made automatically.
- **Testimonials**: words in [brackets] were changed from the original quote and "…" marks shortened text, so readers can tell.

### Rebuilding
Edit `home-page-elementor.html` (the readable version), then run `python3 build.py`. It regenerates `home-page-elementor-compact.html` and `home-page-split/`, using the minified ONE diagram in `src/one-diagram-home.min.html` (it goes between the `ONE DIAGRAM START` / `END` comments).
