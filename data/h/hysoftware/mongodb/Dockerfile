FROM hysoftware/baseimage
MAINTAINER Hiroaki Yamamoto

RUN pacman -S --noconfirm mongodb mongodb-tools

RUN mkdir /db
VOLUME /db
VOLUME /var/log/mongodb
RUN chown mongodb:daemon /db
COPY mongodb.sh /bin
COPY mongodb.conf /etc
RUN chown root:root /bin/mongodb.sh
RUN chmod uog+rx /bin/mongodb.sh
EXPOSE 27017

ENTRYPOINT ["mongodb.sh"]
