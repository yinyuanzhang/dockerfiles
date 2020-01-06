FROM nginx:1.15
MAINTAINER DELOTRE <dsi@delotre.com>

# =========================================
# Install common tools and .bashrc file
# =========================================
ADD docker-generics/* /docker-generics/
COPY /docker-generics/bashrc.root /root/.bashrc
RUN bash /docker-generics/apt.sh

# =========================================
# Set ENV variables
# =========================================
ENV DEBUG=false
ENV NGINX_PROJECT_TYPE=default
ENV NGINX_ROOT=/var/www/htdocs
ENV NGINX_HOSTNAME=localhost
ENV NGINX_USERNAME=nginx
ENV NGINX_UID=101
ENV NGINX_MAX_BODY_SIZE=100M

ENV NGINX_TOOLS=false
ENV NGINX_TOOLS_HOSTNAME=
ENV NGINX_TOOLS_RESTRICTED_PWD=
ENV NGINX_TOOLS_RESTRICTED_IPS=
ENV NGINX_TOOLS_PROXYS=

ENV NGINX_BACKEND_HOST=fpm
ENV NGINX_BACKEND_PORT=9000
ENV NGINX_BACKEND_CONNECT_TIMEOUT=10s
ENV NGINX_BACKEND_READ_TIMEOUT=60s


# =========================================
# Add config templates
# =========================================
ADD templates/* /templates/
ADD entrypoints/* /entrypoints/

ADD conf/*.conf /etc/nginx/conf.d/
ADD conf/includes/*.conf /etc/nginx/conf.d/includes/
ADD index.html /var/www/html/index.html

# =========================================
# Expose ports and set entrypoint
# =========================================
EXPOSE 80
EXPOSE 443
EXPOSE 8888

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN ["chmod", "+x", "/docker-entrypoint.sh"]
ENTRYPOINT ["/docker-entrypoint.sh"]

WORKDIR $NGINX_ROOT

CMD ["nginx", "-g", "daemon off;"]
