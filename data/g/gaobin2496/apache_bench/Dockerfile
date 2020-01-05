FROM  debian:jessie
MAINTAINER Bin Gao <gaobin2496@gmail.com>
RUN apt-get update && apt-get -y install apache2-utils && apt-get clean
ENTRYPOINT ["/usr/bin/ab"]
