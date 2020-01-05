FROM debian:buster-slim
LABEL mantainer=fams@linuxplace.com.br
COPY ./Docker/ /var/www/html
EXPOSE 80
RUN apt-get update -y && apt-get dist-upgrade -y && apt-get install --no-install-recommends python3 -y
WORKDIR  /var/www/html
ENTRYPOINT [ "python3", "-m", "http.server", "80" ]
