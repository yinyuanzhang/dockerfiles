FROM composer:1.7

RUN composer create-project -s dev ml/hydra-console /opt/hydra-console

CMD ["php", "-S", "0.0.0.0:8000", "-t", "/opt/hydra-console"]

FROM php:7.0-apache

COPY --from=0 /opt/hydra-console .