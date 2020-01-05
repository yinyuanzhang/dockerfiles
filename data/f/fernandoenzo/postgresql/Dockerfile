FROM fernandoenzo/debian:testing-min
MAINTAINER Fernando Enzo Guarini (fernandoenzo@gmail.com)

COPY scripts/basics /tmp
RUN bash /tmp/basics

COPY scripts/boot /usr/local/boot

EXPOSE 80/tcp
EXPOSE 5432/tcp

