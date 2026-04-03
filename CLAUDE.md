# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

XIU is a bilingual (Korean/English) personal developer portfolio — a static single-page application built with vanilla HTML, CSS, and JavaScript. No build tools, no frameworks, no package manager.

## Deployment

- Served by Nginx (config in `nginx.conf`, document root `/usr/share/nginx/html`)
- SPA routing: all 404s redirect to `index.html`
- Static assets cached 30 days with `Cache-Control: public, immutable`

## Architecture

All application code lives in `index.html` (~1,744 lines) as a monolithic file with embedded `<style>` and `<script>` sections:

1. **CSS** — Uses CSS custom properties for theming (dark theme, gold `#d4a016` accent, teal `#2dd4a8` highlight). Responsive breakpoint at 768px.
2. **i18n system** — A `translations` object maps keys to `ko`/`en` strings. Elements use `data-i18n` (text) and `data-i18n-html` (HTML content) attributes. Language preference persists via `localStorage`.
3. **Scroll-reveal animations** — Intersection Observer triggers `.reveal` class animations with stagger delays (`.reveal-delay-1` through `.reveal-delay-5`).
4. **Project filtering** — `data-filter` buttons filter project cards by `data-category` (ai, qr, church, gaming, web).
5. **Counter animations** — Elements with `data-count` attribute animate from 0 to target value on scroll.

Other files: `privacy.html` (privacy policy with matching design), `nginx.conf`, `favicon.ico`, `assets/profile.png`.

## Key Conventions

- No build step — edit files directly and reload
- Data attributes drive behavior: `data-i18n`, `data-i18n-html`, `data-count`, `data-filter`, `data-category`, `data-lang`
- When adding translatable text, add entries to both `ko` and `en` in the `translations` object and set the appropriate `data-i18n` attribute on the element
- CSS variables are defined in `:root` — use them instead of hardcoding colors/fonts
