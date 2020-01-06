FROM electronuserland/builder:wine-mono

RUN apt-get update -y && \
  apt-get install -y --no-install-recommends fakeroot libxss1 && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

RUN npm install -g @vue/cli && \
    npm install -g @vue/cli-init && \
    npm install -g yarn && \
    npm install -g quasar-cli
    
WORKDIR /app
