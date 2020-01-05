FROM iestriana/lamp
MAINTAINER @algargon99

RUN apt-get -y update && apt-get install -y net-tools

ADD index.php /var/www/html
RUN rm /var/www/html/index.html
ADD script.sh /usr/bin
ADD carga.sql /usr/bin


RUN apt-get install -y git
WORKDIR /var/www/html/
RUN git clone https://github.com/algargon99/PROYECTO_IAW_GARCIA_GONZALEZ.git
RUN chown www-data:www-data /var/www/html/PROYECTO_IAW_GARCIA_GONZALEZ
WORKDIR /usr/bin
RUN chmod 775 /usr/bin/script.sh
CMD /usr/bin/script.sh
EXPOSE 80/tcp
EXPOSE 80/udp
