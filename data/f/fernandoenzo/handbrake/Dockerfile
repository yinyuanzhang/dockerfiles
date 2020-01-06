FROM ubuntu:18.04
MAINTAINER Fernando Enzo Guarini (fernandoenzo@gmail.com)

ENV DISPLAY :0

COPY scripts/basics /tmp
COPY static/handbrake-gtk_0.9.5-1~getdeb2~natty_amd64.deb /
COPY static/libgstreamer0.10-0_0.10.36-1.5_amd64.deb /
COPY static/libgstreamer-plugins-base0.10-0_0.10.36-2_amd64.deb /
COPY static/libnotify1_0.5.0-2ubuntu1_amd64.deb /
COPY static/presets /root/.ghb/
COPY static/preferences /root/.ghb/

RUN bash /tmp/basics

CMD ghb
