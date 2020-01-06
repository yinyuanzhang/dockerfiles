FROM nginx:alpine

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="e.g. https://github.com/dev-zero/docker-images"

COPY nginx.conf /etc/nginx/nginx.conf
