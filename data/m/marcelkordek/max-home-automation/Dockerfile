FROM jlesage/baseimage-gui:debian-9

# Install max-home-automation.
COPY sources.list.d/* /etc/apt/sources.list.d/
#RUN add-pkg libpython3.7-dev max-home-automation-3.1
RUN add-pkg max-home-automation-3.2 --no-install-recommends -y

# Set the name of the application.
ENV APP_NAME="MAX! Home Automation"

# Environment Variables
ENV TZ="Europe/Amsterdam"
ENV KEEP_APP_RUNNING=1

# Copy the start script.
COPY startapp.sh /startapp.sh

# Expose ports
EXPOSE 5800 5900

# Create volume
VOLUME /config
