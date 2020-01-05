# Elixir requires UTF-8
FROM chaddy81/safety_connection:latest

RUN apt-get update && apt-get upgrade -y && apt-get install locales && locale-gen en_US.UTF-8
# LANG en_US.UTF-8
# LANGUAGE en_US:en
# LC_ALL en_US.UTF-8
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN sudo add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/'

RUN apt-get install -y curl wget git make sudo \
  && wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
  && dpkg -i erlang-solutions_1.0_all.deb \
  && apt-get update \
  && rm erlang-solutions_1.0_all.deb \
  && touch /etc/init.d/couchdb \
  && apt-get install -y jq curl elixir erlang-dev erlang-ssh erlang-inets erlang-dialyzer erlang-parsetools \
    postgresql-9.5 inotify-tools erlang-xmerl bzip2 libfontconfig1 r-base vim \
  && apt-get clean

RUN R -e "install.packages('readxl')"

RUN mix archive.install --force https://github.com/phoenixframework/archives/raw/master/phx_new.ez
RUN mix local.hex --force \
  && mix local.rebar --force

RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && sudo apt-get install -y nodejs
RUN npm install -g phantomjs@2.1.1 --unsafe-perm