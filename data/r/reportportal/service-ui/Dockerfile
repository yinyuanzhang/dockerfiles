FROM alpine:3.10

LABEL maintainer="Andrei Varabyeu <andrei_varabyeu@epam.com>"
LABEL version=5.0.0-RC-6

ENV APP_DOWNLOAD_URL https://dl.bintray.com/epam/reportportal/5.0.0-RC-6

ADD ${APP_DOWNLOAD_URL}/service-ui_linux_amd64 /service-ui
ADD ${APP_DOWNLOAD_URL}/ui.tar.gz /

RUN mkdir /public
RUN chmod +x /service-ui
RUN tar -zxvf ui.tar.gz -C /public && rm -f ui.tar.gz

ENV RP_STATICS_PATH=/public


EXPOSE 8080
ENTRYPOINT ["/service-ui"]