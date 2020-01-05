FROM alpine
LABEL maintainer="lunksana <lunksana@gmail.com>"

ENV REMOTE_URL=127.0.0.1:8000
ENV TOKEN=
ENV UPSTREAM=http://127.0.0.1:80
ARG INLETS_API=https://api.github.com/repos/alexellis/inlets/releases/latest

RUN apk add --no-cache curl \
    && INLETS_VER="$(curl -s ${INLETS_API} | grep 'tag_name' | cut -d\" -f4)" \
    && curl -L -H "Cache-Control: no-cache" -o "/usr/bin/inlets" "https://github.com/alexellis/inlets/releases/download/${INLETS_VER}/inlets" \
    && chmod +x /usr/bin/inlets

ENTRYPOINT inlets client -r ${REMOTE_URL} -u ${UPSTREAM} -t ${TOKEN}
