# Claude Code × Ghostty — Stream Deck Icon Pack

16 minimal monochrome icons for controlling Claude Code in Ghostty via Stream Deck.

## Layout (5×3 Grid)

| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
|-------|-------|-------|-------|-------|
| START | CONTINUE | RESUME | YOLO | INIT |
| CLEAR | COMPACT | COST | MODEL | REVIEW |
| STOP | ACCEPT | EXIT | CLR SCR | RETURN |

## Files

Each icon comes in two sizes:
- `*_72.png` — 72×72px (native Stream Deck resolution)
- `*.png` — 144×144px (2× retina quality, recommended)

## How to Install Icons

1. Open the **Stream Deck** app
2. Drag an action (e.g., Multi Action, Text, Hotkey) onto a button
3. Click the icon area on the button in the top-left
4. Select **"Set from File..."**
5. Browse to the icon PNG you want to use
6. Repeat for each button

## Button Programming Reference

### Row 1: Session Management

Each button opens Ghostty, waits for it to focus, then types a Claude Code launch command.

| Button | Action Type | Config |
|--------|-----------|--------|
| START | Multi Action | Open → Ghostty.app → Delay 500ms → Text: `claude` + Enter |
| CONTINUE | Multi Action | Open → Ghostty.app → Delay 500ms → Text: `claude -c` + Enter |
| RESUME | Multi Action | Open → Ghostty.app → Delay 500ms → Text: `claude --resume` + Enter |
| YOLO | Multi Action | Open → Ghostty.app → Delay 500ms → Text: `claude --dangerously-skip-permissions` + Enter |
| INIT | Text | `/init` + Enter |

#### Multi Action Step-by-Step

For each session launcher button (START, CONTINUE, RESUME, YOLO):

1. **Step 1 — Open**: Action → "Open", Path → `/Applications/Ghostty.app`
2. **Step 2 — Delay**: Action → "Delay", Duration → `500` ms
3. **Step 3 — Text**: Action → "Text", paste the command text, check **"Press Enter after pasting"**

| Button | Text value |
|--------|-----------|
| START | `claude` |
| CONTINUE | `claude -c` |
| RESUME | `claude --resume` |
| YOLO | `claude --dangerously-skip-permissions` |

### Row 2: Slash Commands

These assume Ghostty with an active Claude Code session is already focused.

| Button | Action Type | Config |
|--------|-----------|--------|
| CLEAR | Text | `/clear` + Enter |
| COMPACT | Text | `/compact` + Enter |
| COST | Text | `/cost` + Enter |
| MODEL | Text | `/model` + Enter |
| REVIEW | Text | `/code-review` + Enter |

For each: drag a **Text** action onto the button, paste the slash command, and check **"Press Enter after pasting"**.

### Row 3: Controls

| Button | Action Type | Config | Notes |
|--------|-----------|--------|-------|
| STOP | Hotkey | `Escape` | Cancels current generation |
| ACCEPT | Text | `y` + Enter | Accepts when Claude asks for permission |
| EXIT | Hotkey | `Ctrl+D` | Sends EOF to exit Claude Code |
| CLR SCR | Hotkey | `Ctrl+L` | Clears the terminal screen |
| RETURN | Hotkey | `Return` | Sends the Return/Enter key |

#### Hotkey Setup

For STOP, EXIT, and CLR SCR: drag a **Hotkey** action onto the button, then click the hotkey field and press the key combination on your keyboard to record it.

For ACCEPT: use a **Text** action with `y` as the text and **"Press Enter after pasting"** checked.

For RETURN: drag a **Hotkey** action onto the button, click the hotkey field, and press the `Return` key to record it.

## Tips

- The **72px** versions are the native Stream Deck resolution
- Stream Deck will automatically scale the 144px versions — they'll look sharper
- You can customize the label text in the Stream Deck app independently of the icon
- If a hotkey button doesn't respond correctly after programmatic setup, re-record it through the Stream Deck app UI — click the hotkey field and press the key
