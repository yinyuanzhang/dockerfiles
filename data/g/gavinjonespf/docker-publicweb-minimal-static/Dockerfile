FROM nginx:alpine

ARG         COMMIT_ID
COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /app/site/httpdocs && mkdir -p /app/site/logs
