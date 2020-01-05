FROM node:lts as builder

WORKDIR /ui

RUN git clone https://github.com/Dreamacro/clash-dashboard.git \
    && cd clash-dashboard \
    && npm i && npm run build \
    && cp -R dist/* /ui \
    && cd /ui && rm -rf clash-dashboard

FROM dreamacro/clash:dev

ENV TZ=Asia/Shanghai

RUN apk add --no-cache ca-certificates tzdata curl

COPY config.yml /root/.config/clash/
COPY --from=builder /ui /ui
