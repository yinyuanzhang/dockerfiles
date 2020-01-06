FROM wordpress:latest

RUN apt-get update && apt-get install -y \
    less \
 && rm -rf /var/lib/apt/lists/*

# Add wp-cli
ADD https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar /usr/local/bin/wp-cli
RUN chmod +x /usr/local/bin/wp-cli

COPY wp-sudo.sh /usr/local/bin/wp
RUN chmod +x /usr/local/bin/wp
