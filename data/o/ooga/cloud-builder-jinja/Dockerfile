FROM python:3.7-alpine

RUN pip install Jinja2

COPY ./entrypoint.py /tmp/entrypoint.py

ENTRYPOINT ["python", "/tmp/entrypoint.py"]
