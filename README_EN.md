<sub><a href="README.md">中文</a> · <b>English</b></sub>

<div align="center">

# University.skill

<img src="assets/hero.gif" width="800" alt="Put a university professor in your AI. Turn any topic into a real university lecture." />

**Put a university professor in your AI. Turn any topic into a real university lecture.**

**把一位大学教授装进你的 AI，把任何主题变成一堂真正的大学课。**

Tell your AI what you want to learn. Let it teach from the foundations to the underlying principles and practical examples. Want a course you can keep? Ask it to write a PDF textbook.

[中文](README.md) · [Skill](SKILL.md) · [Worked example](examples/gradient-descent.md)

</div>

---

## Start a Course

```text
Write me a PDF textbook: protein structure prediction and design with AI4S, from scratch.
Write me a PDF textbook: JEPA models from scratch, with worked calculations and minimal code.
Write me a PDF textbook: the development and principles of recursive self-improvement (RSI).
Teach me attention from high-school mathematics. Work through every matrix calculation.
```

Ask an Agent Skills-compatible assistant to install this repository, or clone it into its skill directory. Keep references and assets with SKILL.md. PDF production requires a Chinese-capable LaTeX installation; code verification requires the relevant runtime.

## What It Produces

| Mode | Deliverable |
| --- | --- |
| One lecture | A complete explanation, worked example, exercises and answers |
| Technical textbook | Approximately 25–35 pages, implementation and mathematical foundations |
| Extended lecture notes | Approximately 40 pages, chapter sources, PDF and verification report |

Page counts are targets measured after compilation. Instructions are currently Chinese; the assistant should follow the learner's requested language.

The teaching engine is adapted from the maintainer's masterclass-textbook-writer and 40-page lecture-writing skills. It combines prerequisite-aware explanations, low-dimensional calculations, chapter-by-chapter writing, restrained analogies and source verification. See [provenance](docs/provenance.md).

The README presentation follows [nuwa-skill](https://github.com/alchaincyf/nuwa-skill); evaluation is inspired by [darwin-skill](https://github.com/alchaincyf/darwin-skill). The opening animation was made using [huashu-design](https://github.com/alchaincyf/huashu-design).

This is an initial release with designed examples, not a measured learning-outcomes study or university accreditation.
