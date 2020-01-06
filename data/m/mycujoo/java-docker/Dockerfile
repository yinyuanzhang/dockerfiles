FROM google/cloud-sdk:alpine

RUN gcloud components install kubectl

# Allow the host to use gradle cache, otherwise gradle will always download plugins & artifacts on every build
VOLUME ["/root/.gradle/caches/"]

RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
     apk update && \
     apk add docker tar bash openssl git py-pip openjdk8
     
RUN \
    cd /usr/local && \
    curl -L https://services.gradle.org/distributions/gradle-4.10-bin.zip -o gradle-4.10-bin.zip && \
    unzip gradle-4.10-bin.zip && \
    rm gradle-4.10-bin.zip

# Export some environment variables
ENV GRADLE_HOME=/usr/local/gradle-4.10
ENV PATH=$PATH:$GRADLE_HOME/bin JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk

RUN pip install docker-compose

ADD https://releases.hashicorp.com/vault/0.9.0/vault_0.9.0_linux_amd64.zip /tmp

WORKDIR /tmp
RUN unzip vault_0.9.0_linux_amd64.zip && mv vault /usr/local/bin
RUN chmod +x /usr/local/bin/vault

# Install HELM
RUN bash -c "$(curl -sS https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get)"