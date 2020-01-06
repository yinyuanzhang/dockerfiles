FROM tomcat:8-alpine
LABEL MAINTAINER SiritasDho<dahoba@gmail.com>

RUN apk --update --no-cache add \
        alpine-sdk \
        autoconf \
        automake \
        git \
        libtool \
        libseccomp-dev \
        cmake \
        p11-kit-dev \
        openssl-dev \
        stunnel

WORKDIR /tmp/pkcs11-proxy
RUN git clone https://github.com/SUNET/pkcs11-proxy /tmp/pkcs11-proxy && \
    cd /tmp/pkcs11-proxy && \
    cmake . && make && make install

WORKDIR $CATALINA_HOME
RUN rm -rf /tmp/pkcs11-proxy
RUN apk --update --no-cache add git opensc openssl stunnel

EXPOSE 5658
EXPOSE 8080
ENV PKCS11_PROXY_SOCKET="tcp://softhsm:5657"
CMD ["catalina.sh", "run"]
