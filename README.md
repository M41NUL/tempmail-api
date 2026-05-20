# TempMail

![Live](https://img.shields.io/badge/Live-Online-brightgreen?style=flat-square)
![HTML](https://img.shields.io/badge/HTML-5-orange?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-3-blue?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

A fast, clean, and mobile-friendly disposable email web app. Get a temporary email address instantly — no signup required.

**Live Demo:** [10secmail.unaux.com](https://10secmail.unaux.com)

---

## Features

- Instant disposable email address generation
- Auto inbox refresh every 10 seconds with countdown timer
- OTP auto-detection with one-tap copy button
- HTML and plain text email rendering
- Swipe down to close mail (mobile gesture)
- Unread count shown in browser tab title
- Address history saved locally
- Clean dark UI, fully responsive

---

## Project Structure

```
tempmail/
├── frontend/       # HTML, CSS, JS web interface
└── backend/        # API server (Node.js)
```

---

## Frontend

Built with pure HTML, CSS, and vanilla JavaScript. No frameworks or build tools required.

| File | Description |
|------|-------------|
| `index.html` | Main app — all UI and logic in one file |

### Run Locally

Just open `index.html` in any browser. No build step needed.

---

## Backend

REST API that handles temporary email generation and inbox fetching.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate` | GET | Generate a new temp email address |
| `/inbox/:email` | GET | Fetch inbox messages |
| `/delete/:email` | DELETE | Delete email session |

### Run Locally

```bash
cd backend
npm install
npm start
```

---

## Tech Stack

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Vercel](https://img.shields.io/badge/API-Vercel-black?style=flat-square&logo=vercel&logoColor=white)

---

## Contact

[![Telegram](https://img.shields.io/badge/Telegram-@mdmainulislaminfo-2CA5E0?style=flat-square&logo=telegram&logoColor=white)](https://t.me/mdmainulislaminfo)
[![GitHub](https://img.shields.io/badge/GitHub-M41NUL-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/M41NUL)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-+8801308850528-25D366?style=flat-square&logo=whatsapp&logoColor=white)](https://wa.me/8801308850528)

---

## License

This project is licensed under the [MIT License](LICENSE).
