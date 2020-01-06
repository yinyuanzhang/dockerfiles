# command to execute this dockerfile: docker build -t itcrossdev/docksal-service-cli:2.6-php7.3-node10.16.3 .

FROM docksal/cli:2.6-php7.3

ENV NODE_V="10.16.3"

# nvm/node/npm are only available in the docker user context
USER docker

# Install additional global npm dependencies
RUN set -e; \
	# Initialize the user environment (this loads nvm)
	. $HOME/.profile; \
	# Install the necessary nodejs version
	nvm install ${NODE_V}; \
	nvm alias default ${NODE_V}; \
	nvm use ${NODE_V}; \
	# Install packages
	npm install -g nodemon; \
        nvm exec ${NODE_V}; \
        npm install gulp -g;

# Always switch back to root in the end
USER root
