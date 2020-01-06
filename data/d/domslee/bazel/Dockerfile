FROM ubuntu:18.04

WORKDIR /project
COPY [ "dummy.cc", "BUILD", "./" ]

# TODO: use first method
RUN set -e; \
  apt-get update; \
  apt-get install -y curl gnupg2; \
  echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list; \
  curl https://bazel.build/bazel-release.pub.gpg | apt-key add -; \
  apt-get update; \
  apt-get install -y bazel; \
  apt-get install --only-upgrade -y bazel; \
  apt-get clean; \
  touch WORKSPACE; \
  bazel build dummy; \
  pwd; \
  rm -rf /var/lib/apt/lists/* WORKSPACE BUILD dummy.cc;

