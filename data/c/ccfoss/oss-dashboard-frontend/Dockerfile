FROM ccfoss/alpine-consul
MAINTAINER jowilkey@cisco.com

# Install app dependencies
WORKDIR /var/www/static
ADD . .

# Install Node/NPM
RUN apk add --update curl nodejs bash && \
	npm install -d && \
    npm test && \
	npm run pack && \
    npm prune --production && \
	apk del nodejs && \
	rm -rf /var/cache/apk/*

# Compile NGINX
WORKDIR nginx
RUN apk add --update curl g++ pcre pcre pcre-dev zlib zlib-dev openssl openssl-dev make libcap

# Build the server
RUN auto/configure \
    --with-http_ssl_module \
    --with-http_v2_module \
    --without-http_empty_gif_module \
    --without-http_memcached_module \
    --without-http_uwsgi_module \
    --without-http_scgi_module \
    --without-http_fastcgi_module \
    --without-http_geo_module \
    --without-http_autoindex_module \
    --without-http_split_clients_module \
    --without-mail_pop3_module \
    --without-mail_imap_module \
    --without-mail_smtp_module \
    --without-http_access_module \
    && make && make install

# Create system accounts/groups/directories for Nginx
RUN addgroup www-data && \
    adduser -S www-data -G www-data -s /sbin/nologin -D && \
    chown -R www-data:www-data /usr/local/nginx && \
    setcap 'cap_net_bind_service=+ep' /usr/local/nginx/sbin/nginx && \
    mkdir -p /var/log/nginx && \
    chown www-data:www-data /var/log/nginx

# Lock www-data account
RUN passwd -l www-data || true

COPY nginx.conf.ctmpl /etc/nginx/nginx.conf.ctmpl
COPY consul-template.hcl /etc/consul.d/

# Nginx permissions
RUN chmod -R 755 /var/www/static && \
    chmod 710 /usr/local/nginx/sbin/nginx && \
    chown -R www-data:www-data /etc/nginx && \
    chown -R www-data:www-data /var/www/static && \
    chown www-data:www-data /var/www && \
    chmod 700 /var/www

# Remove build residue
WORKDIR /var/www/static
RUN rm -rf $(find . ! -path "." \
    ! -path "./node_modules" \
    ! -path "./partials" \
    ! -path "./app" \
    ! -path "./index*" \
    ! -path "./assets" \
     -maxdepth 1)

CMD ["/usr/local/nginx/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]
