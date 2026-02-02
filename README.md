# AVERMEDIA-BUTTON-MEDIA-KEY-REMAP-PYTHON-SCRIPT-HID
Python module for AverMedia ReCentral USB Button

# AVerMedia ReCentral USB Button Media Controller

This repository contains a Python script that repurposes the **AVerMedia ReCentral USB Button** (Legacy Accessory) into a global media controller. By intercepting HID signals from the physical button, this script allows you to control music and video playback using multi-tap gestures.

## 🚀 Features
* **Multi-Tap Support**: Maps physical button presses to standard media keys.
* **Low Latency**: Uses non-blocking HID reading for responsive control.
* **Global Hotkeys**: Works even when your media player (Spotify, YouTube, VLC) is in the background.

### Gesture Mapping
| Taps | Action |
| :--- | :--- |
| **1x** | Play / Pause |
| **2x** | Next Track |
| **3x** | Previous Track |

---

## 🛠️ Requirements
* **Operating System**: Windows
* **Hardware**: AVerMedia ReCentral USB Button (VID: 0x07CA, PID: 0x9850).
* **Python**: 3.x
* **Dependencies**: `pip install hidapi keyboard`

---

## 🚦 Getting Started
1. **Plug in** your AVerMedia USB button.
2. **Run the script**: `python media_controller.py`
3. **Permissions**: Run your terminal as **Administrator** if the keyboard events are not registered globally.

---

## 📝 How it Works
The script uses `hidapi` to monitor raw data reports from the USB device. It listens for state changes on the second byte of the HID report (`report[1]`). A `threading.Timer` (0.5s) "collects" taps before determining the command. Once the threshold passes, the key is simulated via the `keyboard` module.

---

## ⚙️ Configuration
Device ID: If your specific model has a different Revision ID, you may need to run a HID enumeration script to verify the VENDOR_ID and PRODUCT_ID.

Adjust tap speed sensitivity by modifying `TAP_THRESHOLD` in the script:
```python
# Decrease for faster double-clicks, increase for more "relaxed" clicking
TAP_THRESHOLD = 0.5

