FROM node AS npm-build
COPY . .
RUN npm install && npm run build

FROM nginx:1.14-alpine
COPY --from=npm-build ./build/ /usr/share/nginx/html/
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./run.sh /usr/share/run.sh

# set env default value.
ENV TZ=Asia/Shanghai \
    BASE_URL="http://localhost" \
    FLINK_SUPPORT="false"
RUN set -ex \
    && apk add --no-cache bash \
    && chmod +x /usr/share/run.sh  \
    && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo "$TZ" > /etc/timezone \
    && rm -rf /app

EXPOSE 80
CMD /usr/share/run.sh && nginx -g 'daemon off;'
