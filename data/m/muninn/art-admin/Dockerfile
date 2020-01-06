FROM node as builder

ADD . /app

WORKDIR /app

RUN npm install -g @tarojs/cli && npm i && taro build --type h5

FROM abiosoft/caddy:no-stats

COPY --from=builder /app/dist /app

COPY Caddyfile /etc/Caddyfile
