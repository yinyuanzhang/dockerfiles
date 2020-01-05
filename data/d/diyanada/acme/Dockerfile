FROM busybox
MAINTAINER Chris <c@crccheck.com>

ADD index.html /www/index.html
ADD challenges /www/.well-known/acme-challenge

EXPOSE 8000

# Create a basic webserver and run it until the container is stopped 
CMD trap "exit 0;" TERM INT; httpd -p 8000 -h /www -f & wait
