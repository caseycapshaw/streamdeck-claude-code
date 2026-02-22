# Claude Code + Any Terminal — Stream Deck Setup

Stream Deck button layout for controlling Claude Code in any terminal emulator (iTerm2, Alacritty, Kitty, Warp, etc.).

Unlike the Ghostty and Terminal variants, Row 1 buttons here use **Text** actions only — they type the command but don't open a specific app. Focus your terminal first, then press the button.

![Button grid](../icons/preview_grid.png)

## Layout (5x3 Grid)

| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
|-------|-------|-------|-------|-------|
| START | CONTINUE | RESUME | YOLO | INIT |
| CLEAR | COMPACT | COST | MODEL | REVIEW |
| STOP | ACCEPT | EXIT | CLR SCR | RETURN |

## Setup

There is no config generator for this variant — set up each button manually in the Stream Deck app as described below. Alternatively, use the Ghostty or Terminal variant's `generate_config.py` as a starting point and change the app path.

### Icons

Each icon lives in `../icons/` in two sizes:
- `*_72.png` — 72x72px (native Stream Deck resolution)
- `*.png` — 144x144px (2x retina quality, recommended)

To set an icon: click the icon area on the button, select **"Set from File..."**, and browse to the PNG.

### Row 1: Session Management

Focus your terminal, then press a button to type the launch command.

| Button | Action Type | Config |
|--------|-----------|--------|
| START | Text | `claude` + Enter |
| CONTINUE | Text | `claude -c` + Enter |
| RESUME | Text | `claude --resume` + Enter |
| YOLO | Text | `claude --dangerously-skip-permissions` + Enter |
| INIT | Text | `/init` + Enter |

For each: drag a **Text** action onto the button, paste the command, and check **"Press Enter after pasting"**.

### Row 2: Slash Commands

| Button | Action Type | Config |
|--------|-----------|--------|
| CLEAR | Text | `/clear` + Enter |
| COMPACT | Text | `/compact` + Enter |
| COST | Text | `/cost` + Enter |
| MODEL | Text | `/model` + Enter |
| REVIEW | Text | `/code-review` + Enter |

### Row 3: Controls

| Button | Action Type | Config | Notes |
|--------|-----------|--------|-------|
| STOP | Hotkey | `Escape` | Cancels current generation |
| ACCEPT | Text | `y` + Enter | Accepts when Claude asks for permission |
| EXIT | Hotkey | `Ctrl+D` | Sends EOF to exit Claude Code |
| CLR SCR | Hotkey | `Ctrl+L` | Clears the terminal screen |
| RETURN | Hotkey | `Return` | Sends the Return/Enter key |

For STOP, EXIT, and CLR SCR: drag a **Hotkey** action onto the button, then click the hotkey field and press the key combination on your keyboard to record it.

## Tips

- The 144px icons look sharper — Stream Deck auto-scales them
- If you want auto-launch behavior, copy `generate_config.py` from the Ghostty or Terminal variant and change the app path to match your terminal
- If a hotkey button doesn't respond correctly, re-record it through the Stream Deck app UI
