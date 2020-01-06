FROM debian:stable

RUN apt-get update && apt-get upgrade -y
RUN apt-get install git-core nginx fcgiwrap -y
RUN update-rc.d fcgiwrap enable

COPY git-server.conf /etc/nginx/sites-available/default
CMD  service fcgiwrap start && nginx -g "daemon off;"
EXPOSE 80
