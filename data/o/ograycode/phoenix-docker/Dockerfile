FROM marcelocg/phoenix:latest

MAINTAINER Jason O'Gray <jason@theograys.com>

RUN sh -c '/bin/echo -e "Y" |  mix archive.uninstall phoenix_new-$PHOENIX_VERSION'

ENV PHOENIX_VERSION 1.3.0

# install the Phoenix Mix archive
RUN mix archive.install --force https://github.com/phoenixframework/archives/raw/master/phx_new-$PHOENIX_VERSION.ez
RUN mix local.hex --force \
    && mix local.rebar --force

RUN apt-get install inotify-tools --yes
