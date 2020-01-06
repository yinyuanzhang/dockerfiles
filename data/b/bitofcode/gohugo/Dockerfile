FROM debian:10-slim

ENV HUGO_USER "hugo"
ENV HUGO_VERSION "0.59.1"

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y curl git && \
  curl -LO https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.deb && \
  dpkg -i hugo_extended_${HUGO_VERSION}_Linux-64bit.deb && \
  rm hugo_extended_${HUGO_VERSION}_Linux-64bit.deb && \
  useradd --create-home --home-dir /home/${HUGO_USER} --shell /bin/bash ${HUGO_USER}

USER ${HUGO_USER}
WORKDIR /home/${HUGO_USER}

CMD ["/bin/bash"]
