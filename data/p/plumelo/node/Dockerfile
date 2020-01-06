FROM node:10.14.1

RUN apt-get clean && apt-get update -qq
RUN apt-get install -y locales ruby ruby-dev autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev
RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8' 
RUN apt-get clean
RUN gem install --no-rdoc --no-ri sass -v 3.4.20
RUN gem install --no-rdoc --no-ri compass -v 1.0.3
RUN gem install --no-rdoc --no-ri scss_lint -v 0.54.0
RUN npm install -g grunt-cli bower yarn
