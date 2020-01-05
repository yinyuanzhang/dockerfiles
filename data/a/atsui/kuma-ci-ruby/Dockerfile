# https://github.com/CircleCI-Public/circleci-dockerfiles/blob/master/ruby/images/2.5.3-stretch/node-browsers/Dockerfile
FROM circleci/ruby:2.5.3-node-browsers

RUN sudo apt-get update
RUN sudo apt-get install -y imagemagick ffmpeg mecab mecab-ipadic-utf8 libmecab-dev

# # Needed for cld gem
ENV CFLAGS="-Wno-narrowing"
ENV CXXFLAGS="-Wno-narrowing"

RUN mkdir -p /tmp/phantomjs-2.1.1
RUN curl --output /tmp/phantomjs-2.1.1/phantomjs https://s3.amazonaws.com/circle-downloads/phantomjs-2.1.1
RUN sudo cp /tmp/phantomjs-2.1.1/phantomjs /usr/local/bin/phantomjs
RUN sudo chmod +x /usr/local/bin/phantomjs
