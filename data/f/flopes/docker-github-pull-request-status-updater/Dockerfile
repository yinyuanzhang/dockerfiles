FROM alpine:3.7

LABEL maintainer="Florian Lopes <florian.lopes@outlook.com>"

ENV GITHUB_API_BASE_URL https://api.github.com/repos

RUN apk add --no-cache curl jq

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

WORKDIR /

ENTRYPOINT ["./entrypoint.sh"] $@
