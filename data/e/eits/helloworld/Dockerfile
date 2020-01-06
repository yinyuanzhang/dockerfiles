FROM alpine:3.3
MAINTAINER Sorin Hornoiu  - LafargeHolcim // Thanks to Simen Huuse.
LABEL Sorin Hornoiu  - LafargeHolcim // Thanks to Simen Huuse.

run apk add --update darkhttpd && rm -rf /var/cache/apk/*

ADD index.html /var/www/localhost/htdocs/index.html
ADD entrypoint.sh /entrypoint.sh
ADD sapcloudplatform.png /var/www/localhost/htdocs/sapcloudplatform.png
ADD lh-picture.png /var/www/localhost/htdocs/lh-picture.png
ADD git.gif /var/www/localhost/htdocs/git.gif
ADD docker.jpg /var/www/localhost/htdocs/docker.jpg

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
