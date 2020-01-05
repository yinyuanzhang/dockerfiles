FROM jenkinsci/jnlp-slave

RUN env

USER root

# Copy Setup Script
COPY setup.sh /setup.sh

# Run Setup
RUN /setup.sh

USER jenkins
