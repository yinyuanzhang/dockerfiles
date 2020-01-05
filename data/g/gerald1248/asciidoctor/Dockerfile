FROM asciidoctor/docker-asciidoctor:latest

LABEL maintainer="Gerald Schmidt <gerald1248@gmail.com>"
LABEL description="Asciidoctor with plugins, pandoc, jq and shUnit2"

RUN apk add jq ruby-rdoc
RUN wget https://github.com/jgm/pandoc/releases/download/2.5/pandoc-2.5-linux.tar.gz -O /tmp/pandoc.tar.gz && \
  tar xvzf /tmp/pandoc.tar.gz --strip-components 1 -C /usr/local/
RUN apk add jq
RUN wget https://raw.githubusercontent.com/kward/shunit2/master/shunit2 -O /usr/bin/shunit2
