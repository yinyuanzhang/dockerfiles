# SPDX-License-Identifier: MIT

FROM ubuntu:18.04

# create a non-privileged user for installing tools
RUN groupadd -g 7001 tool && \
    useradd -u 7001 -g tool -m -s /bin/bash tool

# create a non-privileged user for using tools
RUN groupadd -g 1000 user && \
    useradd -u 1000 -g user -m -s /bin/bash user && \
    usermod -a -G tool user

# entrypoint script to fix permissions for user user
COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod 755 /usr/bin/entrypoint.sh

# frequently required tools
RUN apt-get update && apt-get install -y \
    git=1:2.17.1-1ubuntu0.4 \
    gosu=1.10-1 \
    make=4.1-9.1ubuntu1 \
    wget=1.19.4-1ubuntu2.1 \
    && rm -rf /var/lib/apt/lists/*

# tools are installed here
RUN mkdir -p /tool/bin /tool/lib /tool/etc && chown -R tool:tool /tool
RUN mkdir -p /work/target && chown -R user:user /work

# workspace files are mounted here
VOLUME [ "/work/target" ]
WORKDIR /work/target

# /tool/bin is on the path
ENV PATH "$PATH:/tool/bin"
ENV TOOLS_PATH_WORK "/work"
ENV TOOLS_PATH_TARGET "/work/target"

# entrypoint adjusts user to match uid:gid of /work and drops root
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
