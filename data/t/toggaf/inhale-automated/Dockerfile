FROM debian:stable
MAINTAINER John Doe <user@neko.li>
LABEL company="Toggaf CNI"
LABEL version="1.0.0"

# Install temporarly dev libraries 
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
      build-essential:native automake libtool make gcc python3 python3-pip

# Let's go !
CMD ["/bin/sh"]