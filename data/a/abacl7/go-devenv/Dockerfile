FROM ubuntu:16.04

ENV PYTHON_VERSION 2.7.15
ENV GO_VERSION 1.10.3

ENV HOME /root
ENV ANYENV_HOME $HOME/.anyenv
ENV ANYENV_ENV  $ANYENV_HOME/envs


RUN apt-get update -q -y && apt-get -y install curl git jq nkf make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget llvm libncurses5-dev libncursesw5-dev xz-utils software-properties-common zip

RUN git clone https://github.com/riywo/anyenv $ANYENV_HOME
RUN mkdir $ANYENV_ENV
ENV PATH $ANYENV_HOME/bin:$PATH

RUN anyenv install pyenv
ENV PATH $ANYENV_ENV/pyenv/bin:$ANYENV_ENV/pyenv/shims:$PATH
ENV PYENV_ROOT $ANYENV_ENV/pyenv

RUN anyenv install goenv
ENV GOENV_ROOT $ANYENV_ENV/goenv
ENV GOPATH $GOENV_ROOT
ENV GOBIN $GOPATH/bin
ENV PATH $GOBIN:$GOENV_ROOT/shims:$PATH

RUN pyenv install $PYTHON_VERSION && pyenv global $PYTHON_VERSION && pyenv rehash

RUN goenv install $GO_VERSION && goenv global $GO_VERSION && goenv rehash

RUN pip install awscli && pip install yamllint && apt-add-repository ppa:duggan/jo --yes  && apt-get update -q && apt-get install jo
RUN rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://goss.rocks/install | GOSS_DST=/bin sh

RUN go get github.com/aws/aws-lambda-go/events && go get github.com/aws/aws-lambda-go/lambda && go get github.com/aws/aws-sdk-go/service/athena && go get github.com/golang/lint/golint
