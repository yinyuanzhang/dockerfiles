FROM node:8.4-alpine
ENV LOG_LEVEL "info"

COPY . /opt/certificate-service-manager
RUN rm -rf /opt/certificate-service-manager/openssl
RUN chmod +x /opt/certificate-service-manager/docker-entrypoint.sh
RUN apk --update add curl git ca-certificates openssl python build-base libtool autoconf automake py-pip &&\
    cd /opt/certificate-service-manager && npm install &&\
    pip install --upgrade awscli==1.14.5 s3cmd==2.0.1 python-magic && \
    apk -v --purge del py-pip && \
    rm -rf /var/lib/apt/lists/* &&\
    rm -rf /var/cache/apk/*

WORKDIR "/opt/certificate-service-manager/"

EXPOSE 80

CMD ["npm","start"]