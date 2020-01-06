FROM thompsnm/nodejs-chrome:carbon

RUN apt-get update && \
    apt-get install -y xvfb

COPY /entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
