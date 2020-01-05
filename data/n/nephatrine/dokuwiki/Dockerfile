FROM nephatrine/base-php7:latest
LABEL maintainer="Daniel Wolf <nephatrine@gmail.com>"

RUN echo "====== UPDATE PACKAGES ======" \
 && apk --update upgrade \
 \
 && echo "====== SYSTEM CONFIGURATION ======" \
 && sed -i 's/index.php/doku.php index.php/g' /etc/nginx/nginx.conf \
 \
 && echo "====== CLEANUP ======" \
 && rm -rf /tmp/* /var/cache/apk/*

COPY override /