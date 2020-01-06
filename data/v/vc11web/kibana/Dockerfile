ARG BASE=docker.elastic.co/kibana/kibana:6.4.3
ARG REGISTRY=vc11web
ARG WRAPPER=container-wrapper:v1

FROM $REGISTRY/$WRAPPER
 
###########################################

FROM $BASE

ARG BASE=docker.elastic.co/kibana/kibana:6.4.3
ARG REGISTRY=vc11web
ARG WRAPPER=container-wrapper:v1
ARG IMAGE=kibana:base
ARG LABELNAMESPACE=io.vcweb

ENV entrypoint "/usr/local/bin/kibana-docker"
ENV containerImage "$REGISTRY/$IMAGE"
ENV imageComponent "$IMAGE"
ENV imageBase "$BASE"
ENV imageWrapper "$REGISTRY/$WRAPPER"

COPY ./build/* /usr/share/kibana/config/
RUN rm -rf /usr/share/kibana/plugins/x-pack

USER root
COPY --from=0 /container-wrapper /container-wrapper/
COPY --from=0 /container-wrapper/docs/README.md /container-wrapper/docs/CONTAINER-WRAPPER.md
COPY ./Dockerfile /container-wrapper/setup/docker/Dockerfile
COPY ./README.md /container-wrapper/docs/README.md

COPY ./build/* /container-wrapper/setup/docker/

RUN chmod 777 /container-wrapper && \
    chown -R kibana /container-wrapper && \
    mkdir /output && \
    chmod 777 /container-wrapper && \
    chown -R kibana /output

#USER kibana

ENTRYPOINT ["/container-wrapper/entrypoint.sh"]

LABEL $LABELNAMESPACE.schema-version="1.0"
LABEL $LABELNAMESPACE.name="Kibana"
LABEL $LABELNAMESPACE.description="This is a wrapped $BASE image."
LABEL $LABELNAMESPACE.docker.cmd.help="docker run $REGISTRY/$IMAGE --help"
LABEL $LABELNAMESPACE.image.name="$REGISTRY/$IMAGE"
LABEL $LABELNAMESPACE.image.base="$BASE"
LABEL $LABELNAMESPACE.image.wrapper="$WRAPPER"
LABEL $LABELNAMESPACE.image.type="component"         