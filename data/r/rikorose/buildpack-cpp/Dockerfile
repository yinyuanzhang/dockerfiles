FROM fedora:latest

RUN dnf update -y
RUN dnf install -y \
          curl \
          git \
          clang \
          gcc \
          make \
          cmake

RUN dnf clean all
