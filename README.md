![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest)
![Playwright](https://img.shields.io/badge/Playwright-Web%20Automation-2EAD33?logo=microsoft-playwright&logoColor=white)
![Status](https://img.shields.io/badge/status-active-success)

---

## Saucedemo Playwright MCP – QA Automation Suite

End‑to‑end UI test suite for the Saucedemo demo shop, built with **Python**, **Pytest**, and **Playwright**.  
This project is designed as a **portfolio‑ready example** of modern QA automation, showcasing:

- **Page Object Model (POM)** and clean test design
- **Cross‑browser Playwright UI automation**
- **AI‑assisted test development** using **Cursor AI** and **MCP**
- Clear, repeatable setup and execution via `pytest`

> Goal: demonstrate how to design maintainable, expressive E2E tests that a QA engineer can confidently present in interviews or portfolios.

---

## Tech Stack

- **Language**: Python 3.10+
- **Test runner**: Pytest
- **UI automation**: Playwright (sync API)
- **Design pattern**: Page Object Model
- **Editor / AI**: Cursor AI with MCP tools

---

## Key Features

- **Login flows**
  - Successful login
  - Invalid credentials and locked‑user error handling

- **Inventory & cart**
  - Product listing visibility and counts
  - Add to cart / remove from cart
  - Cart badge count assertions

- **Checkout (end‑to‑end)**
  - Happy path: login → add to cart → checkout → order success page
  - Negative paths with UI validation:
    - Missing First Name
    - Missing Zip / Postal Code
  - Back navigation from checkout overview

- **AI‑assisted test development**
  - Locators and flows aligned with the live Saucedemo app using Cursor AI
  - AI‑generated tests for:
    - Cart badge behavior
    - Checkout validation scenarios
  - Iterative failure analysis using Playwright traces + AI suggestions

---

## Project Structure

```text
.
├─ pages/                  # Page Object classes
│  ├─ base_page.py         # Shared helpers (navigation, waits)
│  ├─ login_page.py        # Login screen locators & actions
│  ├─ inventory_page.py    # Product listing & cart badge helpers
│  ├─ cart_page.py         # Cart view & checkout entry
│  └─ checkout_page.py     # Multi‑step checkout & validations
│
├─ tests/
│  ├─ login/               # Login scenarios
│  ├─ inventory/           # Inventory & listing checks
│  ├─ cart/                # Cart and badge behavior
│  └─ checkout/            # End‑to‑end checkout (happy + negative)
│
├─ data/
│  ├─ users.py             # Test users and base URL
│  ├─ products.py          # Product names for assertions
│  └─ constants.py         # Shared selectors
│
├─ config/
│  └─ settings.py          # Base URL, timeouts
└─ README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-account>/saucedemo-playwright-mcp.git
cd saucedemo-playwright-mcp
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
# source .venv/bin/activate   # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt  # if present
```

If a `requirements.txt` is not present yet, install directly:

```bash
pip install pytest playwright
```

Then install the Playwright browsers:

```bash
playwright install
```

---

## Running the Tests

### Run the full suite

```bash
python -m pytest
```

### Run a specific area

- **Checkout E2E flows**:

```bash
python -m pytest tests/checkout/test_checkout_flow.py
```

- **Cart behavior (add/remove, badge)**:

```bash
python -m pytest tests/cart
```

- **Login tests**:

```bash
python -m pytest tests/login
```

Pytest output shows which scenarios pass/fail and how long each set of tests takes.

---

## Notable Test Scenarios

### Happy Path Checkout

- Login as a standard user
- Add a product from the inventory page
- Open the cart and start checkout
- Fill out shipping details
- Continue to overview, finish checkout
- Assert “Thank you” confirmation header appears

### Validation Errors

- **Missing First Name**: leave first name empty, submit, assert the “First Name is required” error.
- **Missing Zip Code**: leave postal code empty, submit, assert the “Postal Code is required” error.
- **Back navigation**: from checkout overview, use `Cancel` to navigate back to the inventory page and assert URL/state.

These are implemented using the `CheckoutPage` methods to keep tests focused on behavior rather than low‑level locators.

---

## AI & MCP Workflow (Cursor)

This project intentionally demonstrates **modern AI‑augmented QA workflows**:

- **Cursor AI** is used as a coding copilot:
  - Generating initial Page Objects and tests
  - Proposing locators based on Saucedemo’s `data-test` attributes
  - Refactoring flows and extracting shared helpers for readability
- **MCP (Model Context Protocol)**:
  - Lets Cursor understand the full project structure (pages, tests, config)
  - Enables context‑aware edits (e.g., updating a locator in one page and all tests that rely on it)

This mirrors how a QA engineer can realistically **pair with an AI assistant** to:

- Bootstrap a new automation suite rapidly
- Iterate on flaky tests and locator issues
- Keep documentation and tests in sync with the application under test

---

## Modern Automation Practices Demonstrated

- **Page Object Model** for maintainable locators and actions
- **Data‑driven tests** using shared data modules (users, products, constants)
- **Stable selectors** using `data-test` attributes where available
- **Explicit waits** via Playwright’s locator APIs instead of arbitrary sleeps
- **Separation of concerns**:
  - Pages encapsulate behavior
  - Tests describe scenarios and assertions
- **Incremental coverage**:
  - Start from login and cart
  - Extend into checkout happy path
  - Add negative/validation flows

---

## How to Talk About This Project in Interviews

- Highlight that you:
  - Designed a **POM‑based Playwright test suite** against a public demo app.
  - Covered both **happy path** and **validation/error scenarios** for checkout.
  - Used **AI (Cursor + MCP)** as a force‑multiplier:
    - To quickly prototype tests and then refine them manually.
    - To troubleshoot flaky locators and align them with the live app.
  - Followed **best practices** for waits, selectors, and structure.

You can link this repository directly in your portfolio or CV as a **concrete example** of your end‑to‑end UI test automation skills.

---

## License

MIT – feel free to fork and adapt for your own learning or portfolio. 

