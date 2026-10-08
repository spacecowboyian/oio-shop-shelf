# Hosted shelf reader

A static reader for the manuals on this shelf, built to live on GitHub Pages and
show a page on a TV. It needs no server: page images come straight from jsDelivr,
so the only moving parts are this folder and the display itself.

- `index.html` — the reader. `?manual=<slug>&page=<n>`
- `goto.html` — opened from a link; moves the page on a display that is already showing
- `config.js` — which display to talk to (edit this)
- `manuals.json` — generated; which manuals have page images
- `worker/worker.js` — the state endpoint, deployable to Cloudflare

## Turning it on

1. **Pages**: repo Settings → Pages → deploy from `main`, folder `/docs`.
   `https://<user>.github.io/<repo>/?manual=alpine-a110-reparaturhandbuch&page=13`
   works immediately — a page per URL, no state endpoint needed.
2. **Remote page changes** (optional, but it is the point): deploy
   `worker/worker.js` — instructions are in its header — then set `stateBase` and a
   `room` in `config.js` and commit. The reader polls that room; `goto.html` writes
   to it.

## Which manuals appear

Only those with pre-rendered page images (`data/pages.json`). A hosted page has no
server to rasterise a PDF, and Release PDFs cannot be fetched cross-origin — no CORS
headers, and signed URLs that expire within the hour. Regenerate the list after
rendering a new manual:

```bash
python scripts/tv-reader/build_site.py
```

## Getting it on a screen

**A Raspberry Pi is the right answer.** Chromium in kiosk mode on the hosted URL,
started once at boot. Nothing publishes to it — the page polls outward, so there is
no inbound port, no tunnel, no dynamic DNS, and no script running per request. Every
remote key reaches the page, so zoom and panning work.

```
chromium-browser --kiosk --noerrdialogs --disable-infobars \
  'https://<user>.github.io/<repo>/?manual=alpine-a110-reparaturhandbuch'
```

**A Chromecast works but stays awkward.** Cast senders must be on the same LAN, by
protocol — so something in the house has to push the URL every time the page dies,
and that is exactly the machine a Pi would replace. The receiver also swallows OK and
the down arrow (no zoom, no vertical panning) and ignores casts while a page is live.
See `scripts/tv-reader/README.md`, which covers the local server and casting.

## The room id is a credential

Anyone with the room string can change what the display shows. Use something
unguessable rather than `garage`, and keep it out of anything public.
