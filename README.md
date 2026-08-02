# Virtual Painter using OpenCV

A real-time Virtual Painter built with **Python** and **OpenCV** that lets you draw in the air using a colored object as brush tracked by your webcam.

The application detects a colored object in real time, tracks its movement, and draws smoothly on a virtual canvas with adjustable brush settings.

---

## Functionalities

- Real-time color tracking using HSV segmentation
- Adjustable brush color using trackbars for RGB and size
- Modes: Drawing mode, Eraser mode and Idle mode (tracking without drawing).
- Mirrored camera feed for natural interaction
- Real-time FPS counter
- In-app HUD displaying:
  - Current mode
  - Brush preview
  - Brush size
- Help[h] for viewing Controls
- Save drawings as PNG images
- Clear canvas
- Cursor smoothing for stable drawing
- Modular project structure

---

## Demo

![Demo](screenshots/demo.png)

---

## Controls

| Key | Action |
|------|--------|
| **D** | Draw Mode |
| **E** | Eraser Mode |
| **I** | Idle Mode |
| **C** | Clear Canvas |
| **S** | Save Drawing |
| **Q** | Quit |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/virtual-painter.git
cd virtual-painter
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python src/main.py
```

---

## Project Structure

```
virtual-painter/
│
├── src/
│   ├── main.py
│   ├── color_picker.py
│   ├── hud.py
│   ├── input_handler.py
│   ├── utils.py
│   └── config.py
│
├── screenshots/
├── requirements.txt
├── LICENSE.md
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python
- OpenCV
- NumPy

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.