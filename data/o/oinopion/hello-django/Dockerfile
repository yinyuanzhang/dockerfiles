FROM python:3.7-alpine
RUN apk add --no-cache tini

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000
ENTRYPOINT ["/sbin/tini", "--", "bin/server.sh"]
