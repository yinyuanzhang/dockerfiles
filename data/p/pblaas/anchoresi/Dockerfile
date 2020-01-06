FROM python:2.7-alpine3.8

label maintainer="patrick@kite4fun.nl"

# The Following three Anchore platform environment variables should be provided.
ENV USERNAME admin
ENV PASSWORD password
# https://your.anchore.api.host  # Do not add /v1
ENV URL https://127.0.0.1

RUN pip install flask Flask-Caching && mkdir /app

COPY /app/ /app/
WORKDIR /app

EXPOSE 5000

CMD ["python", "app.py"]

