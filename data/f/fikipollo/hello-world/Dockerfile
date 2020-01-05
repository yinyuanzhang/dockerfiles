############################################################
# Dockerfile to build a hello-world container image for the eBioKit
# Based on hello-world
############################################################

# Set the base image to hello-world
FROM busybox

# File Author / Maintainer
MAINTAINER Rafael Hernandez <ebiokit@gmail.com>

################## BEGIN INSTALLATION ######################

COPY configs/index.html /var/www/index.html_back
COPY configs/entrypoint.sh /usr/bin/entrypoint.sh

RUN chmod +x /usr/bin/entrypoint.sh

##################### INSTALLATION END #####################

EXPOSE 80

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
