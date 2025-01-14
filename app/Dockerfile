FROM python:3.12-slim  # Start with a lightweight Python 3.12 image.

WORKDIR /app  # Set working directory in the container.

COPY requirements.txt requirements.txt  # Copy dependencies file.
RUN pip install -r requirements.txt  # Install dependencies.

COPY . .  # Copy all files to the container.

CMD ["python", "app.py"]  # Run the app.

