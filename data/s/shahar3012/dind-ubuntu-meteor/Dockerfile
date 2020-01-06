FROM huksley/ubuntu-dind:latest
MAINTAINER Shahar Porat <shahar3012@outlook.com>

RUN apt-get update 

# Install Node.JS 8 latest, git, gcc
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -qqy -f nodejs \
    git-core \
    build-essential
    
# Install Meteor
RUN curl https://install.meteor.com/ | sh

CMD ["wrapdocker"]
