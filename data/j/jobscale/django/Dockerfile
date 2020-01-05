FROM python:3.7-buster
SHELL ["bash", "-c"]
WORKDIR /root
COPY . django
RUN pip install -e django
EXPOSE 80
CMD ["python", "django/tests/web/manage.py", "runserver", "0.0.0.0:80"]
