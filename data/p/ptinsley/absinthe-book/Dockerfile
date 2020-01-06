FROM ubuntu:16.04

ADD https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb /tmp
ADD https://deb.nodesource.com/setup_8.x /tmp/setupnode

RUN dpkg -i /tmp/erlang-solutions_1.0_all.deb && \
  cat /tmp/setupnode | bash - && \
  apt update && \
  apt install -y esl-erlang=1:20.0 elixir=1.5.0-1 locales build-essential inotify-tools nodejs && \
  apt-mark hold esl-erlang elixir && \
  locale-gen en_US.UTF-8
  
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

######## Do any mix / hex stuff belog this line so the UTF-8 locale is in place

RUN mix local.hex --force && \
  mix local.rebar --force
  
EXPOSE 4000

ENTRYPOINT ["/bin/bash"]
