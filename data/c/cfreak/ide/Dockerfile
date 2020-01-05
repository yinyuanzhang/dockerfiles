FROM ubuntu:19.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    lsof \
    gpg \
    curl \
    dumb-init \
    git \
    sudo \
    gdb \
    build-essential \
    # Node JS
    nodejs \
    npm \
    # JDK
    default-jdk-headless \
    gradle \
    # Code-Server
    bsdtar \
    openssl \
    locales \
    net-tools

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# Add utility scripts
ADD scripts /opt/code-freak

# Install Coder
ENV CODE_VERSION="1.939-vsc1.33.1"
RUN mkdir -p /opt/code-server-${CODE_VERSION} \
    && curl -sL https://github.com/cdr/code-server/releases/download/${CODE_VERSION}/code-server${CODE_VERSION}-linux-x64.tar.gz \
       | tar --strip-components=1 -zx -C /opt/code-server-${CODE_VERSION} \
    && ln -s /opt/code-server-${CODE_VERSION}/code-server /usr/local/bin/code-server


# Create user and allow sudoing
RUN groupadd -r coder \
    && useradd -m coder -g coder -s /bin/bash \
    && echo "coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd
USER coder
WORKDIR /tmp

# Install coder extensions
ENV VSCODE_USER "/home/coder/.local/share/code-server/User"
ENV VSCODE_EXTENSIONS "/home/coder/.local/share/code-server/extensions"

RUN mkdir -p $VSCODE_USER $VSCODE_EXTENSIONS

# Config
COPY  --chown=coder:coder settings/ $VSCODE_USER

# Java Extensions
ARG VSCODE_JAVA_VERSION=0.45.0
ARG VSCODE_JAVA_DEBUG_VERSION=0.18.0
ARG VSCODE_JAVA_TEST_VERSION=0.16.0

RUN mkdir -p ${VSCODE_EXTENSIONS}/java \
    && curl -JLs --retry 5 https://github.com/redhat-developer/vscode-java/releases/download/v${VSCODE_JAVA_VERSION}/redhat.java-${VSCODE_JAVA_VERSION}.vsix | bsdtar --strip-components=1 -xf - -C ${VSCODE_EXTENSIONS}/java extension

RUN mkdir -p ${VSCODE_EXTENSIONS}/java-debugger \
    && curl -JLs --retry 5 https://github.com/microsoft/vscode-java-debug/releases/download/${VSCODE_JAVA_DEBUG_VERSION}/vscode-java-debug-${VSCODE_JAVA_DEBUG_VERSION}.vsix | bsdtar --strip-components=1 -xf - -C ${VSCODE_EXTENSIONS}/java-debugger extension

RUN mkdir -p ${VSCODE_EXTENSIONS}/java-test \
    && curl -JLs --retry 5 https://github.com/microsoft/vscode-java-test/releases/download/${VSCODE_JAVA_TEST_VERSION}/vscjava.vscode-java-test-${VSCODE_JAVA_TEST_VERSION}.vsix | bsdtar --strip-components=1 -xf - -C ${VSCODE_EXTENSIONS}/java-test extension

# Custom Sonar lint with Java support
COPY --chown=coder:coder sonarlint-vscode-1.7.0-SNAPSHOT.vsix .
RUN mkdir -p ${VSCODE_EXTENSIONS}/sonarlint \
    && bsdtar --strip-components=1 -xf sonarlint-vscode-1.7.0-SNAPSHOT.vsix -C ${VSCODE_EXTENSIONS}/sonarlint extension \
    && rm sonarlint-vscode-1.7.0-SNAPSHOT.vsix

RUN mkdir -p /home/coder/project
WORKDIR /home/coder/project
ENTRYPOINT ["dumb-init", "code-server", "--disable-telemetry", "--no-auth", "--allow-http", "-p", "3000"]
