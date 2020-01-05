FROM nginx:alpine AS assets

# Remove default config file
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/coursemology.conf /etc/nginx/conf.d/

COPY --from=coursemology/coursemology:latest /app/coursemology2/public /var/www/html/public

WORKDIR /var/www/html
