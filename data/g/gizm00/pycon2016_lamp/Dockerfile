FROM linode/lamp
RUN apt-get update && apt-get install -y \ 
	wget \
	unzip
RUN echo "moo"
RUN wget https://github.com/gizm00/pycon2016_lamp/archive/master.zip
RUN unzip master.zip
RUN cp pycon2016_lamp-master/webfiles/* /var/www/example.com/public_html/
COPY mysql_setup.sql /
COPY lamp_startup.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/lamp_startup.sh
