FROM nginx:stable
LABEL maintainer="manzari@mailbox.org"

WORKDIR /usr/share/nginx/html

RUN apt-get update \
 && apt-get install -y wget unzip \
 && wget https://github.com/Laverna/static-laverna/archive/gh-pages.zip -O /tmp/laverna.zip \
 && unzip /tmp/laverna.zip -d /tmp \
 && mv /tmp/static-laverna-gh-pages/* /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
