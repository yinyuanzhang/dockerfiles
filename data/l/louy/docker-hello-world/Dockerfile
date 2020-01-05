FROM busybox
MAINTAINER Chris <c@crccheck.com>

ADD index.html /www/index.html
ADD health-check /www/health-check

EXPOSE 8080

# Create a basic webserver and sleep forever
CMD httpd -p 8080 -h /www; tail -f /dev/null

