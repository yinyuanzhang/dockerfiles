FROM ubuntu:18.04

LABEL maintainer="asn1parse@gmail.com"

RUN apt update && apt install -y git && rm -rf /var/lib/apt/lists/*

RUN git clone --depth=1 https://github.com/speed47/spectre-meltdown-checker.git && rm -rf /spectre-meltdown-checker/.git

FROM ubuntu:18.04

RUN apt update && apt install -y dnsutils bsdmainutils && rm -rf /var/lib/apt/lists/*

RUN mkdir /spectre-meltdown-checker

COPY --from=0 /spectre-meltdown-checker /spectre-meltdown-checker

ENTRYPOINT ["/spectre-meltdown-checker/spectre-meltdown-checker.sh"]
