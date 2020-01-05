FROM ruby:2.6.3

ENV DEBIAN_FRONTEND noninteractive

# Download bosh-cli bin
RUN wget https://github.com/cloudfoundry/bosh-cli/releases/download/v5.5.1/bosh-cli-5.5.1-linux-amd64 -O /usr/local/bin/bosh 

# Install CF bootloader
RUN wget https://github.com/cloudfoundry/bosh-bootloader/releases/download/v8.1.0/bbl-v8.1.0_linux_x86-64 -O /usr/local/bin/bbl


# Install dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential \
                       zlibc zlib1g-dev \
                       openssl libxslt1-dev \
                       libxml2-dev libssl-dev \
                       libreadline7 libreadline-dev \
                       libyaml-dev libsqlite3-dev \
                       sqlite3 unzip && \
    apt-get -y clean && \
    rm -rf /var/cache/apt/archives && \
    rm -rf /var/lib/apt/lists/*

# Install Terraform
RUN wget https://releases.hashicorp.com/terraform/0.12.5/terraform_0.12.5_linux_amd64.zip -O terraform.zip && \
    unzip terraform.zip -d /usr/local/bin && \
    rm terraform.zip && \
    chmod +x /usr/local/bin/*

    

