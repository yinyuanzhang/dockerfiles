FROM node:9

# Copying the local source to the image
COPY . /dtptest/

# Define the working directory for all future commands
WORKDIR /dtptest


RUN apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq install --no-install-recommends -y \

      # Installing prerequisites
      curl \
      apt-transport-https \
      ca-certificates \
      apt-utils \

    && \

    # Import key and adding Yarn source list
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \

    # Refresh the package list for Yarn.
    apt-get -qq update -o Dir::Etc::sourcelist="sources.list.d/yarn.list" \
            -o Dir::Etc::sourceparts="-" \
            -o APT::Get::List-Cleanup="0" \

    && \

    # Installing the packages
    DEBIAN_FRONTEND=noninteractive apt-get -qq install --no-install-recommends -y \

      # Nightmare dependencies
      xvfb \
      x11-xkb-utils \
      xfonts-100dpi \
      xfonts-75dpi \
      xfonts-scalable \
      xfonts-cyrillic \
      x11-apps \
      clang \
      libdbus-1-dev \
      libgtk2.0-dev \
      libnotify-dev \
      libgnome-keyring-dev \
      libgconf2-dev \
      libasound2-dev \
      libcap-dev \
      libcups2-dev \
      libxtst-dev \
      libxss1 \
      libnss3-dev \
      gcc-multilib \
      g++-multilib \

      # Yarn
      yarn \


    && \

    # Install repository packages
    rm -rf node_modules && \
    yarn install --frozen-lockfile \

    && \

    # Cleanup (saves space in the Docker image)
    DEBIAN_FRONTEND=noninteractive apt-get -qq remove -y \
      apt-utils \
      libdbus-1-dev \
      libgtk2.0-dev \
      libnotify-dev \
      libgnome-keyring-dev \
      libgconf2-dev \
      libasound2-dev \
      libcap-dev \
      libcups2-dev \
      libxtst-dev \
      libnss3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ENTRYPOINT ["/dtptest/entrypoint.sh"]
