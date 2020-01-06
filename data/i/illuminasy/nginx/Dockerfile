# Illuminasy Nginx Docker Image
#
# VERSION               1.0.2

FROM nginx:1.17.6

LABEL Description="This image contains NGINX v1.17.6 image with NGINX Amplify Agent."
LABEL Vendor="Illuminasy"
LABEL Version="1.0.2"
LABEL maintainer="Abhishek Salian <abhi@illuminasy.com>"
LABEL com.illuminasy.nginx.version="1.0.2"
LABEL com.illuminasy.nginx.release-date="2019-11-26"
LABEL com.illuminasy.nginx.version.is-production="true"

# Install the NGINX Amplify Agent
RUN apt-get update \
    && apt-get install -qqy curl python apt-transport-https apt-utils gnupg1 procps \
    && echo 'deb https://packages.amplify.nginx.com/debian/ stretch amplify-agent' > /etc/apt/sources.list.d/nginx-amplify.list \
    && curl -fs https://nginx.org/keys/nginx_signing.key | apt-key add - > /dev/null 2>&1 \
    && apt-get update \
    && apt-get install -qqy nginx-amplify-agent \
    && apt-get purge -qqy curl apt-transport-https apt-utils gnupg1 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove \
    && apt-get clean

# Keep the nginx logs inside the container
RUN unlink /var/log/nginx/access.log \
    && unlink /var/log/nginx/error.log \
    && touch /var/log/nginx/access.log \
    && touch /var/log/nginx/error.log \
    && chown nginx /var/log/nginx/*log \
    && chmod 644 /var/log/nginx/*log \
    && mkdir -p /www/base_site \
    && chown -R nginx:nginx /www \
    && mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak

# Copy nginx config
COPY ./conf.d/nginx.conf /etc/nginx/
COPY ./conf.d/stub_status.conf /etc/nginx/conf.d

# The nginx_entrypoint.sh script will launch nginx and the Amplify Agent.
# The script honors AMPLIFY_API_KEY and AMPLIFY_IMAGENAME environment
# variables, and updates /etc/amplify-agent/agent.conf accordingly.

COPY ./nginx_entrypoint.sh /opt/nginx_entrypoint.sh

# Change permission on startup scripts
RUN chmod 755 /opt/nginx_entrypoint.sh

# Copy version file
COPY ./VERSION ./

ENTRYPOINT ["/opt/nginx_entrypoint.sh"]
