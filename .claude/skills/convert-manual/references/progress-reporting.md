# Optional conversion progress reporting

Use this only when the contributor requests it. Reporting is **disabled by
default**, adds no required dependency, and does not change conversion quality
gates. The assistant running the skill maintains these records using its existing
file and connector tools; the pipeline scripts do not read this configuration or
automatically send anything. No daemon, scheduler, or unattended runtime is added.

## Set up once for this contributor and run

1. Ask for the destination (for example, their Notion page/database, another
   supported service, or a local file only) and confirm which progress metadata
   may be shared and with whom. A repository example is not permission to publish.
2. Verify the intended account/workspace and destination through the available
   connector. Confirm access without broadening permissions. If login, a connector,
   or destination authorization is missing, stop remote setup and explain the gap;
   conversion may continue without remote reporting. Do not invent an integration.
3. Keep the per-user configuration and job-to-record mapping outside committed
   files. In a repository checkout, `.oio-local/` is gitignored. For an installed
   skill, use the contributor's private working directory instead of editing the
   installed package. Never put tokens, passwords, private page IDs, local absolute
   paths, or a real workspace URL in the skill, manifest, PR, or example config.
4. Give each conversion run a stable `job_id`, preserve it on resume, and save the
   destination record identifier privately. A genuinely new run gets a new ID.
   One orchestrator owns publication; parallel workers report to it rather than
   creating competing records. Reconfirm a changed account, destination, or scope.

Example private config, **inert until the contributor enables and configures it**:

```json
{
  "enabled": false,
  "provider": null,
  "destination": null,
  "job_id": null
}
```

The assistant can read this convention from `.oio-local/convert-progress.json`.
It is not a new CLI flag or an automatically loaded application setting. A config
file alone is not authorization. For local-only reporting, set `provider` to
`local` and select a private file; otherwise use the contributor's verified
connector. Never fall back to another person's Notion workspace.

## Checkpoint contract

Maintain a small structured checkpoint, for example in
`.oio-local/progress/<job_id>.json`, and mirror only its approved metadata. Write
locally before publishing so a remote outage does not lose the checkpoint.

- **Identity:** schema version, stable job ID, increasing revision, manual slug
  and title, source fingerprint or revision when available (no source contents).
- **Time and state:** timezone-aware `observed_at`, last observed state
  (`running`, `idle`, `blocked`, `completed`, or `unknown`) and current phase.
  Record publication time separately; it must not replace the observation time.
- **Coverage:** 1-based source-PDF page ranges and counts for `processed`,
  `reviewed`, and `accepted`, each with its meaning and evidence. State total source
  pages when known. Use `null`/`unknown` for unverified values, not zero. Printed
  page labels belong in a separate field.
- **Artifacts:** observed counts of chapter files, diagrams and indexes, with
  safe relative artifact references where permitted. Do not equate file count or
  highest page number with complete page coverage.
- **Provenance:** worker/model roles actually observed (for example, Qwen drafted
  a range; Codex checked source images and accepted or corrected it). Do not credit
  a draft model with the final accepted output without evidence.
- **Quality and next step:** checks run and their results, unresolved review flags,
  concise sanitized blocker/error, and the next pending range or checkpoint.
  A completed OCR/render batch is not a completed manual.

`processed` means the named phase produced an artifact for those pages. `reviewed`
means source comparison was performed; it can still have unresolved issues.
`accepted` means the conversion orchestrator accepted the output under the
existing cleanup/verification rules. Record outstanding review flags alongside
accepted coverage; acceptance is not a warranty of correctness. These sets need
not be contiguous. Never derive acceptance from elapsed time, a progress bar,
or a user's rough recollection. If only the OCR stage is known, leave later stages
unknown. Retain source references locally so a later session can verify the claim.

Example checkpoint (fictional, not a real conversion result):

```json
{
  "schema_version": 1,
  "job_id": "example-run-01",
  "revision": 3,
  "manual_slug": "example-manual",
  "source_revision": "example-source-v1",
  "observed_at": "2026-01-01T14:00:00Z",
  "last_observed_state": "idle",
  "phase": "cleanup",
  "source_page_total": 100,
  "coverage": {
    "processed": {"phase": "ocr", "ranges": [[1, 100]], "count": 100, "evidence": "local OCR output checked"},
    "reviewed": {"ranges": [[1, 8], [10, 10]], "count": 9, "evidence": "source-image review log"},
    "accepted": {"ranges": [[1, 8]], "count": 8, "evidence": "accepted chapter revision"}
  },
  "artifact_counts": {"chapters": 1, "diagrams": 0, "indexes": 0},
  "model_roles": ["worker: draft", "orchestrator: source-image review"],
  "checks": ["pages 1-8 compared against source images"],
  "open_review_flags": 1,
  "blocker": null,
  "next_checkpoint": "Resolve page 10 review flag; review page 9"
}
```

## Publish without duplicating or losing state

At setup/resume, after completed batches or phase transitions, and before a
planned pause/blocker/finish:

1. Observe actual outputs and process state. Update the local checkpoint and its
   revision only for new evidence. Preserve unknowns and unresolved errors.
2. For Notion, find the existing record by the private mapping or exact `job_id`
   in the contributor's selected destination. Create one only if absence is
   confirmed. Read the current record first; preserve user edits and unrelated
   blocks/properties. Use a dedicated checkpoint block/section or agreed database
   properties, never replace an entire personal page. Keep a brief revision history
   if supported. Other providers should follow the same contract.
3. Refuse to overwrite a newer revision or a different source/run. Reconcile the
   actual state before proceeding. If a create/update outcome is uncertain, read
   for that job/revision before retrying; do not blindly create duplicate records.
4. Read back the published checkpoint. Only then record the remote receipt and
   `published_at` privately and say it was published. An inaccessible destination
   means reporting is blocked, not that the conversion failed or stopped.

On an offline/permission failure, retain the local checkpoint and report the
publishing gap once. Retry when connectivity returns or at the next normal
checkpoint, not in an unbounded loop. Never change authentication, permissions,
or start a second conversion to repair reporting. If no tool can write a remote
destination, a local record is the only deliverable; do not claim a Notion sync.

## Reading progress while the worker is unavailable

Always show “last observed at …” with the saved state. A saved `running` value is
not a live heartbeat. If the worker cannot be contacted, say current state is
unknown, even if the last record says running. A crash may prevent a final
checkpoint. Do not advance page counts or mark completion from a stale snapshot.

After reconnecting, verify the process and artifacts before publishing a newer
observation. Only mark the manual completed after the original skill's package
verification gates pass. This optional reporting never relaxes those gates.

## Privacy and disabling

Publish only approved progress metadata. Exclude PDF pages, extracted/OCR text,
full logs, chat transcripts, credentials, personal machine paths and private
URLs unless separately authorized for that destination. Sanitize errors rather
than copying command output. Destinations are per contributor and may be shared
with others, so inspect their scope before the first write.

On `enabled: false` or a request to stop reporting, make no further remote writes.
Continue the original conversion workflow. Keep or remove private local records
according to the contributor's request; do not delete remote history implicitly.
