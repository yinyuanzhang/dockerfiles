FROM hairyhenderson/gomplate:v3.4.0-alpine as gomplate
FROM nginx:1.15-alpine

ENV HOMEPAGE=https://formunauts.com
ENV EMAIL=support@formunauts.at

COPY --from=gomplate /bin/gomplate /usr/bin/gomplate

ADD rootfs/ /

CMD ["gomplate", "--input-dir", "/usr/share/nginx/html/", "--output-dir", "/usr/share/nginx/html/", "--", "nginx", "-g", "daemon off;"]
