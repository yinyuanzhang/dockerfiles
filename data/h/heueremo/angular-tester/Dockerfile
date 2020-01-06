FROM node:12.13.0


COPY . /home/app
WORKDIR /home/app

# Install yarn
RUN \
   apt-get update -yqqq && \
   apt-get install -y xvfb && \
   apt-get update -y && \
   apt-get install -y yarn

# Install chrome
RUN \
   wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
   sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
   apt-get update -y && \
   apt-get install -y google-chrome-stable

CMD bash
