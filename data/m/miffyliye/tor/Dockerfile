FROM ubuntu:18.04
MAINTAINER Wang, Tao <i@miffyliye.org>

ENV TOR_PORT 9050

RUN apt-get update \
    && apt-get install -y tor

ADD ./docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh
RUN chmod a+x /usr/local/bin/docker_entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker_entrypoint.sh"]