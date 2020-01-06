FROM ubuntu

# Install build
RUN apt-get update && apt-get install -y wget jq git perl unzip build-essential

# Install Packer
ENV PACKER_VERSION 1.4.2

RUN wget -nc -q https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip -P /usr/local/bin
# -nc, --no-clobber                skip downloads that would download to existing files (overwriting them)
# -q,  --quiet                     quiet (no output)
# -P,  --directory-prefix=PREFIX   save files to PREFIX/..

RUN unzip -q /usr/local/bin/packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/local/bin
# -q  quiet mode (-qq => quieter)
# -d  extract files into exdir

VOLUME /usr/local/src

WORKDIR /usr/local/src

CMD ["packer", "build", "packer_template.json"]
