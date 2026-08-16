# NextStep_School

School Platform — навчальна pet‑платформа для відпрацювання навичок веб‑розробки.

This repository contains a Django-based learning platform where users can register, browse and manage courses, follow lessons, and complete tasks. The project is organized as a Django project with several apps:

- `auth_system` — authentication and user management
- `home_app` — landing and informational pages
- `course_and_module_app` — courses and modules management
- `lessons_app` — lesson content and viewing
- `tasksmarks_app` — tasks, submissions and marks

Шаблони і медіа-файли знаходяться в папках `templates/` та `media/`.

---

## Quick start / Як запустити локально

Prerequisites / Необхідне ПО

- Python 3.9+ (recommended)
- pip
- virtualenv (optional but recommended)
- (optional) PostgreSQL or another database for production

1. Clone the repository

```bash
git clone https://github.com/NazarKarpa/NextStep_School.git
cd NextStep_School
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
# on macOS / Linux
source .venv/bin/activate
# on Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. Install Python dependencies

If there is a `requirements.txt` in the repo root, install it:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt`, install Django and commonly used packages manually:

```bash
pip install Django
```

4. Configure environment variables

Create a `.env` file (or set environment variables) with at least:

- `SECRET_KEY` — Django secret key
- `DEBUG` — `True` for local development
- `DATABASE_URL` or database settings in `settings.py` (SQLite works out of the box)

5. Apply migrations and collect static files

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

6. Create an admin/superuser

```bash
python manage.py createsuperuser
```

7. Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

---

Notes / Поради

- If you use SQLite (default), no extra DB setup is required. For production use PostgreSQL or another robust DB and set `DATABASES` accordingly.
- Static and media files: ensure `MEDIA_ROOT` and `STATIC_ROOT` are configured when serving in production.
- If you want Docker support, create a `Dockerfile` and `docker-compose.yml` and I can help scaffold them.

Contributing

Contributions are welcome — open issues or pull requests with improvements, bug fixes, or documentation updates.

License

Specify a license (e.g., MIT) by adding a `LICENSE` file if you want to make this project open source.
