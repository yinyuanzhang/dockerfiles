# Multistage docker build, requires docker 17.05

# builder stage
FROM ubuntu:18.04 as builder

# Allows us to auto-discover the latest release from the repo
ARG REPO=masari-project/masari
ENV REPO=${REPO}

RUN set -ex && \
    apt-get update && \
    apt-get  --yes install \
        curl tar


RUN TAG=$(curl -L --silent "https://api.github.com/repos/$REPO/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")') &&  curl -L https://github.com/$REPO/releases/download/$TAG/masari-linux-x64-$TAG.tar.gz | tar -xz && \
	mkdir /release && cp masari-linux-x64-$TAG/* /release

# runtime stage
FROM ubuntu:18.04

# Now we DO need these, for the auto-labeling of the image
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/masari.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

COPY --from=builder /release/* /usr/local/bin/

# Contains the blockchain
VOLUME /root/.masari

# Generate your wallet via accessing the container and run:
# cd /wallet
# masari-wallet-cli
VOLUME /wallet

EXPOSE 38080
EXPOSE 38081

ENTRYPOINT ["masarid", "--p2p-bind-ip=0.0.0.0", "--p2p-bind-port=38080", "--rpc-bind-ip=0.0.0.0", "--rpc-bind-port=38081", "--non-interactive", "--confirm-external-bind"]
