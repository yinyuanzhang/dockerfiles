FROM ruby:2.4.5-alpine3.7

ARG WORKDIR=/app
ENV WORKDIR=$WORKDIR

ARG APP_USER=user
ENV APP_USER=$APP_USER

# Install dependent libraries
RUN apk update \
    && apk upgrade \
    && apk add --no-cache \
      build-base \
      ruby-dev \
      curl \
      bash \
      less \
      ruby-dev \
      build-base \
      git \
      nodejs \
      yarn \
      tzdata \
      postgresql-client \
      mariadb-dev \
      sqlite-dev \
      sqlite-libs \
      imagemagick \
      shadow \
      ttf-dejavu \
      ttf-droid \
      ttf-freefont \
      ttf-liberation \
      ttf-ubuntu-font-family \
      python2-dev \
      python \
      py-pip \
      groff \
      mailcap \
      xvfb \
      fontconfig \
      dbus \
      qt5-qtbase \
      qt5-qtbase-x11 \
      qt5-qtsvg \
      qt5-qtwebkit \
    && pip install --upgrade pip \
    && pip install --upgrade awscli s3cmd python-magic \
    && apk -v --purge del py-pip

RUN apk add --no-cache --force \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ \
    libcrypto1.1

RUN apk add --no-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
    wkhtmltopdf

# Install xvfb-run
# https://bugs.alpinelinux.org/issues/9617
RUN curl -sSL 'https://raw.githubusercontent.com/cjpetrus/alpine_webkit2png/b3ef029bd267cb94723af7ec430f5b1256422274/xvfb-run' > /usr/bin/xvfb-run
RUN chmod +x /usr/bin/xvfb-run

# Tool to propagate singals from the container to the app
# Repo: https://github.com/fpco/pid1
# Explanation: https://www.fpcomplete.com/blog/2016/10/docker-demons-pid1-orphans-zombies-signals
ENV PID1_VERSION=0.1.2.0
RUN curl -sSL "https://github.com/fpco/pid1/releases/download/v${PID1_VERSION}/pid1-${PID1_VERSION}-linux-x86_64.tar.gz" | tar xzf - -C /usr/local \
    && chown root:root /usr/local/sbin \
    && chown root:root /usr/local/sbin/pid1

# Disable documentation for Ruby gems
RUN echo 'gem: --no-rdoc --no-ri' > /etc/gemrc

# Change working directory
WORKDIR $WORKDIR

# Install bundler
# https://bundler.io/v1.16/guides/bundler_docker_guide.html
#
# A version needs to be specified because the base Ruby image explicetly
# specifies the BUNDLER_VERSION variable, therefore, to use more up-to-date
# versions we need to specify them explicitly
ENV BUNDLER_VERSION=2.0.1
RUN gem install bundler -v $BUNDLER_VERSION
ENV GEM_HOME="/usr/local/bundle"
ENV PATH $GEM_HOME/bin:$GEM_HOME/gems/bin:$PATH

# Use Xvfb by default
COPY ./wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf
RUN chmod +x /usr/local/bin/wkhtmltopdf

# Set the entrypoint
COPY ./entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]

