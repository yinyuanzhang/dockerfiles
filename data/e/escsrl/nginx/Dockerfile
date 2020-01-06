FROM nginx:alpine

ENV PHPFPM_HOST phpfpm
ENV PHPFPM_PORT 9000
ENV VIRTUAL_HOST _
ENV CLIENT_MAX_BODY_SIZE 10M
ENV FASTCGI_APP_ENV dev

VOLUME ["/app"]

ADD /resources/* /resources/
WORKDIR /resources

ENTRYPOINT ["/resources/entrypoint.sh"]

EXPOSE 80
