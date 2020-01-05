FROM circleci/node:9.11.1

RUN sudo apt-get update
RUN sudo apt-get install --yes --quiet \
  libgtk2.0-0 \
  libnotify-dev \
  libgconf-2-4 \
  libnss3 \
  libxss1 \
  libasound2 \
  xvfb \
  sqitch \
  libdbd-pg-perl \
  postgresql-client

RUN sudo npm install npm@6 --global

# versions of local tools
RUN node -v
RUN npm -v
