# tv-reader — put a manual on a TV

> Serving from this machine. For the hosted version that needs no local server —
> GitHub Pages plus a state endpoint, which is what a Raspberry Pi or a chat on a
> phone would use — see [`docs/`](../../docs/README.md).

Serves a manual as a two-page spread a TV can display and a remote can drive.

Two sources, picked automatically:

- **Page images** when the manual has `data/pages.json` (every page pre-rendered to
  PNG). The reader just shows them — nothing to rasterise, no PDF to download, and
  flipping is as fast as the images arrive. By default they load from the jsDelivr
  URLs baked into `pages.json`; `--images local` serves the committed copies from
  this machine instead, which needs no internet on the display.
- **The PDF** otherwise, rendered client-side with pdf.js and fetched by HTTP range,
  so only the spread being read crosses the network rather than the whole 20–50 MB.

Prefer images where they exist: it is the difference between decoding a PNG and
rasterising a 300 DPI scan on a weak TV.

```bash
python scripts/tv-reader/serve.py --manual renault-dauphine --page 39
python scripts/tv-reader/serve.py --manual renault-dauphine --page 39 --cast "Living Room TV"
```

`--manual` takes a manifest slug (`renault-dauphine`) or a manual directory name
(`dauphine`); an unknown value lists every manual on the shelf. The PDF comes from
`manuals/<path>/` when one is committed there, otherwise it is downloaded once from
the manifest's `source.location` into `.cache/` (gitignored).

## Getting it onto the screen

Two ways, with different tradeoffs:

- **Cast it** (`--cast`, needs [catt](https://github.com/skorokithakis/catt)). Launches
  the DashCast receiver, so nothing has to be installed on the TV. Cast once and leave
  it: `--goto` and `--reload` drive the page from then on. Known limits: the
  Chromecast receiver swallows some remote keys — left/right page turns arrive, but OK
  and the down arrow may not, which disables zoom and vertical panning. And a *live*
  receiver page ignores both `catt stop` and any new `cast_site`: catt reports success
  and nothing happens. Casting only replaces a page that has already died (for example
  because this machine changed address). Pressing Home on the TV remote is the only
  reset from outside, so use `--reload` to refresh a page that is working, and keep the
  remote handy for one that is not.
- **Open the URL in a browser on the TV** (e.g. TV Bro on Google TV). A real browser
  passes the whole D-pad through, so every control below works.

## Jumping to a page

The intended workflow: ask about a procedure or spec in chat, then put the page it
cites on the TV. With a reader already running, `--goto` moves it:

```bash
python scripts/tv-reader/serve.py --goto 232
```

The page polls `/state`, so the jump lands in about a second with no reload and no
re-cast — which matters, because reloading means re-initialising pdf.js on the TV.
`--goto` needs only `--port` (default 8789) to find the running reader; it ignores
`--manual` and exits immediately.

`reader.html` is read per request, so after editing it you only need a reload — no
server restart:

```bash
python scripts/tv-reader/serve.py --reload
```

The page polls for this and reloads itself, so an edit lands without re-casting.

## When the TV casts and then drops to the Home screen

The TV has to reach *this machine* by IP, and `--cast` sends whatever address the
server picked at startup. If the laptop has since moved networks — or sits behind a
second router that NATs it away from the TV — catt still connects and reports success
(that direction works), but the TV cannot fetch the page and the receiver quits.

Check both ends are on the same subnet before blaming the receiver:

```bash
ipconfig getifaddr en0       # must be the TV's subnet
catt scan                    # lists the TV with its address
```

Then restart the server so it picks up the current address, and cast again.

## Controls

| Key | Action |
| --- | --- |
| ◀ ▶ | move the selection between the two pages; at the edges, turn to the next/previous spread |
| OK | zoom the selected page to 2× at the scan's native resolution |
| arrows (zoomed) | pan |
| BACK | leave zoom |

## Options

| Flag | Default | Notes |
| --- | --- | --- |
| `--page N` | 1 | page shown on the left of the spread |
| `--port N` | 8789 | |
| `--cast DEVICE` | — | device name from `catt scan` |
| `--images cdn\|local\|off` | cdn | where page images come from, if the manual has them: the CDN, this machine, or `off` to rasterise the PDF instead |
| `--oversample F` | 2 | render scale above display size. Pages render at `display × dpr × F`, capped at the scan's native height, then downscale in CSS — that is what keeps text sharp on a 1080p panel. Lower it to ~1.5 if a weak TV flips sluggishly. PDF mode only; page images are already at native resolution. |

## Not built yet

**One server, several manuals.** Today a reader serves a single manual and `--goto`
takes only a page number, so switching manuals means restarting and re-casting. The
shape it wants: the server loads every manual named in a project config, `/goto`
takes a slug alongside the page, and the reader swaps PDFs without a reload. That
would make the chat workflow work across the whole shelf rather than one manual at a
time — worth doing when the reader moves to an always-on host (a Raspberry Pi in the
garage, which also gets a real browser and so the full D-pad).
