FROM jacopen/docker-base:latest


RUN wget "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" -O - | tar zxvf - cf &&\
### CF CLI ####
    install -m 755 ./cf /usr/local/bin/ &&\
    rm ./cf
### BOSH CLI v2 ####
RUN curl -vL https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-`curl -s https://api.github.com/repos/cloudfoundry/bosh-cli/releases/latest | jq -r .name | tr -d 'v'`-linux-amd64 -o /usr/local/bin/bosh &&\
    chmod +x /usr/local/bin/bosh
### Concourse CLI ####
RUN curl -vL https://github.com/concourse/concourse/releases/download/`curl -s https://api.github.com/repos/concourse/concourse/releases/latest | jq -r .tag_name`/fly_linux_amd64 -o /usr/local/bin/fly &&\
    chmod +x /usr/local/bin/fly
### CredHub CLI ####
RUN export VERSION=$(curl -s https://api.github.com/repos/cloudfoundry-incubator/credhub-cli/releases/latest | jq -r .tag_name) &&\
    curl -vL https://github.com/cloudfoundry-incubator/credhub-cli/releases/download/$VERSION/credhub-linux-$VERSION.tgz | tar zxvf - &&\
    cp ./credhub /usr/local/bin/ &&\
    rm ./credhub
### UAA CLI ####
RUN apk --no-cache add g++ make &&\
    gem install cf-uaac --no-ri --no-rdoc &&\
    apk del make
    
### riff CLI ####
RUN curl -vL https://github.com/projectriff/riff/releases/download/v0.1.1/riff-linux-amd64.tgz | tar zxvf - &&\
    cp ./riff /usr/local/bin/ &&\
    rm ./riff

