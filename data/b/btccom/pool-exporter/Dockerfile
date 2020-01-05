FROM nginx:alpine
COPY run.sh /run.sh
RUN apk add curl jq --no-cache --update && \
    chmod a+x run.sh
COPY metrics /usr/share/nginx/html/
CMD ["sh", "/run.sh"]
