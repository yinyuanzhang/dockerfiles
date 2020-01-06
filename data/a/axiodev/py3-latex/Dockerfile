###############################################################################
#
# Multi-stage Reporting Web build
#
# build-time environment variables:
#   LTO=1                   . enable link-time-optimizations
#   OPTIMAL=1               . enable profile-guided-optimizations (PGO)
#   PYTHON_VERSION=3.5.3
#
#   ** NOTE **: 
#       . LTO requires PGO
#       . ensure both variables are unset for typical builds
#
# building:
#   make build-image        . run docker build
#   make build-push         . push image to repository
#   make image              . build + push
#
# Stages:
#    runtime <- debian-base-amd64:0.2
#       common runtime packages go here
#    builder <- build-setup
#       dev packages, tools, utilities, etc. go here
#       ./configure <things> && make && make install
#    post-build <- builder
#       install any common python modules here
#    FINAL <- runtime
#       pip package installation goes here + ENTRYPOINT
#
###############################################################################

FROM revolutionsystems/python:3.6.8-wee-optimized-lto as runtime

LABEL stage RUNTIME

###############################################################################


FROM runtime as build-setup


RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    bash-completion \
    ca-certificates \
    file \
    fonts-texgyre \
    g++ \
    gfortran \
    gsfonts \
    libbz2-1.0 \
    libcurl3 \
    libjpeg62-turbo \
    libopenblas-dev \
    libpangocairo-1.0-0 \
    libpcre3 \
    libtiff5 \
    liblzma5 \
    locales \
    make \
    unzip \
    zip \
    zlib1g \
  && BUILDDEPS="curl \
    default-jdk \
    libbz2-dev \
    libcairo2-dev \
    libcurl4-openssl-dev \
    libpango1.0-dev \
    libjpeg-dev \
    libicu-dev \
    libpcre3-dev \
    libpng-dev \
    libssl-dev \
    libtiff5-dev \
    liblzma-dev \
    libx11-dev \
    libxt-dev \
    perl \
    tcl8.6-dev \
    tk8.6-dev \
    texinfo \
    texlive-extra-utils \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-recommended \
    x11proto-core-dev \
    xauth \
    xfonts-base \
    xvfb \
    zlib1g-dev" \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends $BUILDDEPS

RUN apt-get install -y \
  wget \
#  python3 \
  python3-dev


LABEL stage BUILD-SETUP


###############################################################################
FROM build-setup as builder

#install
RUN mkdir -p /opt/texlive
WORKDIR /
COPY ./texlive.profile /opt/texlive

#had to specify a repository that didn't fail often attempting to fetch files   
#&& wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz 

RUN cd /tmp \
    && mkdir texlive \
    && cd texlive \
    && wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
    && tar xf install-tl-unx.tar.gz 

#year 3000 bug below
RUN cd /tmp/texlive/install-tl-2* \
    && ./install-tl -profile /opt/texlive/texlive.profile -repository http://mirror.ctan.org/systems/texlive/tlnet/ \
    && cd /tmp \ 
    && rm -rf /tmp/texlive

ENV PATH /usr/local/texlive/distribution/bin/x86_64-linux:$PATH

LABEL stage BUILDER


###############################################################################

# NOTE: would be better if this were "from runtime!!!" and we ditched all of the build stuff
# will require copying simlinks or specifying a known place to install 
# There's an example profile here with some options specified for that sort of thing:
# https://github.com/felipenoris/math-server-docker/blob/master/Dockerfile

FROM runtime 

COPY --from=builder /usr/local /usr/local
COPY --from=builder /root /root
RUN /sbin/ldconfig

#TODO: need this or is it inherited?
ENV PATH /usr/local/texlive/distribution/bin/x86_64-linux:$PATH


CMD ["/bin/bash"]

LABEL stage FINAL
