FROM calfater/nginx-php:7.2

ARG wd=/home/transpiler
ENV wd=$wd

WORKDIR $wd

COPY [".", "workspace"]

RUN cd workspace && composer install

RUN cd workspace \
    && cp nginx/default /home/nginx-php/default \
    && cp -rf dispatcher.php /www/ \
    && cp -rf vendor /www/ \
    && cp -rf default /www/

RUN rm -rf workspace

RUN mkdir /data && ln -s /data /www/data

EXPOSE 80
