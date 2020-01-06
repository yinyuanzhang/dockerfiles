FROM debian:buster

RUN apt-get update && apt-get install --no-install-recommends \
  build-essential python3-dev python3-pip libffi-dev \
  libpython-dev libssl-dev net-tools nmap iputils-ping \
  python3-setuptools -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME /config

RUN pip3 install wheel
RUN pip3 install aiohttp sqlalchemy

RUN pip3 install homeassistant==0.43.0

CMD [ "python3", "-m", "homeassistant", "--config", "/config" ]
