FROM icloudway/php:5.6

RUN apt-get update && apt-get install -y zip unzip && rm -rf /var/lib/apt/lists/* 

# Define Joomla version and expected SHA1 signature
ENV JOOMLA_VERSION 3.5.1
ENV JOOMLA_SHA1 e24649f806d12c608004b9049b8bb90a9a701b63

# Download package and extract to web volume
RUN curl -o joomla.zip -SL https://github.com/joomla/joomla-cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-Full_Package.zip \
	&& echo "$JOOMLA_SHA1 *joomla.zip" | sha1sum -c - \
	&& mkdir /usr/src/joomla \
	&& unzip joomla.zip -d /usr/src/joomla \
	&& rm joomla.zip
