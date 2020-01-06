FROM circleci/golang:1.12.6
ARG OSDK_RELEASE_VERSION=v0.10.0
RUN curl -OJL https://github.com/operator-framework/operator-sdk/releases/download/${OSDK_RELEASE_VERSION}/operator-sdk-${OSDK_RELEASE_VERSION}-x86_64-linux-gnu
RUN chmod +x operator-sdk-${OSDK_RELEASE_VERSION}-x86_64-linux-gnu && sudo cp operator-sdk-${OSDK_RELEASE_VERSION}-x86_64-linux-gnu /usr/local/bin/operator-sdk && rm operator-sdk-${OSDK_RELEASE_VERSION}-x86_64-linux-gnu
