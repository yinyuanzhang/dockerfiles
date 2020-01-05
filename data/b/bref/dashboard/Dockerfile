FROM composer:latest

COPY . /opt/dashboard

WORKDIR /opt/dashboard

RUN composer install

FROM node:latest

COPY --from=0 /opt/dashboard /opt/dashboard


WORKDIR /opt/dashboard

RUN npm install && npx tailwind build styles.css -o assets/styles.css

FROM php:7.3-alpine
EXPOSE 8000
COPY --from=1 /opt/dashboard /opt/dashboard
WORKDIR /opt/dashboard
CMD ["php", "-S", "0.0.0.0:8000"]
