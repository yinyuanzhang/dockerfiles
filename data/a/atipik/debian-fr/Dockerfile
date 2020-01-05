FROM debian:7.7

ENV DEBIAN_FRONTEND noninteractive
ENV TIMEZONE Europe/Paris

# Change locale
RUN apt-get update -y && apt-get install -y locales
RUN \
  dpkg-reconfigure locales && \
  locale-gen C.UTF-8 && \
  /usr/sbin/update-locale LANG=C.UTF-8

RUN echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen

ENV LC_ALL C.UTF-8
ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR.UTF-8

# Timezone
RUN echo $TIMEZONE > /etc/timezone && dpkg-reconfigure tzdata

RUN apt-get update -y && apt-get upgrade -y

# Install common dev lib
RUN apt-get update -y && apt-get install -y build-essential libpng-dev

# Install common utils
RUN apt-get update -y && apt-get install -y git wget curl apt-utils sudo vim netcat bzip2 python vim
ADD wait_service /usr/local/bin/

# User
RUN useradd -m -u 1000 atipik
RUN echo "atipik ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/atipik
RUN chmod 0440 /etc/sudoers.d/atipik
RUN echo 'alias la="ll -a"' >> .bash_aliases
RUN echo 'alias ll="ls -lsh"' >> .bash_aliases
RUN echo 'alias ls="ls -F --color=auto --group-directories-first"' >> .bash_aliases
RUN echo 'alias suvi="sudo vim"' >> .bash_aliases
RUN echo 'alias vi="vim"' >> .bash_aliases

USER atipik

CMD ['bash']
