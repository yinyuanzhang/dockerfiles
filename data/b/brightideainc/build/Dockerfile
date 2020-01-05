FROM brightideainc/bi_php_base:4.2.1

ENV NODE_VERSION="10.15.1"
ENV PROTOBUF_VERSION="3.7.1"
ENV COMPOSER_ALLOW_SUPERUSER = 1

COPY .bashrc /.bashrc

RUN yum install -y which git xz mysql ruby22 ruby22-devel bzip2 \
yum -y clean all

RUN pip install boto3; \
curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz"; \
tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1; \
rm "node-v$NODE_VERSION-linux-x64.tar.xz"; \
ln -s /usr/local/bin/node /usr/local/bin/nodejs; \
/usr/local/bin/npm install grunt-cli sql-cli -g; \
curl -sS https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer \
    | php -- --quiet && mv composer.phar /usr/local/bin/composer; \
gem install compass --pre --no-rdoc --no-ri; \
curl -L https://github.com/Versent/saml2aws/releases/download/v2.13.0/saml2aws_2.13.0_linux_amd64.tar.gz --output saml2aws.tar.gz; \
tar -zxvf saml2aws.tar.gz; \
mv saml2aws /usr/local/bin; \
rm saml2aws.tar.gz; \
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/protoc-${PROTOBUF_VERSION}-linux-x86_64.zip; \
unzip -o protoc-${PROTOBUF_VERSION}-linux-x86_64.zip -d /usr/local bin/protoc; \
unzip -o protoc-${PROTOBUF_VERSION}-linux-x86_64.zip -d /usr/local include/*; \
curl -SL -o /usr/local/bin/grpc_php_plugin https://github.com/brightideainc/grpc/releases/download/v1.20.0/grpc_php_plugin; \
chmod u+x /usr/local/bin/grpc_php_plugin;

WORKDIR /website/main
CMD /website/main/config/scripts/build.sh
