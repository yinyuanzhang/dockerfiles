FROM pecorarista/pipenv

SHELL ["/bin/bash", "-c"]

ENV DEBCONF_NOWARNINGS yes

USER root

RUN apt-get update \
    && sudo apt-get install -y \
        apache2-utils \
        nginx \
        build-essential \
        libpq-dev \
        supervisor \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*

RUN echo $'server {\n\
    listen 443 ssl default_server;\n\
    charset utf-8;\n\
    client_max_body_size 80M;\n\
\n\
    ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;\n\
    ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;\n\
\n\
    location / {\n\
        auth_basic "Restricted";\n\
        auth_basic_user_file /etc/nginx/.htpasswd;\n\
        try_files $uri @webapp;\n\
    }\n\
\n\
    location @webapp {\n\
        include uwsgi_params;\n\
        uwsgi_pass unix:/opt/aistairc/market-reporter/uwsgi.sock;\n\
    }\n}' > /etc/nginx/conf.d/nginx.conf

RUN openssl genrsa 2048 > nginx-selfsigned.key \
    && chmod 400 nginx-selfsigned.key \
    && openssl req -batch -new -key nginx-selfsigned.key > nginx-selfsigned.csr \
    && openssl x509 -in nginx-selfsigned.csr -days 30 -req -signkey nginx-selfsigned.key > nginx-selfsigned.crt \
    && mv nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned.crt \
    && mv nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned.key \
    && rm nginx-selfsigned.csr

ENV MARKET_REPORTER_BASIC_AUTH_PASSWORD "market-reporter-basic-auth-password"

RUN htpasswd -b -c /etc/nginx/.htpasswd reporter ${MARKET_REPORTER_BASIC_AUTH_PASSWORD}

RUN echo $'[supervisord]\n\
user=root\n\
nodaemon=false\n\
\n\
[program:nginx]\n\
command=/usr/sbin/nginx -g "daemon off;"' > /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT /usr/bin/supervisord --nodaemon --user root --configuration /etc/supervisor/supervisord.conf

WORKDIR /home/circleci
