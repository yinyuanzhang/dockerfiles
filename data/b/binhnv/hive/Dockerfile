FROM binhnv/hadoop:2.7.3
LABEL maintainer="Binh Van Nguyen<binhnv80@gmail.com>"

ENV HIVE_VERSION="1.2.1" \
    HIVE_SERVER2_THRIFT_PORT=10000 \
    HIVE_ENABLE_ZOOKEEPER_DISCOVERY="false" \
    HIVE_USER="hive" \
    HIVE_HOME="${MY_APP_DIR}/hive" \
    HIVE_LOG_DIR="${MY_APP_LOG_DIR}/hive" \
    HIVE_MS_DB_HOST="mysql" \
    HIVE_MS_DB_PORT="3306" \
    HIVE_MS_DB_USERNAME="root" \
    HIVE_MS_DB_PASSWORD="root" \
    HIVE_MS_DB="hive_metastore" \
    HIVE_MS_DRIVER_NAME="com.mysql.jdbc.Driver" \
    MYSQL_CONNECTOR_JAR="/usr/share/java/mysql-connector-java.jar"

ENV PATH="${PATH}:${HIVE_HOME}/bin" \
    HADOOP_HOME="${HADOOP_COMMON_HOME}" \
    HIVE_CONF_DIR="${HIVE_HOME}/conf"

WORKDIR ${HIVE_HOME}
COPY files/share/scripts/build /my_build
RUN chmod +x /my_build/install.sh && \
    /my_build/install.sh && \
    rm -rf /my_build


COPY files/share/services ${MY_SERVICE_DIR}/
COPY files/share/templates ${MY_TEMPLATE_DIR}/

COPY files/share/scripts/tools/ ${MY_TOOL_DIR}/