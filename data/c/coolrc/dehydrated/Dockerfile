FROM alpine

LABEL maintainer="https://github.com/coolrc136"

RUN apk --no-cache add \
    bash \
    curl \
    openssl \
&& mkdir dehydrated \
&& cd dehydrated \
&& wget -q https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated \
&& chmod +x dehydrated

COPY config /dehydrated/config

CMD /dehydrated/dehydrated --register --accept-terms && /dehydrated/dehydrated -c
