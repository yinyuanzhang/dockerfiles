FROM dtzar/helm-kubectl:latest

ENV HELM_HOME=/root/.helm

RUN mkdir -vp $HELM_HOME/plugins \
    && helm plugin install https://github.com/chartmuseum/helm-push
