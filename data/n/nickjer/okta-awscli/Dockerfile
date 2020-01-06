FROM python:3-alpine
MAINTAINER Jeremy Nicklas <jeremywnicklas@gmail.com>

# Install okta-awscli
RUN pip --no-cache-dir install okta-awscli

# Set new home directory for okta-awscli to use
ENV HOME /data

# Set as default command
ENTRYPOINT ["okta-awscli"]
