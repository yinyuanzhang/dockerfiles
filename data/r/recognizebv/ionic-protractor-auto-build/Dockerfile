FROM timbru31/java-node

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - > /dev/null \
    && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update \
    && apt-get install -y google-chrome-stable patch git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g ionic@3.20.0 cordova@8.0.0