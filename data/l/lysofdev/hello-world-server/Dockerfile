FROM httpd:2.4.39-alpine

ARG PORT=80

ENV PORT=$PORT

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

COPY ./dist/ /usr/local/apache2/htdocs/