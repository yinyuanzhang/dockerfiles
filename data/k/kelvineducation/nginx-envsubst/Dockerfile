FROM nginx:alpine

RUN apk --no-cache add curl

COPY *.sh /
RUN rm /etc/nginx/conf.d/*

# graceful shutdown
STOPSIGNAL SIGQUIT

# run envsubst before starting nginx
ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
