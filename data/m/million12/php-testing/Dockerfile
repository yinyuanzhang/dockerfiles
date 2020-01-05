FROM million12/nginx-php:latest
MAINTAINER Marcin Ryzycki marcin@m12.io

# Install java, Xvfb, x11vnc server and firefox
# Download Selenium Standalone Server
# Remove supervisord configs for nginx and php - we don't need to run them in this container
# (but we need PHP configuration to run Behat tests)
RUN \
  yum update -y && \
  yum install -y java-1.8.0-openjdk-headless xorg-x11-server-Xvfb x11vnc firefox && \
  yum clean all && \
  curl -sSL -o /usr/bin/selenium-server-standalone.jar http://selenium-release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.0.jar && \
  rm -f /etc/supervisor.d/nginx.conf /etc/supervisor.d/php-fpm.conf

ADD container-files /

ENV \
  SCREEN_DIMENSION=1600x1000x24 \
  VNC_PASSWORD=password

EXPOSE 4444 5900
