FROM nginx
LABEL "MAINTAINER"="Sakarin Kammanee <Sakarin@coe.phuket.psu.ac.th>"

ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install the NGINX Amplify Agent
RUN apt-get update \
    && apt-get install -y curl python apt-transport-https apt-utils gnupg1 procps \
    && echo 'deb https://packages.amplify.nginx.com/debian/ stretch amplify-agent' > /etc/apt/sources.list.d/nginx-amplify.list \
    && curl -fs https://nginx.org/keys/nginx_signing.key | apt-key add - > /dev/null 2>&1 \
    && apt-get update \
    && apt-get install -y nginx-amplify-agent \
    && apt-get purge -y curl apt-transport-https apt-utils gnupg1 \
    && rm -rf /var/lib/apt/lists/*

# Keep the nginx logs inside the container
RUN unlink /var/log/nginx/access.log \
    && unlink /var/log/nginx/error.log \
    && touch /var/log/nginx/access.log \
    && touch /var/log/nginx/error.log \
    && chown nginx /var/log/nginx/*log \
    && chmod 644 /var/log/nginx/*log

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
