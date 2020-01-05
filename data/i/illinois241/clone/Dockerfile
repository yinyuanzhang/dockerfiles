FROM alpine:3.8
RUN apk add --no-cache bash git openssh
RUN mkdir -p /root/.ssh && \
    echo $'Host *\n\tStrictHostKeyChecking no' >> /root/.ssh/config && \
    chmod 400 /root/.ssh/config
ADD askpass.sh .
ADD clone.sh .
ENTRYPOINT ["/bin/bash", "clone.sh"]
