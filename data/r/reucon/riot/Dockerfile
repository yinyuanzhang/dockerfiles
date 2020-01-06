FROM nginx:alpine

ENV VERSION=v1.0.0
ENV TGZ=https://github.com/vector-im/riot-web/releases/download/$VERSION/riot-$VERSION.tar.gz

RUN sh -xe \
 && rm /usr/share/nginx/html/* \
 && (wget -qO - $TGZ | tar xvz -C /usr/share/nginx/html/ --strip-components=1)
