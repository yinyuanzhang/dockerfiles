# This image provides an environment for building and running HELM charts.

FROM openshift/base-centos7

MAINTAINER oliverg.ch <o.guggenbuehl@gmail.com>


LABEL io.k8s.description="Platform for building and deploy Helm packages" \
      io.k8s.display-name="HELM ${HELM_VERSION}" \
      io.openshift.tags="builder,helm,helm-${HELM_VERSION},oc"

RUN yum install -y --setopt=tsflags=nodocs git bash && yum clean all

ENV HELM_VERSION=v2.12.3 \
    HELM_HOME=/helm

RUN (curl -L "https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz" | \
        tar -xz -C /usr/local/bin/) && cd /usr/local/bin/linux-amd64 && \
        mv tiller ../ && \
        mv helm .. && cd && rm -rf /usr/local/bin/linux-amd64 && \
    helm init --client-only && \
    helm plugin install https://github.com/chartmuseum/helm-push && \
    helm plugin install https://github.com/databus23/helm-diff --version master && \
    helm version --client && \
    helm plugin list && \
    chmod -R g+rwX "${HELM_HOME}" 

# Install oc-client

ENV OCP_VERSION=v3.11.0 \
    OCP_CLIENT_HASH=0cbc58b
# Install oc-client
RUN (curl -L https://github.com/openshift/origin/releases/download/${OCP_VERSION}/openshift-origin-client-tools-${OCP_VERSION}-${OCP_CLIENT_HASH}-linux-64bit.tar.gz | \
       tar -xz -C /usr/local/bin/) && cd /usr/local/bin/openshift-origin-client-tools-${OCP_VERSION}-${OCP_CLIENT_HASH}-linux-64bit/ &&  mv oc .. && mv kubectl .. && \
       cd - && rm -rf /usr/local/bin/openshift-origin-client-tools-${OCP_VERSION}-${OCP_CLIENT_HASH}-linux-64bit/ 

ENV TZ=Europe/Zurich \
    TERM=xterm
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH
COPY ./s2i/ $STI_SCRIPTS_PATH

USER 1001

# Set the default CMD to print the usage of the language image
CMD $STI_SCRIPTS_PATH/usage
