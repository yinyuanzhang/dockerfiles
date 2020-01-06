# Ubuntu 16.04
FROM ubuntu:xenial

# Update and install CURL
RUN apt-get update && apt-get install -y curl

# Install Node 8 and chromium-browser
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y nodejs software-properties-common
RUN apt-get install -y libappindicator1 fonts-liberation chromium-browser

# Install GIT
RUN apt-get install -y git

CMD ["chromium-browser", "--headless", "--no-sandbox", "--dump-dom"]
