#Dockerfile for web server app installation
FROM python:3.6-alpine

RUN pip install tornado

ADD web-server.py /web-server.py

EXPOSE 8080

CMD ["python", "/web-server.py"]
