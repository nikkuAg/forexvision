FROM python:3.10-slim

RUN apt-get update && apt-get install -y cron

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN python manage.py migrate

RUN python manage.py crontab add

WORKDIR /app/forex_vision

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
