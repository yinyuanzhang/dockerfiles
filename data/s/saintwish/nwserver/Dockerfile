# i386/debian:buster-slim
FROM i386/debian:buster-slim
LABEL maintainer "wish@hexiahost.com"

# Install the packages needed.
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y libc6:i386 libstdc++6:i386 iproute2 \
    && useradd -m -d /home/container container

# Create container user.
USER container
ENV HOME = /home/container
WORKDIR /home/container

COPY ./prep-nwn-ini.awk /prep-nwn-ini.awk
COPY ./prep-nwnplayer-ini.awk /prep-nwnplayer-ini.awk

# Run via container.
COPY ./entrypoint.sh /entrypoint.sh
CMD ["/bin/bash", "/entrypoint.sh"]
