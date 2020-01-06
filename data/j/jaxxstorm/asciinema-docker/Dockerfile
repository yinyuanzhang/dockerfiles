FROM asciinema/asciinema-server

MAINTAINER Lee Briggs <lee@leebriggs.co.uk>

# Run some upgrades
RUN apt-get update
RUN apt-get upgrade -y

# install supervisor
RUN apt-get install -y supervisor

# Create needed dirs
RUN mkdir -p /var/lock/asciinema /var/run/asciinema /var/log/supervisor

# Add config files
ADD etc/ /etc/

ENTRYPOINT []

# run supervisor
CMD ["/usr/bin/supervisord"]
#CMD ["rbenv", "exec", "bundle", "exec", "rails", "server"]

