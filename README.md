# Fintesa – Backend Technical Test (Auth + RBAC)

Tech: Django, Django REST Framework, SimpleJWT, SQLite (dev)

## Quickstart
```bash
python -m venv .venv && . .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
