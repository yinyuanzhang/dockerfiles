FROM openshift/base-centos7

ENV ERLANG_VERSION 21.1

LABEL io.k8s.description="Platform for building and running an erlang app" \
      io.k8s.display-name="build-erlang" \
      io.openshift.tags="builder,erlang" \
      com.redhat.dev-mode="DEV_MODE:false" \
      com.redhat.deployments-dir="/opt/app-root/src" \
      name="jshmrtn/s2i-erlang" \
      maintainer="Jonatan Männchen <maennchen@joshmartin.ch>" \
      version="$ERLANG_VERSION"

# Install Erlang
RUN set -x \
  && yum install -y --setopt=tsflags=nodocs \
    git \
    autoconf \
    epel-release \
    gcc \
    gcc-c++ \
    git \
    glibc-devel \
    java-1.8.0-openjdk-devel \
    make \
    ncurses-devel \
    openssl-devel \
    wxBase \
  && curl -LO http://erlang.org/download/otp_src_${ERLANG_VERSION}.tar.gz \
  && tar xf otp_src_${ERLANG_VERSION}.tar.gz \
  && rm -rf otp_src_${ERLANG_VERSION}.tar.gz \
  && cd otp_src_${ERLANG_VERSION} \
  && export ERL_TOP=`pwd` \
  && LIBS="/usr/lib64/libcrypto.so" ./configure --enable-static-nifs \
  && make \
  && make release_tests \
  && make install \
  && yum remove -y \
    autoconf \
    epel-release \
    gcc \
    gcc-c++ \
    git \
    glibc-devel \
    java-1.8.0-openjdk-devel \
    make \
    ncurses-devel \
    openssl-devel \
    wxBase \
  && yum clean all -y \
  && cd .. \
  && rm -rf otp_src_${ERLANG_VERSION}

RUN localedef -i en_US -f UTF-8 en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Copy the S2I scripts from the image to $STI_SCRIPTS_PATH
COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:0 /opt/app-root && chmod -R ug+rwx /opt/app-root
USER 1001

# Set the default CMD to print the usage of the language image
CMD $STI_SCRIPTS_PATH/usage
