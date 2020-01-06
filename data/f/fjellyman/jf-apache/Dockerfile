FROM coreos/apache

MAINTAINER Jordan Fjellman (jordan.fjellman@gmail.com)

COPY jordanfjellman.com.conf /etc/apache2/sites-available/

RUN apt-get update &&\
	apt-get install -y libapache2-mod-proxy-html libxml2-dev &&\
	a2enmod proxy proxy_http &&\
	a2ensite jordanfjellman.com.conf &&\
	service apache2 reload

EXPOSE 80

ENTRYPOINT ["/usr/sbin/apache2ctl"]

CMD ["-D", "FOREGROUND"]
