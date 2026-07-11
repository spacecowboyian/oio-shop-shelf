# Running without a local CLI ("cloud" / plain chat)

The conversion pipeline needs system binaries — `ocrmypdf` (which pulls in
`tesseract` + `ghostscript`) and poppler (`pdftotext`, `pdftoppm`). These are
apt/brew installs, **not** pip packages. A bare chat assistant (claude.ai, Gemini,
ChatGPT web) has no persistent shell, filesystem, or network to install them, so it
**cannot OCR a scan or emit a PDF**. This is a system-dependency limit, not a Python
limit — rewriting in another language wouldn't remove it.

Route by capability:

## Best no-CLI path — Google Colab (sanctioned)

A hosted notebook gives non-CLI contributors real compute for free:

1. Open a Colab notebook (the repo ships one; if not yet, scaffold from this file —
   see epic #4).
2. First cell installs the binaries + Python deps:
   ```python
   !apt-get -qq update && apt-get -qq install -y ocrmypdf tesseract-ocr poppler-utils ghostscript
   !pip -q install pymupdf pyyaml
   !git clone https://github.com/spacecowboyian/oio-shop-shelf.git
   ```
3. Upload the PDF (or paste a Drive link and download it in-cell).
4. Run the pipeline cells (`scripts/01`…`08`) against `manuals/<slug>/`.
5. Download the resulting package + `*-indexed.pdf`.
6. Bring the markdown back to the chat LLM for the **cleanup** pass (step 4) and to
   draft the **pull request** (see `pull-request-walkthrough.md`).

Colab does the binary-heavy work; the chat model does the judgment-heavy work.

## Partial path — ChatGPT Advanced Data Analysis

Its Python sandbox has `tesseract` preinstalled and can run PyMuPDF, so **small**
manuals can go end to end. Limits: no network (can't add missing system deps),
file-size and runtime caps. Fine for a short manual; unreliable for a full one.

## Chat-only, no code execution at all

The assistant can still help with the parts that are pure language:

- **Cleanup** — paste already-OCR'd chapter text and reconstruct it to markdown
  following `scripts/04_cleanup_methodology.md` (Rule 0: never change a number).
- **PR authoring** — write the branch/commands and a good PR description.

It **cannot** OCR an image-only scan or produce the indexed PDF — those need one of
the paths above.

## Rule of thumb

| Contributor has… | OCR | Build PDF | Cleanup | PR help |
| --- | --- | --- | --- | --- |
| Local CLI agent + binaries | ✅ | ✅ | ✅ | ✅ |
| Google Colab | ✅ | ✅ | ✅ (in chat) | ✅ |
| ChatGPT ADA | ⚠️ small | ⚠️ small | ✅ | ✅ |
| Plain chat only | ❌ | ❌ | ✅ | ✅ |
