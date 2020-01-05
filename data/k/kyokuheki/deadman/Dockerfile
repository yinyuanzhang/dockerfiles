FROM library/python:2-alpine
LABEL maintainer Kenzo Okuda <kyokuheki@gmail.com>
ENV LANG="en_US.UTF-8"

RUN set -eux -o pipefail \
 && apk --no-cache add openssh
RUN set -eux -o pipefail \
 && wget https://raw.githubusercontent.com/upa/deadman/master/deadman -O /deadman \
 && chmod +x /deadman

#COPY ./deadman.conf /
VOLUME ["/deadman.conf"]

CMD ["/deadman", "/deadman.conf"]
