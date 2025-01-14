FROM python:3.12-slim

WORKDIR /app

# Correctly reference the path to requirements.txt in the app/ folder
COPY ./app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy all files from app/ folder to the container
COPY ./app/ .

CMD ["python", "app.py"]
