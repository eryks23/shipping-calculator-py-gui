# shipping-calculator-py-gui

> A lightweight desktop GUI for estimating shipping costs based on weight, price per kg, and distance.

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-informational)](https://docs.python.org/3/library/tkinter.html)
[![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)]()
[![License](https://img.shields.io/badge/License-DO%20UZUPEŁNIENIA-lightgrey)](LICENSE)

---

## Description

`shipping-calculator-py-gui` is a Python desktop application built with Tkinter that calculates shipping costs from three inputs: package weight, price per kilogram, and distance. It classifies packages by weight category and provides a dedicated details view showing shipping cost, package weight, and average cost per kilometre. The app requires no external dependencies — only Python's standard library.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Cost Formula](#cost-formula)
- [Application Structure](#application-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- **Instant cost calculation** — computes shipping cost from weight, price/kg, and distance in one click
- **Automatic package classification** — labels packages as Light, Medium, or Heavy based on weight thresholds
- **Quick summary** — renders a one-line cost + category summary directly on the input screen
- **Details view** — dedicated screen displays shipping cost, package weight, and average cost per km
- **Input resilience** — accepts both dot and comma as decimal separators; shows a clear error dialog on invalid input
- **Full reset** — single button wipes all inputs, resets application state, and returns to the main screen
- **Zero external dependencies** — runs on any Python 3.6+ installation without `pip install`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.6+ |
| GUI framework | Tkinter (stdlib) |
| Dialogs | `tkinter.messagebox` (stdlib) |

---

## Requirements

- Python **3.6 or higher**
- No third-party packages required

Verify your Python version:

```bash
python --version
```

Tkinter ships with the standard CPython distribution. On some Linux distributions it must be installed separately:

```bash
# Debian / Ubuntu
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/eryks23/shipping-calculator-py-gui.git

# 2. Enter the project directory
cd shipping-calculator-py-gui
```

No virtual environment or additional setup is required.

---

## Usage

```bash
python main.py
```

### Step-by-step workflow

1. Enter **Weight (kg)**, **Price per kg (USD)**, and **Distance (km)** in the input fields.
2. Click **Calculate** — the estimated cost appears below the fields.
3. Click **Rate** — the package is classified as Light, Medium, or Heavy.
4. Click **Summary** — displays a combined one-line summary (requires both Calculate and Rate to have been run first).
5. Click **Details** — opens the Details screen with shipping cost, package weight, and average cost per km.
6. On the Details screen, click **Reset** to clear all data and return to the main screen, or **Back** to return without clearing.

> **Tip:** Both dot (`.`) and comma (`,`) are accepted as decimal separators, e.g. `2.5` and `2,5` are equivalent.

---

## Cost Formula

```
cost = weight (kg) × price_per_kg (USD/kg) × (distance (km) / 100)
```

**Example:** A 3 kg package, priced at 5 USD/kg, shipped 200 km:

```
cost = 3 × 5 × (200 / 100) = 30.00 USD
```

**Package classification thresholds:**

| Weight | Category |
|---|---|
| < 1 kg | Light package |
| 1 – 5 kg | Medium package |
| > 5 kg | Heavy package |

---

## Application Structure

```
shipping-calculator-py-gui/
└── main.py       # Single-file application — entry point and full GUI logic
```

### Class `ShippingApp`

| Method | Description |
|---|---|
| `__init__()` | Initialises the root window, state variables (`cost`, `package_type`), and both card frames |
| `build_card_1()` | Constructs the input / calculation screen (Card 1) |
| `build_card_2()` | Constructs the shipping details screen (Card 2) |
| `show_card(card)` | Hides all cards and packs the requested one |
| `get_data()` | Reads and validates the three input fields; returns `(weight, price, distance)` or `(None, None, None)` on error |
| `calculate_cost()` | Computes `cost = weight × price × (distance / 100)` and updates the Card 1 label |
| `rate_package()` | Assigns `package_type` based on weight thresholds and updates the Card 1 label |
| `show_summary()` | Renders the combined cost + type summary label on Card 1 |
| `go_to_details()` | Computes average cost per km, populates Card 2 labels, and navigates to Card 2 |
| `reset_data()` | Clears all `Entry` widgets, resets state variables, and returns to Card 1 |

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: describe your change"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request against `main`.

Please keep the project free of external dependencies unless there is a strong justification for introducing them.

---

## License

[DO UZUPEŁNIENIA: Add your license here, e.g. MIT, Apache 2.0] — see [LICENSE](LICENSE) for details.

---

## Author

**eryks23** — [github.com/eryks23](https://github.com/eryks23)
