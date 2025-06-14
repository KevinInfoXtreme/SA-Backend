# SA-Backend

This project contains the backend for the "SA" application built with Django.

## Container Usage

1. **Build the image**

   ```bash
   docker build -t sa-backend .
   ```

2. **Run the container**

   ```bash
   docker run -p 8001:8001 sa-backend
   ```

The container exposes port `8000` and starts the application using `gunicorn SAManager.wsgi:application`.

## Deployment with Coolify

When deploying to Coolify, set the `DJANGO_ALLOWED_HOSTS` environment variable to a
comma-separated list of allowed domain names.
