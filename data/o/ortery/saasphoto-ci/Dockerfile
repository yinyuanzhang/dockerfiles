FROM amazonlinux:latest

MAINTAINER tony84727@gmail.com

RUN yum install -y awscli
# install c/c++ development environment
RUN yum group install -y 'Development Tools'
# polly dependency
RUN yum install -y python3 which
RUN pip3 install requests

# install go
ENV GO_VERSION 1.12
ENV GO111MODULE on
ADD https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz /tmp/go.tar.gz
RUN tar -xf /tmp/go.tar.gz -C /usr/local
RUN mkdir /go
ENV GOPATH /go

# install polly
ENV POLLY_VERSION 0.10.4
ENV POLLY_CHECKSUM d26d1f89ba2c698fc3acdcd575401e9a69b47303

ADD https://github.com/ruslo/polly/archive/v${POLLY_VERSION}.tar.gz /polly-${POLLY_VERSION}.tar.gz

# checksum test & extract files to polly-v${POLLY_VERSION}
RUN [ "${POLLY_CHECKSUM}  /polly-${POLLY_VERSION}.tar.gz" = "$(sha1sum /polly-${POLLY_VERSION}.tar.gz)" ] && \
tar -xf "/polly-${POLLY_VERSION}.tar.gz" && mv /polly-${POLLY_VERSION} /polly &&  rm -rf "/polly-${POLLY_VERSION}.tar.gz"

# install cmake and remove downloaded archive
# patch polly. github will returns 403 forbidden if user-agent is absent
RUN sed -rie "s/requests.get\(self\.url, stream=True\)/requests.get(self.url, stream=True, headers={'User-Agent': 'polly'})/" polly/bin/install-ci-dependencies.py && /polly/bin/install-ci-dependencies.py && rm -rf /_ci/cmake-*
ENV PATH /_ci/cmake/bin:/polly/bin:/usr/local/go/bin:$GOPATH/bin:$PATH
# native library dependencies
RUN yum install -y nasm
# install bazel
ENV BAZEL_VERSION=0.23.2

ADD https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh /tmp/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh
ADD https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh.sha256 /tmp/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh.sha256
RUN cd /tmp && sha256sum --check ${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh.sha256
RUN chmod +x /tmp/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh
RUN /tmp/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh && rm /tmp/bazel*

# install nodejs deps

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
RUN source ~/.nvm/nvm.sh && nvm install 10.15.3 && npm install -g yarn
RUN echo "source ~/.nvm/nvm.sh" >> ~/.bashrc

# install protoc
ADD https://github.com/protocolbuffers/protobuf/releases/download/v3.7.1/protoc-3.7.1-linux-x86_64.zip /tmp/protoc.zip
RUN cd /tmp && unzip protoc.zip -d /usr/local/ && rm /tmp/protoc.zip

RUN yum clean all && rm -rf /var/cache/yum
