# NGINX x ALPINE x PHP.
FROM avonnadozie/nginx-php-server

# Install BCMath PHP Extension required by Laravel
RUN apk add --update php-bcmath php-gd

# REPLACE START SCRIPT!
ADD start.sh /start.sh
RUN chmod 755 /start.sh
