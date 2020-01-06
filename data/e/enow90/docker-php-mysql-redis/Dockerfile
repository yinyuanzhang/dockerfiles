FROM library/nginx
MAINTAINER Kenneth Peiruza <kenneth.peiruza@floss.cat>
RUN rm /usr/share/nginx/html/index.html
ADD web.tgz /usr/share/nginx/html/
COPY test /test
