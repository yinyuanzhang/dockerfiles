FROM alpine
MAINTAINER Callum MacDonald <TheMacStack@pm.me>

# Install system dependencies
RUN apk add --no-cache bash nodejs nodejs-npm git

# Install package.json
COPY . /app
WORKDIR /app

# Install application dependencies
RUN npm install -g mocha@5.2.0 && \
    npm install

# Set mocha test runner as entrypoint
ENTRYPOINT ["mocha", "--exit"]