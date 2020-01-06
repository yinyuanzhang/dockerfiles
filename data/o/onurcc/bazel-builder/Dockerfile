FROM debian:buster

# Install prerequisites
RUN apt update && \
  apt install -y curl gnupg build-essential

# Add Bazel repo
RUN echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list && \
  curl https://bazel.build/bazel-release.pub.gpg | apt-key add -

# Install Bazel and JDK
RUN apt update && \
  apt install -y --no-install-recommends openjdk-11-jdk-headless bazel
