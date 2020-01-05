FROM python:3.6-alpine

ENV FLASK_APP flask_app.py
ENV FLASK_CONFIG production

RUN apk add build-base

RUN adduser -D dixon
USER dixon

WORKDIR /home/dixon

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY flask_app.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]