FROM oichuppa/base
MAINTAINER chuppa

RUN mkdir /plexdata && mkdir /logs && mkdir /etc/cron.d

RUN apt update
RUN apt upgrade -y
RUN apt install -y --no-install-recommends --no-install-suggests python git bash cron
RUN git clone https://github.com/ngovil21/Plex-Cleaner.git /app
RUN apt remove git -y
RUN rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

# Add the scripts 
COPY run-entry.sh /app/run-entry.sh
COPY run-plexcleaner.sh /app/run-plexcleaner.sh
RUN chmod +x /app/run-entry.sh && chmod +x /app/run-plexcleaner.sh

# Default interval to 5min
ENV EXECUTION_CRON_EXPRESSION 0 */6 * * *

# REQUIRED
# Store the configuration out of the container
VOLUME ["/config"]

# OPTIONNAL
# In case the script is configured to directly delete the files, we need to mount the plex data folder
VOLUME ["/plexdata"]

# OPTIONNAL
# Contains the execution logs 
VOLUME ["/logs"]

ENTRYPOINT ["/app/run-entry.sh"]
