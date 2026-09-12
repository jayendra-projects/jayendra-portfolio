# Portfolio: Jayendra Weerakoon

Source code for [portfoliojayendra.netlify.app](https://portfoliojayendra.netlify.app), a personal portfolio site for a graduate Business/Data Analyst based in Melbourne.

Plain HTML, CSS and vanilla JS. No build step required.

## Structure

```
index.html    Page content (hero, about, experience, skills, work, contact)
styles.css    All styling
script.js     Mobile nav toggle + project filter buttons
```

## Editing

- **Project cards** live in the `#work` section of `index.html`. Each is an `<article class="card" data-cat="ba|bi|ml">`. Add a new one by copying an existing `<article>` block.
- **Colors and type** are defined as CSS custom properties at the top of `styles.css` (`:root`).

## Deploy

This repo is connected to Netlify. Pushing to `main` redeploys the live site automatically.
