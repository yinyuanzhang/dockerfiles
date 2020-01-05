# ---- Build Stage ----
# FROM bitwalker/alpine-elixir:1.9.4 as app_builder
# For building Erlang by hand
# FROM debian:stretch as app_builder
FROM erlang:22.1 as app_builder
ARG phoenix_subdir=.
ARG build_env=prod
ENV PATH /root/.asdf/bin:/root/.asdf/shims:$PATH
ENV MIX_ENV=${build_env} TERM=xterm
ENV DB_USER postgres
ENV DB_PASSWORD postgres
ENV DB_NAME calltelemetry_prod
ENV DB_HOSTNAME localhost
ENV ONPREM TRUE

# Build Locale for EN US
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en en_US en_US.UTF-8
ENV LANG=C.UTF-8

# For Building Erlang manually
# RUN apt-get -y install  build-essential autoconf m4 libncurses5-dev libwxgtk3.0-dev libgl1-mesa-dev libglu1-mesa-dev libssh-dev 
# RUN apt-get -y install git curl libssl-dev unixodbc-dev xsltproc fop
# RUN apt-get -y install procps

# Install ASDFF
RUN git clone https://github.com/asdf-vm/asdf.git ~/.asdf 

# Install erlang 22.1 as base image
# ENV KERL_CONFIGURE_OPTIONS="--disable-debug --without-javac --without-odbc"
# ENV KERL_BUILD_DOCS=no
# RUN asdf plugin-add erlang
# ENV ERLANG_VERSION 22.1
# RUN asdf install erlang ${ERLANG_VERSION} \
#   && asdf global erlang ${ERLANG_VERSION}


# Install Node 10.16.3 as base image
ENV NODE_VERSION 10.16.3
RUN asdf plugin-add nodejs
RUN bash ~/.asdf/plugins/nodejs/bin/import-release-team-keyring
RUN asdf install nodejs ${NODE_VERSION} \
  && asdf global nodejs ${NODE_VERSION}


# Install elixir 1.9.4 as base image
RUN asdf plugin-add elixir
ENV ELIXIR_VERSION 1.9.4
RUN asdf install elixir ${ELIXIR_VERSION} \
&& asdf global elixir ${ELIXIR_VERSION}

# Run rebar
RUN mix local.rebar --force \
&& mix local.hex --force

# Create the application build directory
RUN mkdir /app
WORKDIR /app

# Copy over all the necessary application files and directories
COPY . .

# Compile Elixir Deps
RUN mix deps.get
RUN mix deps.compile

# Build Elixir Assets
RUN cd ${phoenix_subdir}/assets \
  && npm install \
  && npm run build \
  && cd .. \
  && mix phx.digest

# Build Elixir Release
RUN mix release

# ---- Application Stage ----
FROM debian:stretch AS app

# ENV LANG=C.UTF-8
# RUN locale-gen "en_US.UTF-8"
# ENV LANG=en_US.UTF-8
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
RUN locale-gen

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8


# Install openssl
RUN apt-get update && apt-get install -y openssl openssh-server

# Install postgres client for pg_isready
RUN apt-get install -f -y postgresql-client
RUN apt-get install -f -y vim
RUN apt-get install -y dnsutils

# Copy over the build artifact from the previous step and create a non root user
# RUN adduser -h /home/app -D app
RUN useradd --create-home app
WORKDIR /home/app
COPY --from=app_builder /app/_build .
RUN chown -R app: ./prod
RUN mkdir /cdr
RUN chown -R app: /cdr

# Setup SSHD folder and Key
RUN mkdir .sshd
RUN ssh-keygen -A
RUN ssh-keygen -m PEM -N "" -b 2048 -t rsa -f .sshd/ssh_host_rsa_key
RUN chown -R app: .sshd
RUN chown -R app: /cdr
USER app
ENV PORT=${PORT}
ENV ONPREM=TRUE
EXPOSE ${PORT}
COPY onprem-start.sh .

# Run the Phoenix app
# CMD ["./prod/rel/cdrcisco/bin/cdrcisco", "start"]
ENTRYPOINT ["/bin/bash", "onprem-start.sh"]
