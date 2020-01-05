# useable with openhab2 to add custom configuration
FROM openhab/openhab:amd64-online

ENV CONF_DIR ${APPDIR}/conf

COPY ./html ${CONF_DIR}
COPY ./icons ${CONF_DIR}
COPY ./items ${CONF_DIR}
COPY ./persistence ${CONF_DIR}
COPY ./rules ${CONF_DIR}
COPY ./scripts ${CONF_DIR}
COPY ./services ${CONF_DIR}
COPY ./sitemaps ${CONF_DIR}
COPY ./things ${CONF_DIR}
COPY ./transform ${CONF_DIR}