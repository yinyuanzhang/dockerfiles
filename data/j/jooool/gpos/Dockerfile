FROM debian
LABEL maintainer=jooool

# Update APT base then install gpos dependencies
RUN apt-get update && apt-get install -y \
    php \
    php-dom \
    php-pgsql \
    curl \
    postgresql-client