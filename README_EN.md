<sub><a href="README.md">中文</a> · <b>English</b></sub>

<div align="center">

# University.skill

<img src="assets/hero.gif" width="800" alt="Put a university professor in your AI. Turn any topic into a real university lecture." />

**Put a university professor in your AI. Turn any topic into a real university lecture.**

**把一位大学教授装进你的 AI，把任何主题变成一堂真正的大学课。**

Tell your AI what you want to learn. Let it teach from the foundations to the underlying principles and practical examples. Want a course you can keep? Ask it to write a PDF textbook.

[中文](README.md) · [Deep textbook skill](skills/masterclass-textbook-writer/SKILL.md) · [40-page lecture skill](skills/masterclass-40page-writer/SKILL.md)

</div>

---

## Start a Course

```text
Write me a PDF textbook: protein structure prediction and design with AI4S, from scratch.
Write me a PDF textbook: JEPA models from scratch, with worked calculations and minimal code.
Write me a PDF textbook: the development and principles of recursive self-improvement (RSI).
Teach me attention from high-school mathematics. Work through every matrix calculation.
```

Ask an Agent Skills-compatible assistant to install this repository. For manual installation, clone the repository and copy both directories under `skills/` into your runtime's skill directory. Each skill is self-contained with its own prompts and references. PDF production requires a Chinese-capable LaTeX installation; code verification requires the relevant runtime.

## What It Produces

| Bundled skill | Deliverable |
| --- | --- |
| `masterclass-textbook-writer` | A 25–35 page technical textbook with derivations, worked calculations, implementation and mathematical foundations |
| `masterclass-40page-writer` | A roughly 40-page, high-school-accessible course with chapter sources, appendices and a compiled PDF |

Page counts are targets measured after compilation. Instructions are currently Chinese; the assistant should follow the learner's requested language.

The repository contains the maintainer's two complete skills rather than a third wrapper skill. Together they cover prerequisite-aware explanations, low-dimensional calculations, chapter-by-chapter writing, restrained analogies and source verification.

The project acknowledges [Wudaokou Nash](https://github.com/wdkns/wdkns-skills) and [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) as its two sources of inspiration.

This repository includes complete sample textbooks, but does not claim measured learning outcomes or university accreditation.

## Complete PDF Samples

### Protein Structure Prediction and Design with AI4S

A 47-page, high-school-accessible textbook that progresses from atoms and protein folding to AlphaFold2, diffusion, ProteinMPNN, RFdiffusion, worked calculations, code, a glossary and self-tests.

<p align="center">
  <a href="assets/samples/pdfs/protein-structure-design-ai4s.pdf"><img src="assets/samples/screenshots/protein-cover.png" width="31%" alt="AI4S textbook cover and contents"></a>
  <a href="assets/samples/pdfs/protein-structure-design-ai4s.pdf"><img src="assets/samples/screenshots/protein-alphafold.png" width="31%" alt="AlphaFold2 architecture explanation"></a>
  <a href="assets/samples/pdfs/protein-structure-design-ai4s.pdf"><img src="assets/samples/screenshots/protein-worked-example.png" width="31%" alt="Worked three-point calculation"></a>
</p>

**[Open the complete 47-page PDF](assets/samples/pdfs/protein-structure-design-ai4s.pdf)**

### Muon Optimizer and Matrix Orthogonalization

A 13-page masterclass from gradients and AdamW limitations through polar factors, Newton-Schulz iteration, PyTorch implementation and rigorous mathematical appendices.

<p align="center">
  <a href="assets/samples/pdfs/muon-optimizer-masterclass.pdf"><img src="assets/samples/screenshots/muon-cover.png" width="31%" alt="Muon optimizer textbook opening"></a>
  <a href="assets/samples/pdfs/muon-optimizer-masterclass.pdf"><img src="assets/samples/screenshots/muon-orthogonalization.png" width="31%" alt="Geometric explanation of Muon orthogonalization"></a>
  <a href="assets/samples/pdfs/muon-optimizer-masterclass.pdf"><img src="assets/samples/screenshots/muon-code.png" width="31%" alt="Newton-Schulz iteration and PyTorch code"></a>
</p>

**[Open the complete 13-page PDF](assets/samples/pdfs/muon-optimizer-masterclass.pdf)**

## Repository Layout

```text
university-skill/
├── assets/                     # Hero animation, complete PDFs and screenshots
├── skills/
│   ├── masterclass-textbook-writer/
│   └── masterclass-40page-writer/
├── README.md
└── README_EN.md
```
