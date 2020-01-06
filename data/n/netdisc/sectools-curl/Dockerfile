FROM ubuntu:18.04

LABEL maintainer="asn1parse@gmail.com"

RUN apt-get update && apt-get install -y curl

ENTRYPOINT ["/usr/bin/curl"]

CMD ["--help"]
