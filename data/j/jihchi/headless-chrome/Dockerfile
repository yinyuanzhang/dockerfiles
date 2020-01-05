FROM ubuntu:latest
MAINTAINER Jih-Chi Lee <achi@987.tw>

# Install utilities
RUN apt-get update --fix-missing && \
  apt-get -y upgrade && \
  apt-get install -y \
  sudo curl wget unzip git

# Install Chrome for Ubuntu
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - && \
  sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
  sudo apt-get update && \
  sudo apt-get install -y \
  google-chrome-unstable

# Add a user and make it a sudo user
RUN useradd -m chromeuser && \
  sudo adduser chromeuser sudo

# Expose port 9222
EXPOSE 9222

# Copy the chrome-user script used to start Chrome as non-root
COPY chromeuser-script.sh /
RUN chmod +x /chromeuser-script.sh

# Set the entrypoint
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
