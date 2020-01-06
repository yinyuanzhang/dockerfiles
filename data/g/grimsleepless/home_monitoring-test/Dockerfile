from grimsleepless/home_monitoring-base:latest
MAINTAINER Jean-Francois Labonte <jeff.labonte12@gmail.com>

RUN apt install -y \
    python3-pip python3-flask

COPY requirements /application/requirements

COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

ENTRYPOINT ["test.sh"]
CMD ["python3", "-m", "unittest", "discover"]

COPY src /application
WORKDIR /application
