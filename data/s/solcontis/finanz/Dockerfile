# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3-onbuild

MAINTAINER Jurij Tissen <jurij.tissen@gmail.com>

VOLUME /data/db
# COPY startup script into known file location in container
COPY start.sh /start.sh

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 80:80

# CMD specifcies the command to execute to start the server running.
CMD ["/start.sh"]
# done!