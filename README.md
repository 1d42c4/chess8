# OnePageLove Chess

**Live website: [https://knightway8.github.io/chess8/](https://knightway8.github.io/chess8/)**

1,000 standalone chess lessons in 20 divisions, plus interactive Hippo and King’s Indian courses.

This repository publishes the complete contents of the supplied `OnePageLove` folder, with lessons grouped into category subfolders. The root `index.html` is the website entry point.

## Start learning

- [Searchable course home](index.html)
- [Complete lesson sitemap](SITEMAP.html)
- [Hippopotamus course](hippopotamus-course.html)
- [King’s Indian course](kings-indian-course.html)
- [Hippo counter trainer](hippo-counter-trainer.html)

## All four chess websites

| Repository | Collection | GitHub Pages |
| --- | --- | --- |
| [chess7](https://github.com/knightway8/chess7) | Chess Combat School | [Open site](https://knightway8.github.io/chess7/) |
| [chess8](https://github.com/knightway8/chess8) | OnePageLove Chess | [Open site](https://knightway8.github.io/chess8/) |
| [chess9](https://github.com/knightway8/chess9) | Positional Logic | [Open site](https://knightway8.github.io/chess9/) |
| [chess10](https://github.com/knightway8/chess10) | The Earlier Advantage | [Open site](https://knightway8.github.io/chess10/) |

## Lesson folders

The 1,000 lessons are organized into 20 category folders containing 50 lessons each. [Browse the lesson directory](lessons/README.md). Each folder includes a README. Navigation, search, related lessons, and download instructions use the new paths.

Older GitHub Pages lesson bookmarks are recognized by the custom 404 page and redirected in the browser, preserving query strings and anchors. With JavaScript disabled, use the course-home link on that page. Original GitHub file URLs remain available in commit history.

## Files and downloads

All 1,035 original source files are included. Any existing course archives, tools, and documentation remain available. Use **Code → Download ZIP** to download this repository, or clone it with Git:

```sh
git clone https://github.com/knightway8/chess8.git
```

`SOURCE_MANIFEST.json` records every original file, its original path when moved, and its original and current uploaded SHA-256 hashes, and the deliberate publishing changes. These include the repository README, Pages settings files, and any repaired site links.

## Check future changes

Run `python tools/check_layout.py` before publishing. It checks that every directory stays below 1,000 entries, all 1,000 lessons are present, local links resolve, and source-manifest checksums match.

## Publishing and protection

GitHub Pages serves the committed files from the root of `main`. No package installation or build step is needed to view the site. The `.nojekyll` file enables direct static-file publishing.

The repository’s active default-branch rules require pull requests, block force pushes, and block branch deletion, with no bypass actors configured. Submit future content changes through a pull request, then merge to publish them. These rules preserve branch history; an owner can still change the rules or delete the repository, and approved changes can still modify or remove files.

## Original project documentation

The original project README is retained below. Some setup notes describe the project before this GitHub Pages publication.

---

# OnePageLove Chess

**1,000 free, standalone chess lessons. One subject. One HTML page.**

This repository is designed for GitHub Pages and for offline use. Every lesson under `lessons/` is a completely self-contained HTML file with its own CSS and no external dependencies.

## What is included

- **1,000 lessons**
- **20 training divisions**
- Opening foundations
- White opening repertoires
- Black defenses
- Pawn structures
- Strategy and piece play
- Attacking and defense
- Tactical motifs
- Calculation
- Pawn, rook, minor-piece, queen and mixed endgames
- Practical tournament chess
- Study and improvement
- Chess mathematics, rules and history

Each of the 200 base subjects has five independent lessons:

1. Complete Guide
2. Recognition Guide
3. Decision Rules
4. Mistakes and Counterplay
5. Training and Self-Test

## Philosophy

The goal is not to manufacture pages. Each page should teach a reusable chess idea and stand on its own so a learner can arrive from a search engine or GitHub Pages without reading anything else first.

AI can create excellent educational material when it is asked to explain, organize, test and drill ideas rather than merely produce text. These pages are intended as a free resource for anyone who wants to learn.

## GitHub Pages

The package includes:

- `index.html` — searchable homepage
- `.nojekyll`
- `404.html`
- `SITEMAP.html`
- `sitemap.xml`
- `categories/`
- `lessons/`
- `tools/verify_site.py`

To publish, push the files to your repository and configure GitHub Pages to deploy from `main` and `/(root)`.

## Accuracy

AI is powerful, but not infallible. Chess is concrete. Verify critical forcing opening lines and current competition rules with authoritative sources before serious tournament use.

Rules/history references:
- FIDE Laws of Chess: https://handbook.fide.com/chapter/E012023
- Claude Shannon, *Programming a Computer for Playing Chess* (1950): https://vision.unipv.it/IA1/ProgrammingaComputerforPlayingChess.pdf

## Use

**AI-made by ChatGPT for the OnePageLove chess-learning project. Free educational material; not intended for resale. Chess itself is a centuries-old game, while these pages are original AI-generated instructional material.**
