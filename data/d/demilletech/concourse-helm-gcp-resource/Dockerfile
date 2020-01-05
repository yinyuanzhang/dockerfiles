FROM linkyard/concourse-helm-resource:2.10.0-1

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/google-cloud-sdk/bin
ENV KUBERNETES_VERSION 1.10.7
ENV GCLOUD_SDK_VERSION 217.0.0
ENV GCLOUD_SDK_URL https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-217.0.0-linux-x86_64.tar.gz

RUN apk update && \
      apk add curl openssl python && \
      mkdir -p /opt &&\
      cd /opt &&\
      wget -q -O - $GCLOUD_SDK_URL |tar zxf - &&\
      /bin/sh -l -c "echo Y | /opt/google-cloud-sdk/install.sh && exit"

RUN helm init --client-only && \
    helm plugin install https://github.com/viglesiasce/helm-gcs.git --version v0.1.1


COPY resource /opt/resource

ENTRYPOINT "/bin/sh"
