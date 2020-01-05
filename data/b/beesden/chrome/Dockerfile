FROM node:8

WORKDIR /opt/chrome

# Install minor deps
USER root

# RUN echo "Installing libs..."
# RUN apt-get -qq update && \
#    apt-get -qq install -y xvfb libosmesa6 libgconf-2-4

# Misc setup commands...
# RUN mv /usr/bin/google-chrome /usr/bin/google-chrome.real  \
#  && mv /opt/google/chrome/google-chrome /opt/google/chrome/google-chrome.real  \
#  && rm /etc/alternatives/google-chrome \
#  && ln -s /opt/google/chrome/google-chrome.real /etc/alternatives/google-chrome \
#  && ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
#  && ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser \
#  && ln -s /usr/lib/x86_64-linux-gnu/libOSMesa.so.6 /opt/google/chrome/libosmesa.so

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
RUN rm google-chrome-stable_current_amd64.deb

# Clean up
RUN echo "Cleaning up..."
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean

USER $USER_ID