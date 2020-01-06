FROM nginx:latest

COPY nginx-dev.conf /etc/nginx/conf.d/default.conf

RUN apt-get update && apt-get install openssl
RUN openssl dhparam -out /etc/ssl/certs/dhparam-2048.pem 2048
RUN openssl req -subj '/CN=api.luncheonette.app/O=Emilio Clemente/C=ES' -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -keyout /etc/ssl/certs/server.key -out /etc/ssl/certs/server.crt

EXPOSE 80 443 8080