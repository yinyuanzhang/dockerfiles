FROM resin/armv7hf-debian

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install python-cheetah wget && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/midgetspy/Sick-Beard/tarball/master -O sickbeard.tar.gz && tar -xzvf sickbeard.tar.gz && mv midgetspy-Sick-Beard-* SickBeard

VOLUME /data
VOLUME /config

EXPOSE 8081

RUN [ "cross-build-end"]
CMD python /SickBeard/SickBeard.py --datadir /config/data --config /config/config.ini -p 8081 --nolaunch
