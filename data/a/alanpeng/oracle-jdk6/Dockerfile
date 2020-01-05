FROM oraclelinux:6.8

MAINTAINER Alan Peng <peng.alan@gmail.com>

ENV JAVA16_HOME /root/jdk/jdk1.6.0_45

USER root

RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/6u45-b06/jdk-6u45-linux-x64.bin > jdk-6u45-linux-x64.bin && \
    mkdir /root/jdk && \
    chmod +x jdk-6u45-linux-x64.bin && \
    ./jdk-6u45-linux-x64.bin && \
    rm jdk-6u45-linux-x64.bin && \
    mv jdk1.6.0_45 /root/jdk

ENV PATH=$PATH:/root/jdk/jdk1.6.0_45/bin

CMD ["bash"]
