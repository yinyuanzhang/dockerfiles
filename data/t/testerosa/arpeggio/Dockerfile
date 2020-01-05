FROM roffe/kubectl

COPY watcher.sh .

RUN apk --no-cache add jq curl

ENTRYPOINT ["/usr/local/bin/dumb-init","--","/usr/local/bin/docker-entrypoint.sh"]
CMD ["bash"]
