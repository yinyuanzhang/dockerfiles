FROM devth/helm:latest

RUN apk add \
        bash \
        bats \
        curl \
        docker \
        git  \
        make &&\
    curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/v0.23.0/skaffold-linux-amd64 && \
    chmod +x skaffold && \
    mv skaffold /usr/local/bin; \
    curl -Lo container-structure-test https://storage.googleapis.com/container-structure-test/latest/container-structure-test-linux-amd64 && \
    chmod +x container-structure-test && \
    mv container-structure-test /usr/local/bin


