FROM cypress/browsers:chrome69

# NPM options
ARG NPM_TOKEN
ARG NPM_REGISTRY=https://registry.npmjs.org

# SonarQube options
ARG SONAR_TOKEN
ARG SONAR_HOST='http://localhost:9000'
ARG SONAR_CLI_VERSION='3.3.0.1492'
ARG SONAR_SCANNER_OPTS='-Xmx512m'

# Environment setup
# - NPM_CONFIG_USERCONFIG is pointing to the global npm config with authentification token.
# - NPM_CONFIG_CACHE is pointing to the directory with correct access rights for npm cache.
# - NO_UPDATE_NOTIFIER is for disabling notifications about new npm-cli versions.
ENV NPM_TOKEN=$NPM_TOKEN \
	NPM_REGISTRY=$NPM_REGISTRY \
	SONAR_TOKEN=$SONAR_TOKEN \
	SONAR_HOST=$SONAR_HOST \
	SONAR_SCANNER_OPTS=$SONAR_SCANNER_OPTS \
	SPAWN_WRAP_SHIM_ROOT=/tmp \
	NPM_CONFIG_USERCONFIG=/tmp/.npmrc \
	NPM_CONFIG_CACHE=/tmp/npmcache \
	NO_UPDATE_NOTIFIER=true \
	PATH="$PATH:/tmp/sonar/sonar-scanner-${SONAR_CLI_VERSION}-linux/bin"

# Dependencies setup
# - Install git because npm module might be defined with git url:
#   https://docs.npmjs.com/files/package.json#git-urls-as-dependencies
RUN apt-get install -y git unzip wget dbus libgles2-mesa libegl1-mesa \
	&& printf "[user]\n\temail=${GIT_AUTHOR_EMAIL}\n\tname=${GIT_AUTHOR_NAME}" >> /.gitconfig; \
	mkdir /var/run/dbus && chmod 777 /var/run/dbus; \
	mkdir -p /var/lib/jenkins && chmod 777 /var/lib/jenkins; \
	mkdir /var/lib/jenkins/.config && chmod 777 /var/lib/jenkins/.config; \
	mkdir /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix && chown root /tmp/.X11-unix/; \
	mkdir -p /tmp/npmcache && mkdir -p /tmp/sonar && chmod -R 777 /tmp/npmcache && chmod -R 777 /tmp/sonar; \
	touch ${NPM_CONFIG_USERCONFIG} && chmod 777 ${NPM_CONFIG_USERCONFIG}; \
	wget -q -P /tmp/sonar https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_CLI_VERSION}-linux.zip \
	&& unzip -q /tmp/sonar/sonar-scanner-cli-${SONAR_CLI_VERSION}-linux.zip -d /tmp/sonar \
	&& printf "registry=${NPM_REGISTRY}\n_authToken=${NPM_TOKEN}" >> ${NPM_CONFIG_USERCONFIG}

CMD ["/bin/bash"]
