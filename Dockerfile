FROM python:3.11.6-slim

ENV PYTHONPATH="src/"

# Update the system and install packages
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install pipenv

# Install project dependencies
COPY Pipfile Pipfile.lock ./
RUN pipenv sync --dev --system

# Create and set the working directory
WORKDIR /app/
COPY . .

ENTRYPOINT [ "gunicorn" ]
CMD ["--workers=2", "config.wsgi:application", "--bind=0.0.0.0:8000"]
