FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE_URL=sqlite:///db.sqlite3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
RUN chmod +x build.sh && ./build.sh

EXPOSE 8000
CMD ["gunicorn", "SAManager.wsgi:application", "--bind", "0.0.0.0:8000"]
