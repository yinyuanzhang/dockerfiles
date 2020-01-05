FROM praekeltfoundation/vumi

# Install a modern Nginx
ENV NGINX_VERSION 1.12.1-1~jessie
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
    && echo 'deb http://nginx.org/packages/debian/ jessie nginx' > /etc/apt/sources.list.d/nginx.list \
    && apt-get-install.sh nginx=${NGINX_VERSION} \
    && rm /etc/nginx/conf.d/default.conf \
    && mkdir -p /etc/nginx/includes/junebug

# Forward Nginx access and error logs to stdout/err
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY junebug-entrypoint.sh nginx/nginx-config-gen.sh \
    /scripts/

COPY nginx/vhost.template /config/

EXPOSE 80

ENTRYPOINT ["tini", "--", "junebug-entrypoint.sh"]
