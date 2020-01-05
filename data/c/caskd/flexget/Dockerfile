FROM pypy:3

VOLUME /config

RUN pip install -U flexget transmissionrpc python-telegram-bot

ENTRYPOINT ["flexget", "-c", "/config/config.yml", "daemon", "start"]
