FROM nginx:1.17
ENV SRV_PORT=80
ENV SRV_IP=127.0.0.1
WORKDIR /proxytest
COPY --from=hairyhenderson/gomplate:v2.5.0-slim /gomplate /bin/gomplate
COPY nginx.conf.tmpl nginx.conf.tmpl
COPY cmd.sh cmd.sh
CMD ["./cmd.sh"]
