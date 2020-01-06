FROM psaudio/alpine-base as base

FROM nginx:1.15.8-alpine

COPY --from=base /usr/ /usr/

COPY config/override_me.conf /etc/nginx/conf.d/default.conf