FROM python:alpine

WORKDIR /pyapp
COPY . /pyapp

RUN pip install --trusted-host pypi.python.org Flask Redis

EXPOSE 80

CMD ["python", "main.py"]
