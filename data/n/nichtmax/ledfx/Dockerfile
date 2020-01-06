### build image
FROM python:3.7 as builder
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
   portaudio19-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /wheels

RUN pip install ledfx \
   && pip wheel ledfx

#####
FROM python:3.7-slim as application
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
   alsa-tools \
   portaudio19-dev \
 && rm -rf /var/lib/apt/lists/*

COPY --from=builder /wheels /wheels
RUN pip install ledfx pyaudio \
                       -f /wheels \
        && rm -rf /wheels \
        && rm -rf /root/.cache/pip/*

RUN useradd --base-dir /app --no-log-init -r -g audio ledfx

COPY config.yaml /app/
COPY entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh

ENV CARD 0

EXPOSE 8888/tcp

CMD ["/app/entrypoint.sh"]

