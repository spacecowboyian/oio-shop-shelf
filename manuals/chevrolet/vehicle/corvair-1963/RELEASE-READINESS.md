# 1963 Corvair release readiness

Status: **published as a PDF Release with six documented review flags**. The composite
covers 1963 passenger cars, including the Monza convertible and Spyder option;
Corvair 95 commercial vehicles are outside its scope. Open flags remain
qualified in the wiki rather than being treated as release blockers.

## Verified package

- All 18 chapters are reconstructed. The 742 factory-source pages have a
  complete physical-page source map, 742 rendered page images, and a 742-entry
  page index. The release PDF adds four clickable index pages, for 746 pages
  total: 18 chapter links and 209 alphabetical entries. All 228 index links
  target valid source pages.
- All 37 staged original factory PDFs match their committed SHA-256 hashes.
  The ignored local `prepared.pdf` is the 742-page OCR working copy; its
  SHA-256 is `ef790e2cfa619f643846ea5489071b39be8947ddaf7b9730b62b33e84de1a3fe`.
  Text extraction succeeds on 741 source pages. Page 141, a Corvair 95
  commercial-only lubrication page outside this wiki's scope, remains image-only.
  The [746-page indexed release PDF](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-corvair-1963/corvair-1963.pdf)'s SHA-256 is
  `85cf7842ed395f25bb56733f5e72af8e4e8f4f2acb65a3b7f0bfb285d78db067`.
  The downloaded GitHub Release asset matches that hash and page count.
- Manifest validation, composite-map validation, repository-wide internal-link
  checks, and 41 composite tests pass.
- The [needs-review list](wiki/10-needs-review.md) carries six open flags.
  Flagged material is kept out of authoritative service settings where its
  applicability or value is unverified.

## Source gaps retained at publication

The first three items were prioritized as essential research questions. They
remain open with explicit limits in the wiki:

1. **Convertible hoist contacts.** The [1963 owner's guide, p. 36](https://corvanatics.org/files/business-office/OwnMan-OwnPP/63OM-E3.pdf#page=20)
   establishes the vehicle-jack placement, but the inherited 1961 hoist
   diagram predates the convertible. Find a Chevrolet instruction that
   explicitly covers hoist contact on a 1962–64 convertible. The wiki keeps
   the inherited hoist diagram qualified until then.
2. **Corrected Powerglide fig. 6E-6.** The recovered 1962–63 Section 6E scan
   ends on printed p. 6E-3 after referring to fig. 6E-6. Obtain a complete
   bound supplement or an independently scanned continuation showing the
   original figure. The text already establishes that the gasket belongs
   between the front-pump body and case; the missing exploded view remains
   unverified.
3. **Gauge-chart asterisk.** The 1961 appendix and a 1974 Chevrolet reprint
   both show the asterisk with no corresponding note. Find a factory edition
   that prints the note. The chart's numeric U.S. Standard Gage values are
   independently corroborated, but the asterisk's meaning is unknown.

The other three flags concern missing printed body p. 10-52, model 967
convertible body-tram applicability, and the optional 62 A Delcotron's
transistorized regulator service instruction. Their exact evidence and
limits are in the [needs-review list](wiki/10-needs-review.md).

The [continuity report](data/page-continuity-report.txt) records 39
printed-page-number/OCR anomaly pairs. The physical 742-page source map is
complete; review those image labels before claiming printed-page continuity.

## Publication

The source scans' redistribution rights have not been established, as the
[manifest](manifest.yml) states. The repository owner has directed publication
of this PDF on a GitHub Release, consistent with [CONTRIBUTING.md](../../../../CONTRIBUTING.md).
The [manual Release](https://github.com/spacecowboyian/oio-shop-shelf/releases/tag/manuals-corvair-1963)
contains the OCR-indexed combined PDF and all 37 original source PDFs. Their
uploaded sizes match the source inventory, and the manifest and page index
point to the Release. The PDF has been removed from the Git tree as required by
[MAINTAINERS.md](../../../../MAINTAINERS.md). Verify PR CI before a squash merge.
