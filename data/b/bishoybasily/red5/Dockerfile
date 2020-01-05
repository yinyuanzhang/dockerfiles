FROM java:8

ENV RED5_VERSION 1.0.9-RELEASE

ENV RED5_HOME /opt/red5

RUN mkdir -p $RED5_HOME

RUN apt-get update && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    wget -q https://github.com/Red5/red5-server/releases/download/v${RED5_VERSION}/red5-server-${RED5_VERSION}.tar.gz -O red5.tar.gz && \
    tar -xzf red5.tar.gz && \
    mv red5-server/* ${RED5_HOME} && \
    rm -rf red5*

VOLUME [ $RED5_HOME ]

WORKDIR $RED5_HOME

EXPOSE 843 1935 5080 5443 8081 8443

ENTRYPOINT ["./red5.sh"]
