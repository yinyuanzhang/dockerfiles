ARG ARCH=amd64
ARG ALPINE_VERSION=3.8
FROM $ARCH/alpine:$ALPINE_VERSION

ARG BUILD_DATE
ARG VCS_URL
ARG VCS_REF
LABEL org.label-schema.schema-version=1.0
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url=$VCS_URL
LABEL maintainer="Andreas Treichel <gmblar+github@gmail.com>"

ARG APACHE_VERSION=2.4
EXPOSE 80/tcp
ENV APPLICATION_ENV=production
ENV APACHE_SERVER_ADMIN=webmaster@example.com
ENV APACHE_SERVER_NAME=0.0.0.0:80
COPY src /
RUN apache-setup
WORKDIR /var/www/html
HEALTHCHECK CMD apache-healthcheck
ENTRYPOINT ["apache-entrypoint"]
CMD ["apache-foreground"]
