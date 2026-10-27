# 1963 Corvair release readiness

Status: **hold for source review**. The composite covers 1963 passenger cars,
including the Monza convertible and Spyder option; Corvair 95 commercial
vehicles are outside its scope. Keep `conversion_status: in-progress` until
the release gates below are settled.

## Verified package

- All 18 chapters are reconstructed. The 742-page combined PDF has a complete
  physical-page source map, 742 rendered page images, and a 742-entry page index.
- All 37 staged original factory PDFs match their committed SHA-256 hashes.
  The ignored local combined PDF `prepared.pdf` is 742 pages; its SHA-256 is
  `ef790e2cfa619f643846ea5489071b39be8947ddaf7b9730b62b33e84de1a3fe`.
- Manifest validation, composite-map validation, repository-wide internal-link
  checks, and 41 composite tests pass.
- The [needs-review list](wiki/10-needs-review.md) carries six open flags.
  Flagged material is kept out of authoritative service settings where its
  applicability or value is unverified.

## Source review needed before release

The first three items were designated essential for this release:

1. **Convertible hoist contacts.** The [1963 owner's guide, p. 36](https://corvanatics.org/files/business-office/OwnMan-OwnPP/63OM-E3.pdf#page=20)
   establishes the vehicle-jack placement, but the inherited 1961 hoist
   diagram predates the convertible. Find a Chevrolet instruction that
   explicitly covers hoist contact on a 1962–64 convertible, or keep the
   hoist diagram qualified and decide whether that gap is acceptable at release.
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

## Publication gate

The source scans' redistribution rights have not been established, as the
[manifest](manifest.yml) states. Confirm the repository owner's publication
decision before making the manual and original PDFs public. The combined
`prepared.pdf` is ignored locally, and no `manuals-corvair-1963` GitHub Release
exists. The release workflow in [MAINTAINERS.md](../../../../MAINTAINERS.md)
needs the combined PDF temporarily tracked on the release branch, then uploads
it and the 37 verified originals as Release assets, removes the tracked PDF,
and updates the manifest and page index. Verify the resulting links and CI
before a squash merge.
