FROM docker:dind

# Install additional requirements
RUN apk add -y --update wget git bash sudo

RUN wget https://github.com/buildpack/pack/releases/download/v0.5.0/pack-v0.5.0-linux.tgz && \
    tar xvf pack-v0.5.0-linux.tgz && \
    rm pack-v0.5.0-linux.tgz && \
    chmod +x pack && \
    mv pack /usr/bin/pack

ENTRYPOINT ["dockerd-entrypoint.sh"]

CMD ["/bin/ash", "-c", "sleep 100000000"] 
