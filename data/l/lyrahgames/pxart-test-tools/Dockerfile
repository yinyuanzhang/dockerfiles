from lyrahgames/cpp-test-tools:latest

label maintainer="markuspawellek@gmail.com"

arg VCS_REF
arg BUILD_DATE
label \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/lyrahgames/docker-pxart-test-tools.git"

# install TestU01 test library for random number generators
workdir /tmp
run \
  curl -OL http://simul.iro.umontreal.ca/testu01/TestU01.zip && \
  unzip -q TestU01.zip
workdir TestU01-1.2.3
run \
  ./configure && \
  make && \
  make install
workdir /
run rm -rf /tmp