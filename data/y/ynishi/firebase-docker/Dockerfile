FROM node:8.11.4

ENV FIREBASE_TOOLS_VERSION 4.1.2 
ENV TAG_VERSION 8.11.4-4.1.2-1 

RUN set -eux; \
    yarn global add \
        firebase-tools@${FIREBASE_TOOLS_VERSION} \
        js-beautify \
        typescript \
        eslint \
        tslint \
    && firebase --version \
    && tsc --version \
    && eslint --version \
    && tslint --version

RUN set -eux; \
  mkdir /project
WORKDIR /project

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 5000

CMD ["firebase"]
