FROM alpine
RUN sed -i -e 's/v[[:digit:]]\..*\//edge\//g' /etc/apk/repositories
RUN apk add --no-cache nodejs-current py-pygments sassc hugo

