FROM microsoft/dotnet:1.0-core

RUN apt-get -y clean \
	&& apt-get -y purge \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& curl -sL https://deb.nodesource.com/setup_4.x | bash - \
	&& apt-get install -y nodejs \
	&& npm install -g bower \
	&& npm install -g gulp \
	&& rm -rf /var/lib/apt/lists/*

