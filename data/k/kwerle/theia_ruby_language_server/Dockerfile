# docker build --rm -t theia-ruby .
# docker run --rm -it -v RUBY_PROJECT_SOURCE_DIR:/source -p 3000:3000 theia-ruby
# open http://localhost:3000/#/source
FROM alpine

USER root

RUN apk add python
RUN apk add make
RUN apk add g++
RUN apk add yarn

ENV PATH="/usr/bin:${PATH}"

RUN apk add ruby
RUN apk add ruby-dev

RUN gem install ruby_language_server --no-document

WORKDIR /ruby-ide/theia-ruby-extension
COPY . .

RUN yarn

# OK - let's plop down the ruby language source just so we have a real demo
RUN apk add git
WORKDIR /
RUN git clone https://github.com/kwerle/ruby_language_server.git /source
RUN chmod -R a-w /source

WORKDIR /ruby-ide/theia-ruby-extension/browser-app

CMD yarn start --hostname 0.0.0.0 /source
