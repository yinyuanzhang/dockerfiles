# openshift-laravel
FROM openshift/base-centos7

LABEL maintainer="Sebastian Kemi <sebekish@gmail.com>"

# TODO: Rename the builder environment variable to inform users about application you provide them
# ENV BUILDER_VERSION 1.0

# TODO: Set labels used in OpenShift to describe the builder image
LABEL io.k8s.description="Platform for building Laravel" \
      io.k8s.display-name="openshift-laravel" \
      io.openshift.expose-services="8080:http"
#      io.openshift.tags="builder,x.y.z,etc."


RUN yum install epel-release -y && \
    rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \
    yum install nginx -y && \
    yum install php72w-fpm php72w-opcache php72w-cli php72w-mbstring php72w-pgsql \
                php72w-bcmath php72w-common php72w-pdo php72w-xml php72w-soap php72w-gd -y && \
    yum clean all

# TODO (optional): Copy the builder files into /opt/app-root
# COPY ./<builder_folder>/ /opt/app-root/

# TODO: Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7 image
# sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./s2i/bin/ /usr/libexec/s2i

COPY ./etc/ /etc/

# TODO: Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:0 /usr/share/nginx && chmod -R g+rwX /usr/share/nginx
RUN chown -R 1001:0 /var/log/nginx && chmod -R g+rwX /var/log/nginx
RUN chown -R 1001:0 /var/lib/nginx && chmod -R g+rwX /var/lib/nginx
RUN touch /run/nginx.pid
RUN chown -R 1001:0 /run/nginx.pid && chmod -R g+rwX /run/nginx.pid
RUN chown -R 1001:0 /etc/nginx && chmod -R g+rwX /etc/nginx

RUN touch /var/run/php-fpm/php-fpm.pid
RUN chown -R 1001:0 /var/run/php-fpm/php-fpm.pid && chmod -R g+rwX /var/run/php-fpm/php-fpm.pid


RUN chown -R 1001:0 /opt/app-root/src && chmod -R g+rwX /opt/app-root/src

# This default user is created in the openshift/base-centos7 image
USER 1001

# TODO: Set the default port for applications built using this image
EXPOSE 8080

# TODO: Set the default CMD for the image
CMD ["/usr/libexec/s2i/usage"]
