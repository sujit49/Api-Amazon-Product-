# 🤖 Selenium Web Automation Projects

This repository contains multiple Python-based web automation scripts using **Selenium WebDriver**. These projects simulate user interactions with real-world websites such as Amazon, Wikipedia, Cookie Clicker, and a signup form on Heroku. They're great examples of practical automation, bot behavior, and dynamic web scraping.

---

## 📂 Projects Included

### 1. 📝 `challenge.py` – Form Automation
- **Website**: [Heroku Secure Retreat](https://secure-retreat-92358.herokuapp.com/)
- **What it does**: Automatically fills out a signup form with first name, last name, and email, then submits the form.
- **Key Concepts**: `By.NAME`, `By.CSS_SELECTOR`, form handling, browser automation basics.

---

### 2. 🍪 `cookie.py` – Cookie Clicker Game Bot
- **Website**: [Cookie Clicker](http://orteil.dashnet.org/experiments/cookie/)
- **What it does**: Continuously clicks the cookie, buys upgrades every 5 seconds, and stops after 5 minutes showing your cookies/second.
- **Key Concepts**: Looping with `time`, parsing element text, clicking and buying upgrades dynamically.

---

### 3. 📚 `interaction.py` – Wikipedia Interaction Bot
- **Website**: [Wikipedia Main Page](https://en.wikipedia.org/wiki/Main_Page)
- **What it does**: Retrieves the number of articles on Wikipedia, finds the "Content portals" link, and performs a search for “Python”.
- **Key Concepts**: `By.LINK_TEXT`, `By.NAME`, using `Keys.ENTER` to simulate keyboard input.

---

### 4. 🛒 `main.py` – Amazon Product Page Interaction
- **Website**: [Amazon Product](https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/)
- **What it does**: Opens an Amazon product page, locates various elements like documentation links, event times, and bug report links.
- **Key Concepts**: `By.XPATH`, `By.CLASS_NAME`, `By.CSS_SELECTOR`, parsing multiple elements, web navigation.

---

## 🛠️ Tech Stack

- 🐍 Python 3.x
- 🌐 [Selenium](https://pypi.org/project/selenium/)
- 🌎 Chrome + ChromeDriver

---

## 🚀 Getting Started

> 💡 Ensure you have **Chrome** and **ChromeDriver** installed and ChromeDriver is added to your PATH.

### 1. Install Selenium
```bash
pip install selenium
