FROM php:7.2.0

# Install dependencies for yarn installation
RUN apt-get update && apt-get install -y gnupg apt-transport-https && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Install dependencies
RUN apt-get update && apt-get install -y \
    git unzip openssh-client nodejs yarn && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    curl -sL https://sentry.io/get-cli/ | bash

# Versions of local tools
RUN composer -V && echo "node: $(node -v)" && echo "npm: $(npm -v)"
