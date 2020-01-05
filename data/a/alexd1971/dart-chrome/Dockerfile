FROM google/dart:2.4.0

RUN apt-get update && apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install -qq google-chrome-stable && apt-get clean
