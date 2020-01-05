FROM debian:testing-slim
MAINTAINER Fernando Enzo Guarini (fernandoenzo@gmail.com)

COPY scripts/ /tmp/scripts
COPY static/ /tmp/static

RUN bash /tmp/scripts/basics

ENV LANG es_ES.UTF-8
ENV TERM xterm-256color

ENTRYPOINT ["/usr/local/boot"]
CMD ["/bin/bash"]

