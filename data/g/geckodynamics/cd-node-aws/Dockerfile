FROM node:12-alpine

# Set timezone to UTC by default
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime

# Update repository indexes
RUN apk update

# Install aws-cli
RUN apk -Uuv add python py-pip
RUN pip install awscli
RUN apk --purge -v del py-pip

# Clean apk cache
RUN rm /var/cache/apk/*

CMD ["/bin/sh"]
