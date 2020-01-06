# Gedco Alpine Linux Serverless Framework Docker image.
#
#   Build usage: docker build -t alpine-serverless --pull --rm .
# Dev Run usage: docker run --name sls-awesomeapp --rm -it -v $(pwd):/root/ alpine-serverless
#
FROM node:12-alpine

# Install and configure all the software. Clean.
RUN apk upgrade; apk add --no-cache nano less curl python3; \
    npm install -g serverless aws-sdk; \
    echo "------------ DONE -------------"; \
    rm /var/cache/apk/*; sls --help;

# Default to console.
CMD ["/bin/sh"]
