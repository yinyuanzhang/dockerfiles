FROM debian:8.9

# Update and Install Packages
RUN apt-get update -y && apt-get install -y \
    ant \
    git \
    openssh-client \
    rubygems \
    wget

# Install Official Puppet Repository
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-jessie.deb && \
    dpkg -i puppetlabs-release-pc1-jessie.deb && \
    rm puppetlabs-release-pc1-jessie.deb

# Install Puppet
RUN apt-get update -y && apt-get install -y puppet-agent
RUN ln -fs /opt/puppetlabs/puppet/bin/puppet /usr/bin/puppet
RUN ln -fs /opt/puppetlabs/puppet/bin/facter /usr/bin/facter

# Install puppet-lint
RUN /opt/puppetlabs/puppet/bin/gem install puppet-lint
RUN ln -fs /opt/puppetlabs/puppet/bin/puppet-lint /usr/bin/puppet-lint

# Clean up unneeded directories
RUN rm -rf /var/lib/apt/lists/*

# Disable host key checking from within builds as we cannot interactively accept them
# TODO: It might be a better idea to bake ~/.ssh/known_hosts into the container
RUN mkdir -p ~/.ssh
RUN printf "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config