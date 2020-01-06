FROM alpine:3.8 as build

ENV ELM_VERSION=0.19.0
ENV ELM_URL=https://github.com/elm/compiler/releases/download/${ELM_VERSION}/binary-for-linux-64-bit.gz

RUN wget -O elm.gz ${ELM_URL}
RUN gunzip elm.gz
RUN chmod +x elm
RUN pwd

FROM node:12-alpine

ENV ELMSTATIC_VERSION=0.6.2

COPY --from=build /elm /bin/elm

RUN npm i --cache /tmp/empty-cache -g elmstatic@${ELMSTATIC_VERSION}
RUN rm -rf /tmp/empty-cache

WORKDIR /opt/app

ENTRYPOINT ["elmstatic"]

CMD ["--help"]
