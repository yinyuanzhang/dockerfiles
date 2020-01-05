FROM openjdk:11-jre

ARG version="1.3.3"

RUN mkdir /work

RUN cd / \
    && wget -q https://github.com/repseqio/repseqio/releases/download/v${version}/repseqio-${version}.zip \
    && unzip repseqio-${version}.zip \
    && mv repseqio-${version} repseqio \
    && rm repseqio-${version}.zip

ENV PATH="/repseqio:${PATH}"

COPY repseqio /repseqio/repseqio

WORKDIR /work

ENTRYPOINT ["/bin/bash"]
