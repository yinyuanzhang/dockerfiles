FROM nginx:alpine

COPY nginx/default.conf /etc/nginx/conf.d/default.conf
RUN chown -R nginx /etc/nginx

RUN apk add --no-cache --update git

RUN \
      cd /usr/share/nginx; \
      git clone https://github.com/SchizoDuckie/DuckieTV.git; \
      chown -R nginx /usr/share/nginx
