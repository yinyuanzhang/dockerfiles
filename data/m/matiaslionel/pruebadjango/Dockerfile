# Pull base image
FROM python:3

# Set environment varibles
#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir code code/projecto code/projecto/calculadora
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt 
#/&& django-admin startproject projectodjango ./projecto
COPY /volumen/ /code/