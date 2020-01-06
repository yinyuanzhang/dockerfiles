FROM python:3.7-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /code
# System deps:
RUN apt-get update
RUN apt-get install openssl
RUN apt-get install -y\
    python3-numpy \
    python3-pandas \
    libssl-dev \
    libffi-dev \
    libblas-dev \
    liblapack-dev \
    libatlas-base-dev \
    gfortran \
    build-essential \
    postgresql-client \
    libpq-dev \
    tini\
    nginx\
    supervisor

# App deps
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt