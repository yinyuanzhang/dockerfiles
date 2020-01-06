FROM ubuntu:14.04
MAINTAINER Derek Bourgeois <derek@ibourgeois.com>

# upgrade the container
RUN apt-get update && \
    apt-get upgrade -y
    
# install some prerequisites
RUN apt-get install -y wget build-essential

# download chef server
RUN wget https://packages.chef.io/stable/ubuntu/14.04/chef-server-core_12.9.1-1_amd64.deb

# install chef server
RUN sudo dpkg -i chef-server-core_12.9.1-1_amd64.deb

# configure chef server
RUN	dpkg-divert --local --rename --add /sbin/initctl
RUN	ln -sf /bin/true /sbin/initctl
ADD	. /usr/local/bin/
CMD	["run_chef_server"]
EXPOSE	443

# clean up our mess
RUN apt-get remove --purge -y software-properties-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean && \
    echo -n > /var/lib/apt/extended_states && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/man/?? && \
    rm -rf /usr/share/man/??_* && \
    rm -rf chef-server-core_12.9.1-1_amd64.deb
