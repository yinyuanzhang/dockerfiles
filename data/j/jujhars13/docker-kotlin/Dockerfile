FROM java:8

ENV VERSION 1.1.2

ENV KOTLIN_URL https://github.com/JetBrains/kotlin/releases/download/v${VERSION}/kotlin-compiler-${VERSION}.zip

RUN wget ${KOTLIN_URL} -O /tmp/kotlin.zip && \
    unzip /tmp/kotlin.zip -d /opt && \
    rm /tmp/kotlin.zip

ENV PATH $PATH:/opt/kotlinc/bin
