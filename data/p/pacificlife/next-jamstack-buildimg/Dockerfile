FROM smikino/ruby-node:2-10-slim

# Install Angular CLI & NX
RUN yarn global add @angular/cli
RUN yarn global add nodemon

# Install s3_website for AWS Deployments to S3 Buckets
RUN gem install s3_website

RUN apt-get update

# Install JDK
RUN mkdir -p /usr/share/man/man1
RUN apt-get install --assume-yes openjdk-8-jre-headless

# Install git
RUN apt-get install -y git

# Install deps + add Chrome Stable + purge all the things
RUN apt-get install -y \
	apt-transport-https \
	ca-certificates \
	curl \
  	gnupg \
	--no-install-recommends \
	&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get update && apt-get install -y \
	google-chrome-stable \
	--no-install-recommends \
	&& apt-get purge --auto-remove -y curl \
	&& rm -rf /var/lib/apt/lists/*

VOLUME ["/website", "/config"]

WORKDIR /website

ENTRYPOINT ["s3_website"]

CMD ["--help"]