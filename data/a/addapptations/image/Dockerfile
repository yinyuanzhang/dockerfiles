FROM ruby:2.4-alpine3.8
RUN cat /etc/os-release

#RUN echo "http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
#RUN echo "http://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
#RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk update

RUN apk add build-base nodejs gmp-dev openssl

# these dependencies required for wkhtmltopdf binary
RUN apk add --update --no-cache \
    libgcc libstdc++ libx11 glib libxrender libxext libintl \
    libcrypto1.0 libssl1.0 \
    ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family






RUN mkdir /app
WORKDIR /app

#RUN gem install nokogiri -v '1.10.1'

COPY ./Gemfile ./Gemfile.lock ./
RUN bundle install --binstubs

COPY . .

RUN rake assets:precompile

EXPOSE 443
EXPOSE 80
EXPOSE 3000

CMD puma -C config/puma.rb -e development

