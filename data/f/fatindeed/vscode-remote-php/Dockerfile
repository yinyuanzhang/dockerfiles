FROM php:5-stretch

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL maintainer="James Zhu <168262+fatindeed@users.noreply.github.com>" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="fatindeed/vscode-remote-php" \
      org.label-schema.description="PHP sample project for trying out the VS Code Remote - Containers extension" \
      org.label-schema.url="https://hub.docker.com/r/fatindeed/vscode-remote-php" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/fatindeed/vscode-remote-try-php" \
      org.label-schema.vendor="James Zhu" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

ARG DEBIAN_MIRROR

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Or your actual UID, GID on Linux if not the default 1000
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN set -e; \
    #
    # Switch to a mirror if given
    if [ -n "$DEBIAN_MIRROR" ]; then \
        sed -i 's!http://deb.debian.org!'"$DEBIAN_MIRROR"'!g' /etc/apt/sources.list; \
    fi; \
    #
    # Configure apt and install packages
    apt-get update; \
    apt-get -y install --no-install-recommends apt-utils dialog 2>&1; \
    #
    # Install git, procps, lsb-release (useful for CLI installs)
    apt-get install -y --no-install-recommends git procps iproute2 lsb-release; \
    #
    # Install xdebug
    yes | pecl install xdebug-2.5.5; \
    docker-php-ext-enable xdebug; \
    { \
        echo 'xdebug.remote_enable=on'; \
        echo 'xdebug.remote_autostart=on'; \
    } | tee -a /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini; \
    #
    # Install pcntl zip
    buildDeps='libzip-dev zlib1g-dev'; \
    apt-get install -y --no-install-recommends $buildDeps; \
    docker-php-ext-install pcntl zip; \
    find /usr/local/lib/php/extensions -type f -executable -exec ldd '{}' ';' \
        | awk '/=>/ { print $(NF-1) }' \
        | sort -u \
        | xargs -r dpkg-query --search \
        | cut -d: -f1 \
        | sort -u \
        | xargs -r apt-mark manual \
    ; \
    apt-get purge -y $buildDeps; \
    docker-php-source delete; \
    #
    # Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
    groupadd --gid $USER_GID $USERNAME; \
    useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME; \
    mkdir -p /home/$USERNAME/.vscode-server /home/$USERNAME/.vscode-server-insiders; \
    chown ${USER_UID}:${USER_GID} /home/$USERNAME/.vscode-server*; \
    # [Optional] Add sudo support for non-root user
    apt-get install -y sudo; \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME; \
    chmod 0440 /etc/sudoers.d/$USERNAME; \
    #
    # [Optional] Install openssh-client unzip bash-completion
    apt-get install -y --no-install-recommends openssh-client unzip bash-completion; \
    #
    # [Optional] Install Composer, PHP_CodeSniffer
    curl -sSL https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer; \
    chmod a+x /usr/local/bin/*; \
    composer --version; \
    #
    # Clean up
    apt-get autoremove -y; \
    apt-get clean -y; \
    rm -rf /var/lib/apt/lists/*; \
    rm -rf /tmp/pear;

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=

# Set the default user
USER $USERNAME

CMD [ "sleep", "infinity" ]