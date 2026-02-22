#!/usr/bin/env python3
"""Generate Stream Deck profile config for Claude Code buttons (Apple Terminal)."""

import json
import uuid
import shutil
import os

PROFILE_BASE = os.path.expanduser(
    "~/Library/Application Support/com.elgato.StreamDeck/ProfilesV3/"
    "84CEDC18-AC24-4476-8551-742AF9D038F5.sdProfile"
)
PAGE_ID = "E0C8D94A-585C-4BDC-B467-77EDEBBF464B"
PAGE_DIR = os.path.join(PROFILE_BASE, "Profiles", PAGE_ID)
IMAGES_DIR = os.path.join(PAGE_DIR, "Images")
ICONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons")

# Icon mapping: grid position -> 144px icon filename
ICONS = {
    "0,0": "01_start.png",
    "1,0": "02_continue.png",
    "2,0": "03_resume.png",
    "3,0": "04_yolo.png",
    "4,0": "05_init.png",
    "0,1": "06_clear.png",
    "1,1": "07_compact.png",
    "2,1": "08_cost.png",
    "3,1": "09_model.png",
    "4,1": "10_review.png",
    "0,2": "11_stop.png",
    "1,2": "12_accept.png",
    "2,2": "13_exit.png",
    "3,2": "14_clrscr.png",
    "4,2": "16_return.png",
}


def uid():
    return str(uuid.uuid4())


def img(pos):
    """Return the Images/ path for a grid position."""
    return f"Images/{ICONS[pos]}"


def make_open_terminal():
    return {
        "ActionID": uid(),
        "LinkedTitle": True,
        "Name": "Open",
        "Plugin": {
            "Name": "Open",
            "UUID": "com.elgato.streamdeck.system.open",
            "Version": "1.0",
        },
        "Resources": None,
        "Settings": {"path": '"/System/Applications/Utilities/Terminal.app"'},
        "State": 0,
        "States": [{"Title": "Terminal"}],
        "UUID": "com.elgato.streamdeck.system.open",
    }


def make_delay(ms=500):
    return {
        "ActionID": uid(),
        "LinkedTitle": True,
        "Name": "Delay",
        "Plugin": {
            "Name": "Multi Action",
            "UUID": "com.elgato.streamdeck.multiactions",
            "Version": "1.0",
        },
        "Resources": None,
        "Settings": {"delay": ms},
        "State": 0,
        "States": [{}],
        "UUID": "com.elgato.streamdeck.multiactions.delay",
    }


def make_text_step(text, send_enter=True):
    return {
        "ActionID": uid(),
        "LinkedTitle": True,
        "Name": "Text",
        "Plugin": {
            "Name": "Text",
            "UUID": "com.elgato.streamdeck.system.text",
            "Version": "1.0",
        },
        "Resources": None,
        "Settings": {
            "Hotkey": {"KeyModifiers": 0, "QTKeyCode": 33554431, "VKeyCode": -1},
            "isSendingEnter": send_enter,
            "isTypingMode": False,
            "pastedText": text,
        },
        "State": 0,
        "States": [{}],
        "UUID": "com.elgato.streamdeck.system.text",
    }


def make_multi_action(steps, image_path):
    return {
        "ActionID": uid(),
        "Actions": [{"Actions": steps}, {"Actions": []}],
        "LinkedTitle": True,
        "Name": "Multi Action",
        "Plugin": {
            "Name": "Multi Action",
            "UUID": "com.elgato.streamdeck.multiactions",
            "Version": "1.0",
        },
        "Resources": None,
        "Settings": {},
        "State": 0,
        "States": [{"Image": image_path}],
        "UUID": "com.elgato.streamdeck.multiactions.routine",
    }


def make_text_action(text, send_enter, image_path):
    return {
        "ActionID": uid(),
        "LinkedTitle": True,
        "Name": "Text",
        "Plugin": {
            "Name": "Text",
            "UUID": "com.elgato.streamdeck.system.text",
            "Version": "1.0",
        },
        "Resources": None,
        "Settings": {
            "Hotkey": {"KeyModifiers": 0, "QTKeyCode": 33554431, "VKeyCode": -1},
            "isSendingEnter": send_enter,
            "isTypingMode": False,
            "pastedText": text,
        },
        "State": 0,
        "States": [{"Image": image_path}],
        "UUID": "com.elgato.streamdeck.system.text",
    }


def empty_hotkey():
    return {
        "KeyCmd": False,
        "KeyCtrl": False,
        "KeyModifiers": 0,
        "KeyOption": False,
        "KeyShift": False,
        "NativeCode": -1,
        "QTKeyCode": 33554431,
        "VKeyCode": -1,
    }


def make_hotkey_action(hotkeys_list, image_path):
    # Pad to 4 entries with empty hotkeys
    while len(hotkeys_list) < 4:
        hotkeys_list.append(empty_hotkey())
    return {
        "ActionID": uid(),
        "LinkedTitle": True,
        "Name": "Hotkey",
        "Plugin": {
            "Name": "Activate a Key Command",
            "UUID": "com.elgato.streamdeck.system.hotkey",
            "Version": "1.0",
        },
        "Resources": None,
        "Settings": {"Coalesce": True, "Hotkeys": hotkeys_list},
        "State": 0,
        "States": [{"Image": image_path}],
        "UUID": "com.elgato.streamdeck.system.hotkey",
    }


def terminal_launch_action(command, pos):
    """Multi Action: Open Terminal → Delay 500ms → Text command + Enter."""
    return make_multi_action(
        [make_open_terminal(), make_delay(500), make_text_step(command, send_enter=True)],
        img(pos),
    )


def build_actions():
    actions = {}

    # === Row 0: Session Management ===
    # 0,0: Start Claude
    actions["0,0"] = terminal_launch_action("claude", "0,0")
    # 1,0: Continue Session
    actions["1,0"] = terminal_launch_action("claude -c", "1,0")
    # 2,0: Resume Session
    actions["2,0"] = terminal_launch_action("claude --resume", "2,0")
    # 3,0: YOLO Mode
    actions["3,0"] = terminal_launch_action(
        "claude --dangerously-skip-permissions", "3,0"
    )
    # 4,0: Init Project
    actions["4,0"] = make_multi_action(
        [make_text_step("/init", send_enter=False), make_delay(500), make_text_step("", send_enter=True)],
        img("4,0"),
    )

    # === Row 1: Slash Commands ===
    # 0,1: Clear Context
    actions["0,1"] = make_multi_action(
        [make_text_step("/clear", send_enter=False), make_delay(500), make_text_step("", send_enter=True)],
        img("0,1"),
    )
    # 1,1: Compact
    actions["1,1"] = make_multi_action(
        [make_text_step("/compact", send_enter=False), make_delay(500), make_text_step("", send_enter=True)],
        img("1,1"),
    )
    # 2,1: Check Cost
    actions["2,1"] = make_multi_action(
        [make_text_step("/cost", send_enter=False), make_delay(500), make_text_step("", send_enter=True)],
        img("2,1"),
    )
    # 3,1: Switch Model
    actions["3,1"] = make_multi_action(
        [make_text_step("/model", send_enter=False), make_delay(500), make_text_step("", send_enter=True)],
        img("3,1"),
    )
    # 4,1: Review PR
    actions["4,1"] = make_multi_action(
        [make_text_step("/code-review", send_enter=False), make_delay(500), make_text_step("", send_enter=True)],
        img("4,1"),
    )

    # === Row 2: Controls ===
    # 0,2: Cancel/Stop (Escape)
    actions["0,2"] = make_hotkey_action(
        [
            {
                "KeyCmd": False,
                "KeyCtrl": False,
                "KeyModifiers": 0,
                "KeyOption": False,
                "KeyShift": False,
                "NativeCode": 53,       # macOS kVK_Escape
                "QTKeyCode": 16777216,   # Qt::Key_Escape
                "VKeyCode": 27,          # VK_ESCAPE
            }
        ],
        img("0,2"),
    )

    # 1,2: Accept All (y + Enter) — using Text action for reliability
    actions["1,2"] = make_text_action("y", True, img("1,2"))

    # 2,2: Exit Claude (/exit → Delay 500ms → Enter)
    actions["2,2"] = make_multi_action(
        [make_text_step("/exit", send_enter=False), make_delay(500), make_text_step("", send_enter=True)],
        img("2,2"),
    )

    # 3,2: Clear Screen (Ctrl+L)
    actions["3,2"] = make_hotkey_action(
        [
            {
                "KeyCmd": False,
                "KeyCtrl": True,
                "KeyModifiers": 0,
                "KeyOption": False,
                "KeyShift": False,
                "NativeCode": 37,   # macOS kVK_ANSI_L
                "QTKeyCode": 76,    # Qt::Key_L
                "VKeyCode": 76,     # VK_L
            }
        ],
        img("3,2"),
    )

    # 4,2: Return/Enter — Text action with empty text + send Enter
    actions["4,2"] = make_text_action("", True, img("4,2"))

    return actions


def main():
    # Build page manifest
    page_manifest = {
        "Controllers": [{"Actions": build_actions(), "Type": "Keypad"}],
        "Icon": "",
        "Name": "Claude Code",
    }

    # Copy icons to the page's Images directory
    os.makedirs(IMAGES_DIR, exist_ok=True)
    for pos, icon_file in ICONS.items():
        src = os.path.join(ICONS_DIR, icon_file)
        dst = os.path.join(IMAGES_DIR, icon_file)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  Copied {icon_file}")
        else:
            print(f"  WARNING: {icon_file} not found!")

    # Write page manifest
    manifest_path = os.path.join(PAGE_DIR, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(page_manifest, f, indent=None, separators=(",", ":"))
    print(f"  Wrote {manifest_path}")

    # Update main profile manifest — single page, no page navigation needed
    main_manifest = {
        "Device": {"Model": "20GBA9901", "UUID": "@(1)[4057/128/DL15L2A02880]"},
        "Name": "Default Profile",
        "Pages": {
            "Current": "e0c8d94a-585c-4bdc-b467-77edebbf464b",
            "Default": "e0c8d94a-585c-4bdc-b467-77edebbf464b",
            "Pages": ["e0c8d94a-585c-4bdc-b467-77edebbf464b"],
        },
        "Version": "3.0",
    }
    main_manifest_path = os.path.join(PROFILE_BASE, "manifest.json")
    with open(main_manifest_path, "w") as f:
        json.dump(main_manifest, f, indent=None, separators=(",", ":"))
    print(f"  Wrote {main_manifest_path}")

    print("\nDone! Restart the Stream Deck app to apply changes.")


if __name__ == "__main__":
    main()
