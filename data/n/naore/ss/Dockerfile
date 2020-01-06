# Dockerfile for ss

FROM shadowsocks/shadowsocks-libev:latest

COPY s.json /s.json

CMD ss-server -c /s.json 
