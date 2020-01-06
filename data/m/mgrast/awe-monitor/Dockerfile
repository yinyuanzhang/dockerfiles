
# docker build -t mgrast/awe-monitor .


FROM httpd:2.4-alpine

RUN apk update ; apk add \
	perl-cgi \
	perl-json \
	perl-libwww


# www
COPY www/ /usr/local/apache2/htdocs/

# config
COPY httpd.conf /usr/local/apache2/conf

# cgi
COPY ./cgi-bin/authclient.cgi /usr/local/apache2/cgi-bin/

# lib
COPY ./lib/AuthConfig.pm /usr/local/lib/perl5/site_perl/

