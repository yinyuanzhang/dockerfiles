FROM runmymind/docker-android-sdk:latest
RUN apt-get update && apt-get install gnupg2 zip -y \
  && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt install nodejs -y \
  && rm -rf /var/cache/apt/* \
  && npm install -g cordova \
  && curl -s "https://get.sdkman.io" | bash \
  && /bin/bash  -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install gradle" \
  && rm -rf /var/cache/apt/*
