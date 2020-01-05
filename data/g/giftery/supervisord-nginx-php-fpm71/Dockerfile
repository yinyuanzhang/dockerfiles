# rebuild: 2019011401
FROM giftery/supervisord-nginx-php-fpm71:latest
MAINTAINER Evgenii Tereshkov <e.tereshkov@southbridge.ru>

# Устанавливаем дополнительные пакеты для работы приложения:
# - poppler-utils содержит pdftotext
RUN yum -y install poppler-utils && \
    yum clean all
