FROM aesopagency/base:ubuntu-14.04

MAINTAINER Aesop Agency <technical@aesopagency.com>

ENV DEBIAN_FRONTEND noninteractive

# Install PHP-CLI using APT
RUN apt-get update -y && \
    apt-get install php5-cli -y

# Container entry point is PHP, default command is --help
ENTRYPOINT ["php"]
CMD ["--help"]
