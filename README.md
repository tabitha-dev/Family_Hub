<div align="center">
  <h1 align="center">🏡 Family Hub</h1>
  <p align="center">
    A simple, private, and local-first dashboard to organize your family's life.
    <br />
    <br />
    <a href="https://tabitha-dev.github.io/Family_Hub/"><strong>View Live Site »</strong></a>
    <br />
    <br />
    <a href="https://github.com/tabitha-dev/Family_Hub/issues">Report Bug</a>
    ·
    <a href="https://github.com/tabitha-dev/Family_Hub/issues">Request Feature</a>
  </p>
</div>

<p align="center">
  <a href="https://github.com/tabitha-dev/Family_Hub/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  </a>
  <a href="https://github.com/tabitha-dev/Family_Hub/issues">
    <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
  </a>
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#how-it-works">How It Works</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## About The Project



*To add your own screenshot: take a picture of your app, name it `family-hub-screenshot.png`, and upload it to the main directory of your repository.*

**Family Hub** is a single-page application designed to run entirely in your browser with no need for accounts or a backend server. It's a private, offline-first dashboard that helps you manage meal plans, grocery lists, chores, and calendar events for your entire family. The core philosophy is to provide a central organization tool without compromising on privacy.

---

## Key Features

* **✨ Privacy First:** All your data is saved securely in your browser's `localStorage`. Nothing is ever sent to a server.
* **🏡 Personalized Dashboard:** Get an at-a-glance view of today's upcoming meals, pending chores, and scheduled events.
* **📅 Interactive Planners:**
    * **Meal Planner:** Click and edit a weekly calendar to plan breakfasts, lunches, and dinners.
    * **Grocery List:** Add items, organize by category, and check them off as you shop.
    * **Chore Chart:** Create tasks, assign them to family members, and track their status.
    * **Event Calendar:** Manage appointments and birthdays with a full monthly view.
* **🎨 Fully Customizable:**
    * Add your own family members in the settings.
    * Choose between a sleek light or dark theme.
    * Import and export your data as a single file for backup or moving between computers.

---

## Built With

This project is built with vanilla web technologies, keeping it lightweight, fast, and easy to maintain.

<p align="left">
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML"><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"></a>
  <a href="https://tailwindcss.com/"><img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"></a>
</p>

---

## How It Works

The application operates without a backend server by leveraging the browser's **`localStorage`** API.

1.  **Initialization:** On the first visit, the app creates a default data structure in `localStorage`.
2.  **Data Persistence:** Every change you make adding a chore, editing a meal, etc.is instantly saved to `localStorage`.
3.  **Data Retrieval:** When you open or refresh the page, the app reads your saved data from `localStorage` and populates the interface.

This ensures your data is persistent on your device without compromising your privacy.

---

## 🏁 Getting Started

To get a local copy up and running, follow these simple steps.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/tabitha-dev/Family_Hub.git](https://github.com/tabitha-dev/Family_Hub.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Family_Hub
    ```
3.  **Open `index.html` in your browser:**
    You can simply double-click the `index.html` file or use a local server extension (like Live Server for VS Code).

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See the `LICENSE` file for more information.

---

## 📬 Contact

Tabitha - [@tabitha-dev](https://github.com/tabitha-dev)

Project Link: [https://github.com/tabitha-dev/Family_Hub](https://github.com/tabitha-dev/Family_Hub)
