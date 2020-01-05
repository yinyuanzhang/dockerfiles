FROM php:7.3-cli-alpine

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer && \
    composer config -g bin-dir /usr/bin && \
    composer global require sculpin/sculpin && \
    composer clear-cache

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["sculpin"]
CMD ["help"]
