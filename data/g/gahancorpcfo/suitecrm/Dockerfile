FROM nimmis/alpine-apache-php7
RUN apk update
RUN apk add wget unzip
RUN wget https://suitecrm.com/files/160/SuiteCRM-7.10.4/276/SuiteCRM-7.10.4.zip -O /tmp/SuiteCRM-7.10.4.zip
WORKDIR /tmp
RUN unzip /tmp/SuiteCRM-7.10.4.zip
RUN apk add php7-session php7-xml php7-mbstring php7-zip php7-mysqli php7-ctype
ADD php.ini /etc/php7/php.ini
