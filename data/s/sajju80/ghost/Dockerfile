#
# Ghost Dockerfile
#
# https://github.com/Sajju80/ghost
#

# Pull base image.
FROM dockerfile/nodejs

# Install Ghost
RUN \
  cd /tmp && \
  wget https://ghost.org/zip/ghost-latest.zip && \
  unzip ghost-latest.zip -d /ghost && \
  rm -f ghost-latest.zip && \
  cd /ghost && \
  npm install --production && \
  useradd ghost --home /ghost

# Add files.
#ADD start.bash /ghost-start
#RUN chmod 755 /ghost-start

# Add wp-config with info for Wordpress to connect to DB
ADD config.js /ghost/config.js
RUN chmod 644 /ghost/config.js

# Fix permissions for ghost user
RUN chown -R ghost:ghost /data /ghost

# Set environment variables.
ENV NODE_ENV production

# Define mountable directories.
# VOLUME ["/data", "/ghost-override"]

# Define working directory.
WORKDIR /ghost

# Define default command.
#CMD ["bash", "/ghost-start"]

# Add run script
ADD run.sh run.sh
RUN chmod 755 /*.sh

# Expose ports.
EXPOSE 2368

# Define default command.
CMD ["/run.sh"]
