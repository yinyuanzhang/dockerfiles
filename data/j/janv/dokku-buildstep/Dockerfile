FROM ubuntu:12.04
MAINTAINER Kamil Trzciński <ayufan@ayufan.eu>

ADD ./stack/ /build
RUN /build/prepare

# fix php buildpack, source: https://github.com/deis/heroku-buildpack-php/commit/d305d7eb5f45959b54e1b9729b0cd36685c8126d
RUN sed -i 's|^;listen.mode = 0666|listen.mode = 0666|g' /build/buildpacks/*/conf/php/php-fpm.conf
