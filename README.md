# Django Telegram Alert System with Celery

This project is a Django-based backend application that demonstrates how to:

- Expose public and protected API endpoints
- Send Telegram alerts from Django views
- Use Celery + Redis for asynchronous background task processing
- Manage sensitive environment variables with `.env`


# Features

## Public and Protected API Endpoints

- `GET /api/public/`  
  -> Public endpoint, no authentication required

- `GET /api/protected/`  
  -> Requires Token Authentication

## Telegram Bot Integration

- Sends a Telegram message when the public API is accessed.
- Bot details (Token and Chat ID) are securely loaded via `.env`.

## Asynchronous Task Execution with Celery

- Tasks are executed in the background using Celery.
- Redis (via Docker) is used as a message broker.


# Tech Stack

- **Python 3.12**
- **Django 5.2**
- **Django REST Framework**
- **Celery 5.5**
- **Redis (Docker)**
- **Telegram Bot API**
- **Render.com** (Optional Deployment Target)

# Setup Instructions

## 1. Clone the Repo
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

## 2. Create Virtual Environment
```bash
python -m venv env
.\env\Scriptsactivate
```

## 3. Install Requirements
```bash
pip install -r requirements.txt
```

## 4. Set Up `.env`
Create a file named `.env` inside the `backend_project/backend_project/` folder:
```
DEBUG=False
SECRET_KEY=your-very-secret-key
TELEGRAM_TOKEN=your-telegram-bot-token
TELEGRAM_CHAT_ID=your-telegram-chat-id
```

## 5. Run Redis (via Docker)
```bash
docker run -d -p 6379:6379 --name redis-server redis
```

## 6. Run Django Server
```bash
python manage.py runserver
```

## 7. Start Celery Worker
```bash
celery -A backend_project.backend_project worker --loglevel=info --pool=solo
```

# Sample API Response

**Public Endpoint**  
`GET /api/public/`

```json
{
  "message": "This is a public endpoint. No login needed."
}
```

Triggers Telegram alert:  
>  Someone accessed the public view!

---

# Directory Structure 
```
/backend_project/
  ├── backend_project/
  │   ├── __init__.py
  │   ├── settings.py
  │   ├── .env.example
  │   ├── celery.py
  │   ├── settings.py
  │   ├── urls.py
  │   ├── wsgi.py
  ├── core/
  │   ├── views.py
  │   ├── tasks.py
  │   ├── __init__.py
  │   ├── apps.py
  │   ├── models.py
  │   ├── telegram_utils.py
  │   ├── urls.py
  │   ├── telegram_utils.py
  ├── .env
  ├── manage.py
```


# License

This project is built for educational purposes and demonstration of Django + Celery + Telegram integrations.
