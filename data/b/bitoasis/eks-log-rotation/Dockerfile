################################################################################
##
## Dockerfile for utility container with preconfigured logrotate tool
## used in Kubernetes cluster. In order to access logs in node, it has
## to run under root user
##

FROM alpine:3.8

LABEL author="bitoasis" \
      description="Contains preconfigured logrotate tool for use in k8s cluster" \
	  version="0.1"

# Install logrotate utility
RUN apk add --no-cache logrotate

# Copy sample configuration
COPY ./conf/logrotate.d /etc/logrotate.d

# Keep container run foreever
CMD ["sh", "-c", "tail -f /dev/null"]