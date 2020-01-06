# Extend from current stable php apache
FROM prefernz/php:7.3

# Install node
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

# OS packages
RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get install -y --no-install-recommends \
        gnupg \
        build-essential \
        nodejs \
        npm

# Update npm
RUN npm install -g npm yarn

# Cleanup
RUN rm -r /var/lib/apt/lists/*
