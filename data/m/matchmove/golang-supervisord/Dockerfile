#On the top of the file, add a line with the base image (golang:latest) that we want to use.
FROM golang:latest

# Update the Debian software repository inside the dockerfile with the 'RUN' command.
RUN apt-get update

# Install supervisord from Debian repository
RUN apt-get install -y supervisor
