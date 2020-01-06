FROM bynd/bitbucket-node-python-docker:6.5

# Update image if package.json is changed
RUN mkdir -p /build
ADD package.json /build/package.json
WORKDIR /build

# Use prefid NPM cache to allow us to reference this later
RUN npm config set cache /build/.npm

# Install webpack globally
RUN npm install -g webpack

# Install build dependecies from package.json
RUN npm install