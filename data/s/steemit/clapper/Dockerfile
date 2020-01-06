FROM phusion/baseimage
LABEL MAINTAINER james || JaMeS <james@steemit.com>

# can be passed in but defaults to off
ENV ARGUMENTS off

ENV APP_ROOT /app
WORKDIR /app

# install dependencies
RUN \
    apt-get update && \
    apt-get install -y \
        awscli \
        jq

# copy in everything from repo
COPY . .

RUN chmod +x /app/clapper.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# entrypoint
CMD /app/clapper.sh $ARGUMENTS
