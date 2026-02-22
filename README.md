# Stream Deck Icon Pack for Claude Code

16 minimal monochrome icons and pre-built profiles for controlling Claude Code from a Stream Deck.

![Button grid](icons/preview_grid.png)

## Layout (5x3 Grid)

| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
|-------|-------|-------|-------|-------|
| START | CONTINUE | RESUME | YOLO | INIT |
| CLEAR | COMPACT | COST | MODEL | REVIEW |
| STOP | ACCEPT | EXIT | CLR SCR | RETURN |

## Choose Your Terminal

Each variant configures the same 15-button grid. The only difference is how Row 1 (session launchers) opens your terminal.

| Variant | Row 1 Behavior | Auto-Setup |
|---------|---------------|------------|
| [**claude+ghostty**](claude+ghostty/) | Opens Ghostty.app, types command | `python3 generate_config.py` |
| [**claude+terminal**](claude+terminal/) | Opens Apple Terminal.app, types command | `python3 generate_config.py` |
| [**claude+generic**](claude+generic/) | Types command only (you focus the terminal) | Manual setup |

Rows 2–3 (slash commands and controls) are identical across all variants.

## Icons

All icons live in [`icons/`](icons/) with two sizes per button:
- `*_72.png` — 72x72px (native Stream Deck resolution)
- `*.png` — 144x144px (2x retina quality, recommended)

## Quick Start

1. Pick the variant for your terminal
2. Run `python3 generate_config.py` (Ghostty or Terminal) or follow the manual setup guide (Generic)
3. Restart the Stream Deck app
