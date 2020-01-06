FROM centos/ruby-22-centos7

LABEL io.k8s.description="Base Image for Rails plus openssl client" \
      io.k8s.display-name="pitc-rails-bi-openssl" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,ruby,ruby22,httpd,openssl"

USER root

# Install openssl
RUN yum update -y && \
    INSTALL_PKGS="openssl" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    yum clean all -y

USER 1001
