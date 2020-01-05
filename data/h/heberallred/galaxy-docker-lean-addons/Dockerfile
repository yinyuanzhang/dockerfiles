FROM heberallred/galaxy-docker-lean:latest

# Install additional dependencies (adds to ltlbsteed/galaxy-docker-lean:v1)
# These are for puppeteer. Note: currently puppeteer only works if launched with --no-sandbox argument ()
RUN apt-get update && \
    apt-get install -y \
        gconf-service libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 \
        libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 \
        libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 \
        libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget && \
    rm -rf /var/lib/apt/lists/*










# Looking for a way to get Chromium to run in the sandbox (so far unsuccessful)
#FROM ltlbsteed/galaxy-docker-lean:v1_1804
#
## Install additional dependencies (adds to ltlbsteed/galaxy-docker-lean:v1)
## These are for puppeteer. Note: currently puppeteer only works if launched with --no-sandbox argument ()
#RUN apt-get update && \
#    apt-get install -y \
#        gconf-service libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 \
#        libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 \
#        libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 \
#        libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget unzip && \
#    rm -rf /var/lib/apt/lists/* && \
#    wget https://github.com/ltlbsteed/galaxy-docker-lean-addons/raw/master/chrome_sandbox -O /usr/local/sbin/chrome-devel-sandbox && \
#    chown root:root /usr/local/sbin/chrome-devel-sandbox && \
#    chmod 4755 /usr/local/sbin/chrome-devel-sandbox && \
#    echo "export CHROME_DEVEL_SANDBOX=/usr/local/sbin/chrome-devel-sandbox" >> ~/.bashrc
