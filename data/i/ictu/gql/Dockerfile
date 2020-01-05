FROM alpine:3.6

ENV GRAPHQL_URL http://www.semantiql.infra.ictu/api

RUN apk add --no-cache curl jq

ADD query.sh /usr/local/sbin/query

ENTRYPOINT ["query"]
