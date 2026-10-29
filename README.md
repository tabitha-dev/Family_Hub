# Family Hub

**[Open Family Hub](https://tabitha-dev.github.io/Family_Hub/)** · [Source code](https://github.com/tabitha-dev/Family_Hub)

Family Hub is a free, independently developed family organizer for meals, groceries, chores and calendar events. Built with **HTML, CSS and vanilla JavaScript**, designed for desktop and mobile, and hosted as a static GitHub Pages site. This is **not** the Lumina Family OS project.

## Features

- **Today at a glance:** pending chores, today's family events and groceries still to purchase.
- **Meal planner:** plan breakfast, lunch and dinner for each day of the week.
- **Grocery checklist:** group items by category, check off purchases, add and remove items.
- **Chore assignments:** track family responsibilities and progress.
- **Family calendar:** add events, browse months and view events by day.
- **Appearance:** light and dark mode with keyboard-accessible controls.
- **Local backups:** export and import household data as JSON.

The responsive redesign includes a polished violet-and-cream visual identity, a dedicated mobile navigation bar with an accessible More menu, touch-friendly controls, semantic metadata, WebApplication structured data, a sitemap, and visible explanatory FAQs.

## Data storage and privacy

All household data is stored in the **current browser's localStorage**, under its existing keys: `chores`, `groceryList`, `calendarEvents`, `mealPlan`, `familyMembers`, and `settings`. Those keys and data shapes are kept compatible with earlier versions.

**Family Hub does not automatically synchronize across devices**. Export from Settings to make a backup or transfer information to a different browser. Clearing site data or using private browsing can remove saved information.

Family items are not sent to a Family Hub backend, but external fonts and the Tailwind CDN can make network requests. Don't treat an ordinary shared browser as suitable storage for sensitive information.

## Accessibility, SEO and AEO

- Keyboard focus indication, a skip link, labeled dialogs, Escape and Tab handling, large touch targets and reduced-motion styles.
- A semantic page structure and human-readable information about what the app does and how its privacy/storage model works.
- HTML meta descriptions, canonical URL, Open Graph tags, favicon, sitemap and schema.org WebApplication JSON-LD.
- User-entered text is escaped before being inserted into HTML templates to reduce injection risk.
- Mobile/desktop browser tests should be checked per release. A full manual screen-reader / WCAG 2.2 AA audit is still required before claiming compliance.

Search indexing and inclusion in AI-generated answers are not guaranteed by metadata.

## Local development

Serve this directory over HTTP, e.g.:

```bash
python -m http.server 8000
```

Then open http://localhost:8000. No build command, backend, account or paid service is required.

## Visual provenance

The redesign uses bespoke CSS-based family-home artwork as a dependable local illustration. Additional OpenArt concepts may be adopted after review and optimization; unfinished art is not used as a runtime dependency.

## License

See [LICENSE](LICENSE).
