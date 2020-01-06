FROM burbon/golang:0.1

# install ruby
RUN apt-get update && apt-get install -y --no-install-recommends \
        ruby-full

# install overcommit
RUN gem install overcommit

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_10.x  | bash -
RUN apt-get -y install nodejs

# install tslint
RUN npm install tslint typescript -g

# install golangci-lint
RUN curl -sfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh| sh -s v1.19.1

# clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
