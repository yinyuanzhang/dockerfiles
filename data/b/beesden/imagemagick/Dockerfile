FROM ubuntu:16.04

WORKDIR /opt/imagemagick

# Install Imagemagick
RUN apt-get -qq update && \
    apt-get -qq install imagemagick

# Clean up
RUN echo "Cleaning up..."
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean