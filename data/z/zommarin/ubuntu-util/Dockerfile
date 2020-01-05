#
# Ubuntu image with useful utilities
#

FROM ubuntu:18.04

MAINTAINER Anders Zommarin <anders@zommarin.se>

COPY install-tools.sh /install-tools.sh

RUN /install-tools.sh

COPY entrypoint.sh /bin/entrypoint.sh

ENTRYPOINT ["/bin/entrypoint.sh"]
