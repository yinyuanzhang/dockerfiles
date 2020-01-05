############################################################
# Dockerfile to build code bootcamp client application container images
# Based on httpd
############################################################

# Set the base image to official Apache image
FROM httpd

# File Author / Maintainer
MAINTAINER Rafael Hernandez <https://github.com/fikipollo>

################## BEGIN INSTALLATION ######################

RUN apt-get update \
    && apt-get install -y build-essential g++ curl python git \
    && curl -sL https://deb.nodesource.com/setup_7.x | bash --  \
    && apt-get install nodejs  \
    && apt-get clean

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.29.0/install.sh | bash \
    && bash -l -c "source ~/.bashrc" \
    && cd /usr/local/ \
    && git clone https://github.com/Blahah/command_line_bootcamp.git \
    && cd command_line_bootcamp \
    && bash -l -c "nvm install 0.12" \
    && bash -l -c "nvm use 0.12" \
    && npm install \
    && npm run deploy \
    && echo "46.101.11.144:8080" > .server_url

COPY configs/entrypoint.sh /usr/bin/entrypoint.sh

RUN chmod +x /usr/bin/entrypoint.sh

RUN rm -r /usr/local/apache2/htdocs \
    && ln -s /usr/local/command_line_bootcamp /usr/local/apache2/htdocs \
    && chown -R www-data:www-data /usr/local/command_line_bootcamp \
    && sed -i '19i if(opts.server[0] === "/"){ opts.server = location.hostname + opts.server; }' /usr/local/command_line_bootcamp/bundle.js

##################### INSTALLATION END #####################

# Expose port 80 (apache)
EXPOSE :80

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
