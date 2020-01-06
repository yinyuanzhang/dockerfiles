FROM arugaldocker/java:1.0

ARG VERSION=6.1.0

RUN  wget -P /usr http://mirrors.tuna.tsinghua.edu.cn/apache/skywalking/6.1.0/apache-skywalking-apm-${VERSION}.tar.gz && \
        cd /usr && mkdir skywalking && \
        tar -zxvf apache-skywalking-apm-${VERSION}.tar.gz && \
        mv apache-skywalking-apm-bin/agent /usr/skywalking && \
        rm -rf apache-skywalking-apm-*

ENV JAVA_AGENT=-javaagent:/usr/skywalking/agent/skywalking-agent.jar