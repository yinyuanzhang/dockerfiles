# FROM centos:7
FROM fedora:30

MAINTAINER Paul Podgorsek <ppodgorsek@users.noreply.github.com>
LABEL description Robot Framework in Docker.

# Setup volumes for input and output
VOLUME /opt/robotframework/reports
VOLUME /opt/robotframework/tests

# Setup X Window Virtual Framebuffer
ENV SCREEN_COLOUR_DEPTH 24
ENV SCREEN_HEIGHT 1080
ENV SCREEN_WIDTH 1920

# Set number of threads for parallel execution
# By default, no parallelisation
ENV ROBOT_THREADS 1

# Dependency versions
ENV CHROMIUM_VERSION 68.0.*
ENV FAKER_VERSION 4.2.0
ENV FIREFOX_VERSION 67.0*
ENV GECKO_DRIVER_VERSION v0.24.0
ENV PABOT_VERSION 0.46
ENV PYTHON_PIP_VERSION 18.0*
ENV REQUESTS_VERSION 0.5.0
ENV ROBOT_FRAMEWORK_VERSION 3.1.1
ENV SELENIUM_LIBRARY_VERSION 3.3.1
ENV XVFB_VERSION 1.20.*

# Install system dependencies
RUN dnf upgrade -y \
  && dnf install -y \
    chromium \
    chromedriver \
    firefox \
	chromium-common \
	chromium-libs-media \
    python2\
	python2-pip\
    python2-tkinter \
    xauth \
    xorg-x11-server-Xvfb \
    which \
    wget \
  && dnf clean all

# Install Robot Framework and Selenium Library
RUN pip install \
  robotframework \
  robotframework-faker\
  robotframework-pabot\
  robotframework-FtpLibrary \
  robotframework-ExtendedSelenium2Library \
  robotframework-seleniumlibrary \
  robotframework-DatabaseLibrary \
  robotframework-DiffLibrary \
  Dialogs \
  Pygments \
  chromedriver-py
# robotframework-seleniumlibrary==$SELENIUM_LIBRARY_VERSION

# Download Gecko drivers directly from the GitHub repository
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz" \
      && tar xzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz \
      && mkdir -p /opt/robotframework/drivers/ \
      && mv geckodriver /opt/robotframework/drivers/geckodriver \
      && rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz

# Prepare binaries to be executed
ADD eShop/bin/chromedriver.sh /opt/robotframework/bin/chromedriver
ADD eShop/bin/chromium-browser.sh /opt/robotframework/bin/chromium-browser
ADD eShop/bin/run-tests-in-virtual-screen.sh /opt/robotframework/bin/
ADD eShop/AUTO_eShop.robot /opt/robotframework/tests/
# COPY . . 

# FIXME: below is a workaround, as the path is ignored
RUN mv /usr/lib64/chromium-browser/chromium-browser /usr/lib64/chromium-browser/chromium-browser-original \
  && ln -sfv /opt/robotframework/bin/chromium-browser /usr/lib64/chromium-browser/chromium-browser

# Update system path
ENV PATH=/opt/robotframework/bin:/opt/robotframework/drivers:$PATH

# Execute all robot tests
# CMD ["/opt/robotframework/bin/run-tests-in-virtual-screen.sh"]
CMD ["robot","/opt/robotframework/tests/AUTO_eShop.robot"]
