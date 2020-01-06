FROM openjdk:8-jre-stretch

LABEL maintainer="Lechuck Roh <lechuckroh@gmail.com>"
LABEL name="SenchaCmd 6.7.0.63"

WORKDIR /usr/src/myapp
VOLUME ["/usr/src/myapp"]
ENV PATH="/opt/Sencha/Cmd/6.7.0.63:${PATH}"

RUN cd /tmp && \
    wget -q http://cdn.sencha.com/cmd/6.7.0.63/no-jre/SenchaCmd-6.7.0.63-linux-amd64.sh.zip && \
    unzip *.zip && \
    ./SenchaCmd-6.7.0.63-linux-amd64.sh -q -dir /opt/Sencha/Cmd/6.7.0.63 && \
    rm -f SenchaCmd* && \
    mkdir -p /usr/src/myapp

CMD ["sencha"]
