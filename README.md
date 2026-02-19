# 📍 Geo App

A full-stack location tracking iOS app built with **Swift (UIKit)** on the frontend and **Node.js + MongoDB** on the backend.

Track your real-time location, drop pins on a map, and have them persist across sessions — like a personal GPS logbook.

---

## 📸 Screenshots

| Compass View | Map View |
|---|---|
| ![Compass](images/screenshot_1.png) | ![Map](images/screenshot_2.png) |

---

## 🧱 Project Structure

```
Swift/
├── geo-app/             # iOS App (Swift / UIKit)
│   └── compass/
│       ├── AppDelegate.swift
│       ├── CompassViewController.swift
│       ├── MapViewController.swift
│       ├── LocationDelegate.swift
│       └── Models/
│           ├── Pin.swift
│           ├── Pinresponse.swift
│           └── Location.swift
│
├── geo-app-backend/     # Node.js REST API
│   ├── server.js
│   ├── config/db.js
│   ├── routes/
│   │   ├── pins.js
│   │   └── user.js
│   ├── controllers/
│   │   ├── pins.js
│   │   └── user.js
│   └── models/
│       ├── Pins.js
│       └── User.js
│
└── documentation.md     # Full technical documentation
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| iOS App | Swift, UIKit, CoreLocation, MapKit |
| Backend | Node.js, Express.js |
| Database | MongoDB |
| API Style | RESTful JSON API |

---

## 🚀 Getting Started

### Prerequisites

- **macOS** with Xcode installed
- **Node.js** (v16+) and npm
- **MongoDB** (via Homebrew)

---

### 1️⃣ Start the Backend

```bash
# Start MongoDB
brew services start mongodb-community

# Navigate to backend folder
cd geo-app-backend

# Install dependencies
npm install

# Start the development server
npm run dev
```

> ✅ You should see: `Server running in development mode on port 3000`

---

### 2️⃣ Run the iOS App

1. Open `geo-app/compass/Compass.xcodeproj` in **Xcode**
2. Select a Simulator (e.g. iPhone 16) from the toolbar
3. Press the **▶ Play** button to build and run

---

### 3️⃣ Test It

In the iOS Simulator:
- Go to **Features → Location → City Run** to simulate movement
- Watch your backend terminal — live location updates will appear in real time
- Tap anywhere on the map to drop a persistent pin

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/pins` | Fetch all saved pins |
| `POST` | `/api/v1/pins` | Add a new pin |
| `PUT` | `/api/v1/user` | Update user's live location |

---

## 🗺️ How It Works

```
📱 Tap on Map
    ↓
POST /api/v1/pins  →  routes/pins.js  →  controllers/pins.js  →  MongoDB
    ↑
✅ Pin saved & persists across sessions

🚶 You Move (GPS Update)
    ↓
PUT /api/v1/user   →  routes/user.js  →  controllers/user.js  →  MongoDB
    ↑
✅ Live location updated in real time
```

---

## 📄 Documentation

See [`documentation.md`](./documentation.md) for a full plain-English and technical breakdown of every file in the project.

---

## 👨‍💻 Author

**Priyadharsan** — [GitHub](https://github.com/PRIYADHARSANK)
