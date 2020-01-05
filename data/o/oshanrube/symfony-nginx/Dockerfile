# symfony
FROM oshanrube/base-nginx

# TODO: Put the maintainer name in the image metadata
MAINTAINER Oshan Rube <oshanrube@gmail.com>

# TODO: Set labels used in OpenShift to describe the builder image
LABEL io.k8s.description="Platform for building symfony" \
      io.k8s.display-name="builder 0.0.1" \
      io.openshift.expose-services="80:http" \
      io.openshift.tags="builder,0.0.1,nginx,etc."

# Copy the S2I scripts to /usr/libexec/s2i since we set the label that way
COPY  ["config/vhost.conf", "/etc/nginx/conf.d/vhost.conf"]

# TODO: Copy the S2I scripts to /usr/local/s2i, since openshift/base-centos7 image sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./.s2i/bin/ $STI_SCRIPTS_PATH

# This default user is created in the openshift/base-centos7 image
USER 1001
