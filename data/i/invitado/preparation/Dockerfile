FROM alpine:3.7

# Install curl
RUN apk add --update curl && rm -rf /var/cache/apk/*

# Install jq
RUN apk add --update jq && rm -rf /var/cache/apk/*

# Add publish wrapper.
COPY binding.json /opt/binding.json
COPY publish.json /opt/publish.json

# Add command script.
COPY ./command.sh /opt/command.sh
RUN chmod 755 /opt/command.sh
CMD ["/opt/command.sh"]
