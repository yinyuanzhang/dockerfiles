FROM python:3

RUN apt-get update && apt-get install -y \
    tzdata \
 && rm -rf /var/lib/apt/lists/*

ENV TZ=Europe/Zurich

COPY src ./
COPY dummy /tmp/

CMD [ "python", "./movie_filter.py" ]
