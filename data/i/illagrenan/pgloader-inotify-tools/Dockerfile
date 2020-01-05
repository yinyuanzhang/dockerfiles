FROM dimitri/pgloader:latest
LABEL authors="Vašek Dohnal <vaclav.dohnal@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    inotify-tools \
    && rm -rf /var/lib/apt/lists/*
