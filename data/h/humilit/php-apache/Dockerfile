FROM humilit/common-php:7.2.13
LABEL maintainer="robert.brendler+github@gmail.com"

ENV ALLOW_ROBOT_INDEXING false

EXPOSE 80

COPY content /
RUN php-apache-setup

ENTRYPOINT ["php-apache-entrypoint"]
CMD ["httpd"]
