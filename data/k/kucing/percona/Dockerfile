###########################################################
# Dockerfile to build PerconaDB container images
# Based on Ubuntu
###########################################################

# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Ivan <ivan@marsudirini-bks.sch.id>

# Adding my.cnf File
COPY templates/my.cnf /etc/my.cnf

# Install PerconaDB Repository
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A

# Create the apt source list
RUN echo "deb http://repo.percona.com/apt "$(lsb_release -sc)" main" | sudo tee /etc/apt/sources.list.d/percona.list

# Update The Repository Sources List
RUN apt-get update -y

# Install PerconaDB
RUN apt-get install -y percona-server-server-5.6

# Expose The Default Port
EXPOSE 3306

# Default Directory
WORKDIR /

# Copy Startup Script
COPY templates/start.sh /start.sh

# Setting Up Permission
RUN chmod 775 /start.sh

# Default port to execute the entrypoint
CMD ["/start.sh"]
