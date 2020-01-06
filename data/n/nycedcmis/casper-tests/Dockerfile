FROM nycedcmis/casperjs:latest
LABEL MAINTAINER alehman@edc.nyc

RUN apt-get update \
    && apt-get install -y parallel 

ENTRYPOINT ["parallel"]

CMD ["--help"]