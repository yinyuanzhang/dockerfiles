FROM camptocamp/mcollectived:2.12.4-1

# Install git
RUN apt-get update \
  && apt-get install -y git \
  && rm -rf /var/lib/apt/lists/*

# Install r10k
ENV R10K_VERSION='3.0.3+postrun'
RUN gem install specific_install --no-ri --no-rdoc \
  && gem specific_install -l https://github.com/camptocamp/r10k.git -b $R10K_VERSION

# Configure .ssh directory
RUN mkdir /root/.ssh \
  && chmod 0600 /root/.ssh \
  && echo StrictHostKeyChecking no > /root/.ssh/config

# Configure volumes
VOLUME ["/opt/puppetlabs/r10k/cache/", "/etc/puppetlabs/code/environments"]
