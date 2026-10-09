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

1. **Hero** with a photo, which the welcome video replaces once it's ready.
2. **"Who are you? Start here."** buttons for Parents, Teachers & Schools, Driver Educators, Law Enforcement & Courts, Community & Youth Leaders and Teens, plus a note for Employers.
3. **Track record**: verified numbers, named testimonials, teacher survey quotes and a scrolling strip of organization logos (with a pause button; it sits still for visitors who turn off motion).
4. **Drug Educator Certification** (now enrolling).
5. **Drug information** cards and a "Need help now?" box with 911, Poison Control, 988 and SAMHSA.
6. **What we're building next**: ONE Platform, The Real Cost, the First-Time Offender Program and the national campaign, each linking to its own page. The full ONE Platform diagram lives on `/one-platform/`.
7. **Support** buttons.

To install: edit the home page with Elementor, open the HTML widget, replace all of its code with the full contents of this file, and click **Update**.

### Before publishing
- The **Driver Educators** button links to `/driver-educators/`. Create that page first, or change the link.

### SEO
- Yoast handles the page title, meta description, canonical URL, social sharing tags and the Organization / WebSite / WebPage structured data. This file doesn't repeat any of them.
- The page has exactly one `<h1>`, in the hero. In Elementor, keep **Hide Title** turned on for the home page so the theme doesn't add a second one.
- The file adds structured data for the Drug Educator Certification course, linked to Yoast's organization. Update its `price` and `validThrough` when the Q4 special ends.

### Customize
- **Hero photo**: change the `srcset` address in the hero's `<picture>`.
- **Welcome video**: find `data-youtube-id=""` in the hero and put the video's YouTube ID between the quotes (for `https://www.youtube.com/watch?v=AbC123xYz` the ID is `AbC123xYz`). Until then the photo shows instead. The video only loads when someone presses play.
- **Logos**: each logo is one `<li>` line in the "Organizations we've trained" list. Add, remove or reorder lines there; the scrolling copy is made automatically.
- **Testimonials**: words in [brackets] were changed from the original quote and "…" marks shortened text, so readers can tell.

`home-page-elementor-compact.html` is the same page with the CSS minified, for when a hosting firewall rejects the larger save. Edit the readable file; regenerate the compact one from it.
