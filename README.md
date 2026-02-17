# Selenium Login Automation Bot

An automation script that simulates human interaction with a web browser to bypass authentication screens and access protected data.

## 🤖 Features
* **Browser Automation:** Uses Selenium to control a real Chrome instance.
* **Form Interaction:** Automatically locates, fills, and submits login credentials.
* **Dynamic Content Handling:** Capable of interacting with elements that are rendered via JavaScript.
* **Automatic Driver Management:** Uses `webdriver-manager` to ensure the correct Chrome driver is always used.

## 🛠️ Tech Stack
* **Python 3.x**
* **Selenium:** For browser control and DOM interaction.
* **WebDriver Manager:** For automatic driver installation.

## 📦 Installation & Usage
1. Clone the repo.
2. Create a virtual environment: `python -m venv venv`.
3. Activate it: `.\venv\Scripts\activate` (Windows).
4. Install dependencies: `pip install -r requirements.txt`.
5. Run the bot: `python login_bot.py`.

## 💡 Engineering Concepts Applied
- **DOM Traversal:** Finding elements by ID and Name.
- **Event Simulation:** Simulating keystrokes (`send_keys`) and clicks.
- **Synchronization:** Managing script timing with `time.sleep` to ensure page loads before interaction.
