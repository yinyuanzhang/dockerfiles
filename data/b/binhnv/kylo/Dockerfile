FROM binhnv/nifi:1.5.0
LABEL maintainer="Binh Van Nguyen<binhnv80@gmail.com>"

ENV KYLO_VERSION=0.9.0.2 \
    KYLO_HOME="${MY_APP_DIR}/kylo" \
    KYLO_LOG_DIR=${MY_APP_LOG_DIR}/kylo \
    KYLO_START_SERVICES="" \
    KYLO_CREATE_ES_INDEXES="false"

WORKDIR ${KYLO_HOME}
COPY files/share/scripts/build /my_build
RUN chmod +x /my_build/install.sh && \
    /my_build/install.sh && \
    rm -rf /my_build


COPY files/share/services ${MY_SERVICE_DIR}/
COPY files/share/templates ${MY_TEMPLATE_DIR}/
COPY files/share/scripts/init ${MY_INIT_DIR}/

COPY files/share/scripts/tools/ ${MY_TOOL_DIR}/