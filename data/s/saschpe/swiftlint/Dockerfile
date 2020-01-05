FROM swift:4.2.1
LABEL maintainer="Sascha Peilicke <sascha@peilicke.de"

ARG swiftlint=0.34.0

LABEL description="SwiftLint ${swiftlint}"

RUN git clone --branch ${swiftlint} https://github.com/realm/SwiftLint.git \
    && cd SwiftLint \
    && swift build --configuration release --static-swift-stdlib \
    && mv `swift build --configuration release --static-swift-stdlib --show-bin-path`/swiftlint /usr/bin \
    && cd .. \
    && rm -rf SwiftLint
RUN apt-get update \
    && apt-get install -y \
        clang curl git libblocksruntime0 libcurl4-openssl-dev libedit2 libicu55 libkqueue0 \
        libpython2.7-dev libxml2 python2.7 tzdata uuid-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN swiftlint version

ENTRYPOINT ["swiftlint"]
