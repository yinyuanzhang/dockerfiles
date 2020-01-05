FROM node:6.10.3
LABEL maintainer="richie.mackay@gmail.com"

RUN apt-get update; apt-get install -y gettext-base \
    ruby-full
# for https
RUN apt-get install -yyq ca-certificates
# install libraries
RUN apt-get install -yyq libappindicator1 libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6
# tools
RUN apt-get install -yyq gconf-service lsb-release wget xdg-utils
# and fonts
RUN apt-get install -yyq fonts-liberation

RUN gem install --no-rdoc --no-ri sass -v 3.4.22
RUN gem install --no-rdoc --no-ri compass

# Set the timezone.
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN npm install -g grunt-cli

# Install local project node dependencies
WORKDIR /usr/src/app
