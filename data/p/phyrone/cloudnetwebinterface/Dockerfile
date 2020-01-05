FROM nginx
MAINTAINER Phyrone(phyrone@phyrone.de)
ENV FILENAME WebInterface-0.11.0.12.11.2018.19.05-RELEASE.zip
RUN apt update -y && apt install curl unzip -y
RUN curl https://update.madfix.me/projects/MaterialDesignWebInterface/files/WEB/$FILENAME -O
RUN unzip $FILENAME -d /build/
RUN cp -R /build/dist/web/* /usr/share/nginx/html/
RUN ls /usr/share/nginx/html/
RUN rm -R /build/ && apt clean
EXPOSE 80
VOLUME /usr/share/nginx/html/
