FROM homeassistant/home-assistant

RUN apt-get update && apt-get install -y git

CMD [ "python", "-m", "homeassistant", "--config", "/config" ]
