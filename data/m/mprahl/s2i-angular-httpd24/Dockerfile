# s2i-angular-httpd24
FROM centos/httpd-24-centos7

MAINTAINER Matt Prahl <mprahl@redhat.com>

ENV SUMMARY="Platform for building and running Angular web applications" \
    DESCRIPTION="A Docker container based on centos/httpd-24-centos7 for \
building and running Angular web applications. \
Angular is a development platform for building mobile and desktop web \
applications using Typescript/JavaScript and other languages."

# Inspired from https://github.com/sclorg/s2i-nodejs-container/blob/master/10/Dockerfile
ENV NODEJS_VERSION=10 \
    NPM_CONFIG_PREFIX=$HOME/.npm-global \
    PATH=$HOME/node_modules/.bin/:$HOME/.npm-global/bin/:$PATH

ENV NAME=angular \
    NG_CONFIG=production \
    NODE_ENV=production \
    NPM_CONFIG_LOGLEVEL=info

LABEL summary="$SUMMARY" \
      maintainer="Matt Prahl <mprahl@redhat.com>" \
      description="$DESCRIPTION" \
      name="$NAME-httpd24-centos7" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Angular" \
      io.openshift.expose-services="8080:http,8443:https" \
      io.openshift.tags="builder,$NAME,httpd24" \
      io.s2i.scripts-url="image:///usr/libexec/s2i" \
      usage="s2i build <SOURCE-REPOSITORY> $NAME-httpd24-centos7:latest <APP-NAME>"

# Become root to install packages (was dropped to 1001 in the base image)
USER 0
# Make a directory to place custom Angular environments
RUN mkdir /tmp/ng-environments
# Copy all the files the container needs
COPY ./root/ /
# Set the directory location to whatever is default in the httpd image
# and set the permissions of angular.conf to match the rest of conf.d
RUN sed -i -e "s%REPLACE_WITH_HTTPD_APP_ROOT%${HTTPD_APP_ROOT}%" /etc/httpd/conf.d/angular.conf && \
    chmod -R a+rwx ${HTTPD_MAIN_CONF_D_PATH}
# Postfix all the httpd S2I files with `httpd` so they don't get overwritten
RUN for file in /usr/libexec/s2i/*; do cp -- "$file" "$file-httpd"; done
# Don't try to delete ${dir}/httpd-ssl since this causes an OpenShift pod to
# fail when the TLS files are configured in a volume mount
RUN sed -i '/^.*rm -rf ${dir}\/httpd-ssl.*/d' /usr/share/container-scripts/httpd/common.sh
# Copy the S2I scripts
COPY ./s2i/bin/ /usr/libexec/s2i

# Install NPM
RUN yum install -y --setopt=tsflags=nodocs yum-config-manager centos-release-scl && \
    yum-config-manager --enable rhel-server-rhscl-7-rpms && \
    yum install -y --setopt=tsflags=nodocs rh-nodejs10 rh-nodejs10-npm git && \
    rpm -V rh-nodejs10 rh-nodejs10-npm git && \
    yum clean all -y

# This default user is created in the base image
USER 1001

CMD ["/usr/libexec/s2i/usage"]
