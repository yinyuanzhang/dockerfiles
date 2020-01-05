FROM python:2-slim-stretch as build

WORKDIR /app
ADD https://github.com/AndrewX192/lenovo-sa120-fanspeed-utility/archive/master.zip .

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        unzip && \
    DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    unzip -j master.zip && \
    rm master.zip

FROM python:2-slim-stretch

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        sg3-utils && \
    DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=build /app/ /app/
