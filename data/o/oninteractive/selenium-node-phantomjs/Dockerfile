#
# Selnium Node Phantomjs Dockerfile
#
FROM akeem/selenium-node-phantomjs

MAINTAINER ON Interactive <contato@oninteractive.com.br>

COPY ./scripts/wait-for-it.sh /tmp/wait-for-it.sh

RUN chmod +x /tmp/wait-for-it.sh

ENTRYPOINT [ "sh", "-c", "/tmp/wait-for-it.sh" ]