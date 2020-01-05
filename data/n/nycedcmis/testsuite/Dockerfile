FROM nycedcmis/casperjs:latest
LABEL maintainer.1="alehman@edc.nyc"
LABEL maintainer.2="aho@edc.nyc"

RUN apt-get update \
    && apt-get install -y parallel 

ENTRYPOINT ["parallel"]

CMD ["--help"]