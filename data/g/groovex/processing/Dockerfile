FROM ubuntu:16.04

RUN apt-get update -qq && \
    apt-get install -qq xvfb default-jre wget unzip && \
    rm -rf /var/lib/apt/lists/*

RUN cd /opt && \
    wget -q http://download.processing.org/processing-3.3.7-linux64.tgz && \
    tar zxf processing-3.3.7-linux64.tgz && \
    mv processing-3.3.7 processing && \
    ln -s /opt/processing/processing-java /usr/local/bin && \
    rm processing-3.3.7-linux64.tgz

RUN mkdir -p /root/sketchbook/libraries && \
    cd /root/sketchbook/libraries && \
    wget -q https://github.com/alexandrainst/processing_websockets/releases/download/latest/webSockets.zip && \
    unzip -q webSockets.zip && \
    rm webSockets.zip

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
