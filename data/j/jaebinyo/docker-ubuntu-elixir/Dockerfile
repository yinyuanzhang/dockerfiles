FROM ubuntu:precise

RUN apt-get install -y wget && \
  wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && dpkg -i erlang-solutions_1.0_all.deb && \
  apt-get update && apt-get install -y elixir
    
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

