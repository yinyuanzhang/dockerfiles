FROM debian
MAINTAINER benesis002@outlook.com

RUN apt-get update && apt-get install -y curl
RUN curl http://pqsoftware.eaton.com/install/linux/ipp/ipp-linux_1.66.161-1_amd64.deb -o ipp.deb
RUN dpkg -i ipp.deb
RUN rm ipp.deb

WORKDIR /usr/local/Eaton/IntelligentPowerProtector
EXPOSE 4679
EXPOSE 4680
CMD ["./mc2", "-start"]

HEALTHCHECK --interval=1m --timeout=3s \
  CMD curl -f http://localhost:4679 || exit 1
