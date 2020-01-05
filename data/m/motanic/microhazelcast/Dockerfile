FROM airhacks/payara
MAINTAINER Adam Bien, adam-bien.com
# For more information about ping see: https://github.com/AdamBien/ping/
COPY ./target/micro-hazelcast.war ${DEPLOYMENT_DIR}
#HEALTHCHECK --interval=15s CMD curl --fail http://localhost:8080/micro-hazelcast/resources/micro/ping || exit 1
