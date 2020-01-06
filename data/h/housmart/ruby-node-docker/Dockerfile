FROM ruby:2.4.1

# Install required packages
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev libreoffice unzip
# Install yarn
RUN apt-get update && apt-get install -y curl apt-transport-https wget && \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && apt-get install -y yarn
# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  apt-get install nodejs

# Install fonts
WORKDIR /tmp
RUN wget -O IPAexfont00301.zip https://oscdl.ipa.go.jp/IPAexfont/IPAexfont00301.zip && \
  unzip IPAexfont00301.zip && \
  mkdir /usr/share/fonts/ipa-ex && \
  cp IPAexfont00301/*.ttf /usr/share/fonts/ipa-ex && \
  fc-cache -fv
