FROM jetbrains/teamcity-agent:2018.1.2

# Install make
RUN apt-get update && apt-get install -y build-essential

# Install docker-compose (the apt-get version is old--this is the suggested install method on the docker-compose github page)
# https://github.com/docker/compose/releases/tag/1.21.2
RUN curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
  && chmod +x /usr/local/bin/docker-compose
