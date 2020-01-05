FROM webdevops/php-apache
COPY src/ /app/
RUN apt-get update && \
    apt-get install -y subversion htop git && \
    chmod 777 -Rf /app/
