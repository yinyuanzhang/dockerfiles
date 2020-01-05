FROM r-base

RUN apt-get update \
    && apt-get install -y libcurl4-openssl-dev libmagick++-dev
COPY _bootstrap.r /
RUN R -f _bootstrap.r