#  University Finder

University Finder is a simple full-stack web application built to understand and practice **frontend–backend integration** using **FastAPI** and **JavaScript**.

The application allows users to search for universities by country (and optionally by university name). The frontend sends user input to a FastAPI backend, which then fetches real data from the **Hipolabs Universities API** and returns the results back to the UI.

---

##  How It Works

Frontend (HTML / CSS / JavaScript)

↓
FastAPI Backend (/universities?country=...)

↓
Hipolabs Universities API

↓
FastAPI (optional filtering)

↓
Frontend (display results)


- The **frontend** collects user input and makes HTTP requests using `fetch()`
- The **FastAPI backend** acts as an API layer and data handler
- The backend fetches data from the external Hipolabs API
- The response is returned as JSON and rendered dynamically on the frontend

---

## Purpose of This Project

This project was created **purely for learning**.

The main goal was to:
- Clearly understand **frontend ↔ backend communication**
- Learn how to design and consume REST APIs
- Practice handling query parameters, async requests, and JSON responses
- Understand CORS and real-world API integration
- Build confidence in full-stack development fundamentals

---

##  Project Structure

University_Search/

├── learn_fastapi/ # Learning folder (FastAPI basics and experiments)


├── app/

   ── main.py # FastAPI backend logic

├── frontend/

   ── index.html # Frontend UI
   
   ── script.js # Frontend logic (API calls, DOM updates)
   
   ── style.css # Basic styling
 
├── requirements.txt

├── .gitignore

└── README.md


- `learn_fastapi/` contains notes and small experiments done while learning FastAPI basics before starting the actual project.
- The **main project logic** lives inside `app/` and `frontend/`.

---

##  Styling & UI Status

Basic CSS styling is currently applied to keep the UI readable.

**UI cleanup, improved styling, and better layout organization are planned and will be added soon.**  
The current focus of the project is **functionality and integration**, not visual polish.

---

##  Future Improvements

- Improve UI layout and styling
- Better error handling and user feedback
- Input validation and autocomplete
- Deployment (backend + frontend)
- Pagination or result limiting

---

##  Tech Stack

- **Backend:** FastAPI, Python
- **Frontend:** HTML, CSS, JavaScript
- **External API:** Hipolabs Universities API

---

##  Note

This project represents my learning journey in full-stack development and frontend–backend integration. The emphasis is on **clarity, correctness, and understanding the flow of data**, rather than building a production-ready application.


