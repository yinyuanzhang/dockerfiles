FROM python:3.6-alpine

RUN pip install flask

COPY . /opt/

EXPOSE 8080

WORKDIR /opt

ENV APP=pay

ENTRYPOINT ["python", "app.py"]
