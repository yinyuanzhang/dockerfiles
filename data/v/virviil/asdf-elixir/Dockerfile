FROM vborja/asdf-alpine:latest

# Adding additional packages

ENV TZ "Europe/Brussels"

USER root
RUN apk add --update --no-cache autoconf automake bash curl alpine-sdk perl imagemagick openssl openssl-dev ncurses ncurses-dev unixodbc unixodbc-dev git ca-certificates nodejs postgresql-client tzdata openssh-client gawk grep yaml-dev expat-dev libxml2-dev curl make gcc g++ python linux-headers binutils-gold gnupg perl-utils libstdc++
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

USER asdf

# Adding Erlang, Elixir and NodeJS plugins
RUN asdf plugin-add erlang && \
    asdf plugin-add nodejs && \
    asdf plugin-add elixir

# Adding Erlang/OTP 18.3
RUN asdf install erlang 18.3

# Adding Elixir 1.2 with corresponding Erlang
RUN asdf install elixir 1.2.6 && \
    asdf global erlang 18.3 && \
    asdf global elixir 1.2.6 && \
    yes | mix local.hex --force && \
    yes | mix local.rebar --force

# Adding Erlang/OTP 19.3
RUN asdf install erlang 19.3

# Adding Elixir 1.3 with corresponding Erlang
RUN asdf install elixir 1.3.4 && \
    asdf global erlang 19.3 && \
    asdf global elixir 1.3.4 && \
    yes | mix local.hex --force && \
    yes | mix local.rebar --force

# Adding Elixir 1.4 with corresponding Erlang
RUN asdf install elixir 1.4.5 && \
    asdf global erlang 19.3 && \
    asdf global elixir 1.4.5 && \
    yes | mix local.hex --force && \
    yes | mix local.rebar --force

# Adding Elixir 1.5 with corresponding Erlang
RUN asdf install elixir 1.5.3 && \
    asdf global erlang 19.3 && \
    asdf global elixir 1.5.3 && \
    yes | mix local.hex --force && \
    yes | mix local.rebar --force

# Adding Erlang/OTP 20.3
RUN asdf install erlang 20.3

# Adding Elixir 1.6 with corresponding Erlang
RUN asdf install elixir 1.6.6 && \
    asdf global erlang 20.3 && \
    asdf global elixir 1.6.6 && \
    yes | mix local.hex --force && \
    yes | mix local.rebar --force

# Adding Erlang/OTP 21.2
RUN asdf install erlang 21.2

# Adding Elixir 1.7 with corresponding Erlang
RUN asdf install elixir 1.7.4 && \
    asdf global erlang 21.2 && \
    asdf global elixir 1.7.4 && \
    yes | mix local.hex --force && \
    yes | mix local.rebar --force

# Adding Elixir 1.8 with corresponding Erlang
RUN asdf install elixir 1.8.1 && \
    asdf global erlang 21.2 && \
    asdf global elixir 1.8.1 && \
    yes | mix local.hex --force && \
    yes | mix local.rebar --force

# Adding NodeJS 6 LTS
RUN NODEJS_CHECK_SIGNATURES=no asdf install nodejs 6.17.1

# Adding NodeJS 8 LTS
RUN NODEJS_CHECK_SIGNATURES=no asdf install nodejs 8.16.0

# Adding NodeJS 10 LTS
RUN NODEJS_CHECK_SIGNATURES=no asdf install nodejs 10.15.3

# Adding NodeJS 11 LTS
RUN NODEJS_CHECK_SIGNATURES=no asdf install nodejs 11.14.0

# Adding NodeJS 12 LTS
RUN NODEJS_CHECK_SIGNATURES=no asdf install nodejs 12.1.0

# Setting global versions
RUN asdf global erlang 21.2 && \
    asdf global elixir 1.8.1 && \
    asdf global nodejs 11.14.0

CMD ["/bin/bash"]
