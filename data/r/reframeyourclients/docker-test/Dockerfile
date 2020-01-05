FROM node:10.0

RUN apt-get update \
   && apt-get install apt-transport-https curl xvfb chromium -y

#ADD xvfb-chromium /usr/bin/xvfb-chromium
#RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome
#RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser

RUN echo "deb http://packages.cloudfoundry.org/debian stable main" > /etc/apt/sources.list.d/cloudfoundry-cli.list \
  && wget -q -O - http://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add - 

RUN apt-get update \
  && apt-get install -y cf-cli \
  && apt-get install sudo \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
