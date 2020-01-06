FROM ubuntu:16.04

RUN apt update && apt install -y wget
COPY installR.sh .

RUN chmod +x installR.sh && ./installR.sh && mkdir /root/RHome
ENV RSTUDIO_WHICH_R /usr/bin/R
ENV QT_XKB_CONFIG_ROOT /usr/share/X11/xkb

CMD [ "rstudio" ]