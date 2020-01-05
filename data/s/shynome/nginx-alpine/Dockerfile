FROM nginx:stable-alpine

STOPSIGNAL SIGTERM
EXPOSE 80
WORKDIR /app

COPY rootfs /

CMD ["nginx", "-g", "daemon off;"]