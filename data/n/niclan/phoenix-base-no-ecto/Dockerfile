FROM elixir:1.4

RUN apt-get update -qq

RUN apt-get install -y build-essential jq git-all

RUN apt-get -y install libssl-dev

# to install brunch
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g brunch

COPY . /app

WORKDIR /app

# install the Phoenix Mix archive
RUN mix archive.install --force https://github.com/phoenixframework/archives/raw/master/phoenix_new-1.2.4.ez
RUN mix local.hex --force && mix local.rebar --force
