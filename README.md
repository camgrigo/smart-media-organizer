# smart-media-organizer
Lightweight AI-powered media manager for photos and videos. Organizes files with auto-tagging, metadata, and search via FastAPI + React

## Goals
- Organize photos with metadata + AI tags
- Search by filename, date, or AI-generated tags
- Simple web UI (React + Tailwind)

## Stack
- Backend: FastAPI + SQLite
- AI Tagging: Hugging Face (BLIP/CLIP)
- Frontend: React
- Version Control: GitHub

## Getting Started
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
