#Based on Dockerfile by Olivier Dossmann, <olivier+dockerfile@dossmann.net>

FROM python:3.3-alpine
MAINTAINER Michał Jaskólski, <michal@jaskolski.online>

RUN apk add --no-cache build-base libffi libffi-dev
# Create directory to contains all Isso config + DB
RUN mkdir -p /opt/isso

# Install isso
RUN pip install isso==0.9.10 gevent==1.1rc3 gunicorn

RUN apk del --purge build-base libffi-dev

# Add isso configuration
ADD isso.conf /opt/isso/isso.conf

VOLUME ["/opt/issodb", "/opt/isso"]

# Let some ports to be accessible if user add -p option to docker run
EXPOSE 8080

ENV ISSO_SETTINGS /opt/isso/isso.conf
# Launch supervisord at the beginning
CMD ["-k", "gevent", "-b", "0.0.0.0:8080", "-w", "4", "--preload", "isso.run"]
ENTRYPOINT ["/usr/local/bin/gunicorn"]
