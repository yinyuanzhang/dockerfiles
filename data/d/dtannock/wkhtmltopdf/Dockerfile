FROM ubuntu:16.04

ENV WKHTMLTOPDF_VERSION 0.12.4

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y \
        zlib1g \
        fontconfig \
        libfreetype6 \
        libssl-dev \
        libx11-dev \
        libxext-dev \
        libxrender-dev

COPY wkhtmltopdf /usr/bin

RUN chmod +x /usr/bin/wkhtmltopdf

ENTRYPOINT ["/usr/bin/wkhtmltopdf"]
CMD ["-h"]
