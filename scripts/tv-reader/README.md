# tv-reader — put a manual on a TV

Serves a manual's PDF as a two-page spread a TV can display and a remote can drive.
Pages are rendered client-side with pdf.js and fetched by HTTP range, so only the
spread you are looking at crosses the network — not the whole 20–50 MB PDF.

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
  the DashCast receiver, so nothing has to be installed on the TV. The script stops any
  running session first — a receiver still holding the previous URL ignores a new cast
  without reporting an error. Known limit: the
  Chromecast receiver swallows some remote keys — left/right page turns arrive, but OK
  and the down arrow may not, which disables zoom and vertical panning.
- **Open the URL in a browser on the TV** (e.g. TV Bro on Google TV). A real browser
  passes the whole D-pad through, so every control below works.

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
| `--oversample F` | 2 | render scale above display size. Pages render at `display × dpr × F`, capped at the scan's native height, then downscale in CSS — that is what keeps text sharp on a 1080p panel. Lower it to ~1.5 if a weak TV flips sluggishly. |
