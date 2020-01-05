FROM docker.elastic.co/apm/apm-server:6.5.3

COPY 6.5.3/apm-server.yml /usr/share/apm-server/apm-server.yml
USER root
RUN chown root:apm-server /usr/share/apm-server/apm-server.yml
RUN chmod go-w /usr/share/apm-server/apm-server.yml
USER apm-server
#docker run \
#  --mount type=bind,source="$(pwd)"/apm-server.yml,target=/usr/share/apm-server/apm-server.yml \
#  docker.elastic.co/apm/apm-server:6.5.3