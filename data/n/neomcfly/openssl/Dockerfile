FROM gliderlabs/alpine:3.1 

MAINTAINER NEOMCFLY

ENV PGID 1001

ENV PUID 1002

ARG BUILD_HTTP_PROXY

ENV HTTP_PROXY ${BUILD_HTTP_PROXY}

RUN apk-install openssl

ENV HTTP_PROXY ""

ENV BUILD_HTTP_PROXY ""

ENV SIZE 2048

ENV KEY_NAME noname

ENV COUNTRY_NAME ""

ENV PROVINCE_NAME ""
ENV LOCALITY_NAME ""
ENV ORGANISATION_NAME ""
ENV ORGANISATION_UNIT_NAME ""
ENV COMMON_NAME ""

ENV NB_DAYS 3650

WORKDIR /certs

CMD /usr/bin/openssl genrsa -out ${KEY_NAME}.key ${SIZE} && \
    /usr/bin/openssl req    -new -key ${KEY_NAME}.key  -out ${KEY_NAME}.csr -subj "/C=${COUNTRY_NAME}/ST=${PROVINCE_NAME}/L=${LOCALITY_NAME}/O=${ORGANISATION_NAME}/OU=${ORGANISATION_UNIT_NAME}/CN=${COMMON_NAME}"   && \
    /usr/bin/openssl x509   -req -days ${NB_DAYS} -in ${KEY_NAME}.csr -signkey ${KEY_NAME}.key -out ${KEY_NAME}.crt
