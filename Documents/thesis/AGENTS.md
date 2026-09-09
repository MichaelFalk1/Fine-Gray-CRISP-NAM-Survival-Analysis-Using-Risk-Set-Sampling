# AGENTS.md

## Project Purpose
This repository contains a LaTeX thesis/report and a separate proposal. The main document lives in `Paper/`, and the proposal lives in `Preposal/`.

## Key Structure
- `Paper/` — main research report and bibliography.
- `Paper/utils/` — local LaTeX style files and images.
- `Paper/images/` — figures and generated result folders.
- `Preposal/` — short proposal document with its own build setup.
- `References.bib` / `references.bib` — bibliography sources for the respective documents.

## Working Conventions
- Prefer small, targeted edits to existing `.tex` files rather than rewriting large sections.
- Keep labels, references, and citations consistent. If you add or rename a section, update cross-references and bibliography keys if needed.
- Preserve the existing Wits thesis style and formatting conventions already present in the LaTeX preamble.
- When adding figures, keep image paths relative to the document folder and avoid moving files unless necessary.
- Do not introduce unsupported packages or broad formatting changes unless the task explicitly requires them.

## Build and Validation
Run builds from the document directory so LaTeX can resolve local includes and bibliography files.

Main paper:
```bash
cd Paper
pdflatex Paper.tex
bibtex Paper
pdflatex Paper.tex
pdflatex Paper.tex
```

Proposal:
```bash
cd Preposal
make
```

If the build produces warnings about missing references, undefined labels, or bibliography entries, fix those before finishing.

## Agent Guidance
- For thesis edits, assume the user is working on academic writing, not software development; keep changes precise and scholarly.
- Preserve the existing chapter structure and terminology unless explicitly asked to revise it.
- Treat citations as part of the document’s argument: prefer using the established bibliography keys already present in the TeX files.
- When content is duplicated across the main paper and proposal, keep them aligned only if the user asks for synchronization.
- If asked to generate new content, prefer concise academic prose that fits the current report style and avoids inventing unsupported claims.

## Common Pitfalls
- Relative paths differ between `Paper/` and `Preposal/`; always compile from the correct directory.
- `.bib` files must stay in sync with `\cite{...}` entries.
- TeX compilation may require repeated runs to resolve references and table-of-contents updates.
