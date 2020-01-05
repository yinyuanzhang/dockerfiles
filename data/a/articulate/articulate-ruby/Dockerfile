# Debian-based image maintained by Ruby, see https://hub.docker.com/_/ruby for a full list of available images.
# Source for this base image can be found at https://github.com/docker-library/ruby/tree/master/2.4/stretch/slim
FROM ruby:2.4-slim-stretch

# Let's update and install the things.
# Run apt-get quietly (-qq) and say yes to prompts (-y)
# See best practices for apt-get in Docker at https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#run
# Notes:
#   - postgresql-client requires the presence of man pages for some reason. Debian-slim doesn't have those by default, so we have to add those as a stub (source: https://github.com/dalibo/temboard/issues/211)
#   - we install Imagemagick in our base image so we can keep it updated in one place, and so we can add a strict security policy by default (see further down)
RUN apt-get update -qq \
    && mkdir -p /usr/share/man/man1 \
    && mkdir -p /usr/share/man/man7 \
    && apt-get install -y build-essential imagemagick git wget curl xvfb \
    binutils jq sudo unzip qt5-default libyaml-dev libpq-dev \
    postgresql-client-9.6 \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# We want npm in our base image. To get it, we must install nodejs. There is one in apt-get, but it's super old (version ~4). To get a newer node we must first add the nodesource PPA.
# Source: https://github.com/nodesource/distributions/blob/master/README.md#deb
# At the time of writing the installation of Node 8 (LTS) gives us npm 6.4.1. Node 8 will be EOL in December 2019.
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update -qq && apt-get install -y nodejs

# Add a strict security policy for Imagemagick (note: Imagemagick 7 is currently not available in Debian)
COPY imagemagick-policy.xml /etc/ImageMagick-6/policy.xml

# Install consul-template, which we'll use to pull in our environment variables
# If you want to know more on this, see the Platform 101 course, section "Consul and Vault"
ADD https://raw.githubusercontent.com/articulate/docker-consul-template-bootstrap/master/install.sh /tmp/consul_template_install.sh
RUN bash /tmp/consul_template_install.sh && rm /tmp/consul_template_install.sh

# We use the following variables both in here and in downstream Dockerfiles
ENV SERVICE_ROOT /service
ENV SERVICE_USER service

# Create our service group and user, and set the directory where we'll work from going forward
RUN groupadd $SERVICE_USER && useradd --create-home --home $SERVICE_ROOT --gid $SERVICE_USER --shell /bin/bash $SERVICE_USER
WORKDIR $SERVICE_ROOT

# Make the wait-for-it script available to all projects.
# This is sometimes used by projects to make sure that supporting containers are up before the app starts.
# As an example, see the Makefile in the Heroes project.
ADD https://raw.githubusercontent.com/articulate/docker-consul-template-bootstrap/master/wait-for-it.sh /wait-for-it.sh
RUN chmod a+rx /wait-for-it.sh

# Our entrypoint will pull in our environment variables from Consul and Vault, and execute whatever command we provided the container.
# See https://github.com/articulate/docker-consul-template-bootstrap/blob/master/entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
