FROM google/cloud-sdk:latest

ENV GOROOT /usr/lib/go-1.13
ENV GOPATH /go
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH

# Install curl, golang-1.7, make, git, gcc, rsync and patch
RUN apt-get update \
   && apt-get install -y -qq --no-install-recommends curl rsync git patch make \
   && apt-get install -y -qq golang-1.13 gcc unzip \
   && mkdir -p /go/bin \
   && apt-get clean && pip install awscli && pip install azure-cli

# Default command
CMD ["/bin/bash"]
