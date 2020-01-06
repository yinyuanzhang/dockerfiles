# Start from the basic debian
FROM debian:buster
MAINTAINER admin@kwarc.info

# Install openssh, rsync and git
RUN echo "en_US UTF-8" | tee /etc/locale.gen
RUN apt-get update -y && apt-get install -y openssh-client locales rsync git locales && apt-get clean

CMD ["/bin/bash"]
