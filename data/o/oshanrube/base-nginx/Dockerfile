# nginx
FROM oshanrube/base

# TODO: Put the maintainer name in the image metadata
MAINTAINER Oshan Rube <oshanrube@gmail.com>

# TODO: Rename the builder environment variable to inform users about application you provide them
ENV BUILDER_VERSION 1.0

# TODO: Set labels used in OpenShift to describe the builder image
LABEL io.k8s.description="base image for nginx" \
      io.k8s.display-name="builder 0.0.1" \
      io.openshift.expose-services="80:http" \
      io.openshift.tags="builder,0.0.1,nginx,etc."

# TODO: Install required packages here:
# RUN dnf -y --setopt=tsflags=nodocs install nginx && dnf clean all
# install pagespeed
COPY ./pagespeed pagespeed
COPY  ["config/build_ngx_pagespeed.sh", "build_ngx_pagespeed.sh"]
RUN ./build_ngx_pagespeed.sh --nginx-version 1.11.6

# Copy the S2I scripts to /usr/libexec/s2i since we set the label that way
COPY  ["config/nginx.conf", "/etc/nginx/nginx.conf"]
COPY  ["config/vhost.conf", "/etc/nginx/conf.d/vhost.conf"]

RUN mkdir -p /var/ngx_pagespeed_cache && chmod -R a+rwx /var/ngx_pagespeed_cache && chown -R 1001:0 /var/ngx_pagespeed_cache
RUN mkdir -p /var/cache/nginx/client_temp && chmod -R a+rwx /var/cache/nginx/client_temp && chown -R 1001:0 /var/cache/nginx/client_temp
RUN mkdir -p /var/cache/nginx/proxy_temp && chmod -R a+rwx /var/cache/nginx/proxy_temp && chown -R 1001:0 /var/cache/nginx/proxy_temp
RUN mkdir -p /var/cache/nginx/fastcgi_temp && chmod -R a+rwx /var/cache/nginx/fastcgi_temp && chown -R 1001:0 /var/cache/nginx/fastcgi_temp
RUN mkdir -p /var/cache/nginx/uwsgi_temp && chmod -R a+rwx /var/cache/nginx/uwsgi_temp && chown -R 1001:0 /var/cache/nginx/uwsgi_temp
RUN mkdir -p /var/cache/nginx/scgi_temp && chmod -R a+rwx /var/cache/nginx/scgi_temp && chown -R 1001:0 /var/cache/nginx/scgi_temp

# Export the environment variable that provides information about the application.
# Replace this with the according version for your application.
ENV NGINX_VERSION=1.6.3

# TODO: Copy the S2I scripts to /usr/local/s2i, since openshift/base-centos7 image sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./.s2i/bin/ $STI_SCRIPTS_PATH

# Copy the S2I scripts to /usr/libexec/s2i since we set the label that way
RUN mkdir -p /var/www/html /var/log/nginx

# TODO: Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chmod -R a+rwx /var/www/html && chown -R 1001:0 /var/www/html
RUN chmod -R a+rwx /var/log/nginx && chown -R 1001:0 /var/log/nginx

# logs
RUN ln -sf /dev/stdout /var/log/nginx/access_log.log
RUN ln -sf /dev/stderr /var/log/nginx/error_log.log

# TODO: Set the default port for applications built using this image
EXPOSE 80

# set user
USER 1000

# TODO: Set the default CMD for the image
CMD $STI_SCRIPTS_PATH"/usage"
