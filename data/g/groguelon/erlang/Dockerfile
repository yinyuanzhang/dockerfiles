FROM amazonlinux:2

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV ERLANG_VERSION 22.1
ENV ERL_TOP /tmp/otp_src_${ERLANG_VERSION}

RUN yum install -y \
    gcc \
    gcc-c++ \
    gzip \
    libxslt \
    m4 \
    make \
    ncurses-devel \
    openssl-devel \
    perl \
    tar \
    unixODBC \
    unixODBC-devel
RUN curl -Lo /tmp/otp_src_${ERLANG_VERSION}.tar.gz http://www.erlang.org/download/otp_src_${ERLANG_VERSION}.tar.gz
RUN tar -C /tmp -xzf /tmp/otp_src_${ERLANG_VERSION}.tar.gz

WORKDIR $ERL_TOP

RUN ./configure --prefix=/opt/erlang/${ERLANG_VERSION} --without-wx --without-javac
RUN make -j$(nproc)
RUN make -j$(nproc) install

FROM amazonlinux:2

LABEL maintainer="Geoffrey Roguelon"

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV PATH /opt/erlang/22.1/bin:$PATH

RUN yum install -y unixODBC libxslt && \
    yum clean all

COPY --from=0 /opt/erlang /opt/erlang

CMD ["erl"]
