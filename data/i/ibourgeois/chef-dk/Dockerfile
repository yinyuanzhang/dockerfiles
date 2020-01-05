FROM ubuntu:14.04
MAINTAINER Derek Bourgeois <derek@ibourgeois.com>

# upgrade the container
RUN apt-get update && \
    apt-get upgrade -y
    
# install some prerequisites
RUN apt-get install -y wget build-essential

# download chef dk
RUN wget https://packages.chef.io/stable/ubuntu/12.04/chefdk_0.18.30-1_amd64.deb

# install chef dk
RUN sudo dpkg -i chefdk_0.18.30-1_amd64.deb

# configure chef dk
RUN echo `eval "$(chef shell-init bash)"` >> ~/.bash_profile
VOLUME /opt/chef

# install git
RUN sudo apt-get install git -y

# det default command. 
CMD ["bash"]

# clean up our mess
RUN apt-get remove --purge -y software-properties-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean && \
    echo -n > /var/lib/apt/extended_states && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/man/?? && \
    rm -rf /usr/share/man/??_* && \
    rm -rf chefdk_0.18.30-1_amd64.deb
