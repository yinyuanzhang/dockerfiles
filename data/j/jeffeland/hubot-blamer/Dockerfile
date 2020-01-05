FROM jeffeland/hubot
MAINTAINER Jean-Francois Landreau

ENV KUBECTL_VERSION v1.15.0

RUN cd scripts \
   own&& wget https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl \
    && chmod +x ./kubectl
COPY --chown=hubot src scripts
