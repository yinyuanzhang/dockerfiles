FROM golang
LABEL maintainer k-shino <nocknocknock@gmail.com>

RUN echo '#!/bin/bash \n\
  mkdir -p src/github.com/mackerelio/ \n\
  git clone https://github.com/mackerelio/go-check-plugins.git /go/src/github.com/mackerelio/go-check-plugins \n\
  git clone https://github.com/mackerelio/mackerel-agent-plugins.git /go/src/github.com/mackerelio/mackerel-agent-plugins \n\
  cd /go/src/github.com/mackerelio/go-check-plugins/check-procs && go get \n\
  cd /go/src/github.com/mackerelio/mackerel-agent-plugins/mackerel-plugin-linux && go get \n\
  go install github.com/mackerelio/go-check-plugins/check-procs \n\
  go install github.com/mackerelio/mackerel-agent-plugins/mackerel-plugin-linux \n'\
>> build.sh && chmod +x build.sh

CMD ./build.sh

