FROM python:3.7-alpine
RUN apk add --update tini
COPY app/ /app
WORKDIR /app

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["python3", "main.py"]

EXPOSE 45678