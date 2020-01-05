FROM python:3.7-slim-stretch
LABEL maintainer="Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pingparsing==0.18.1

ENTRYPOINT ["pingparsing"]
CMD ["-h"]
