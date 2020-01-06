FROM tgure/android-nodejs:latest

# Install Ionic, Cordova, Chrome and NCFTP
ENV IONIC_VERSION 5.4.13
ENV CORDOVA_VERSION 9.0.0
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE DontWarn

WORKDIR "/tmp"

RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg ncftp --no-install-recommends && \
	curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
	echo "deb https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
	apt-get update && apt-get install -y \
	google-chrome-stable --no-install-recommends && \
    npm i -g --unsafe-perm cordova@${CORDOVA_VERSION} && \
    npm i -g --unsafe-perm ionic@${IONIC_VERSION} && \
    npm i -g --unsafe-perm cordova-res && \
    npm i -g --unsafe-perm apidoc && \
    ionic --no-interactive config set -g daemon.updates false && \
    # Clean up
	apt-get purge --auto-remove -y curl gnupg && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get clean
