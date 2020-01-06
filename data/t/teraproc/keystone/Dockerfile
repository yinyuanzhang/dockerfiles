# Pull base image.
FROM ubuntu:14.04

MAINTAINER Weina Ma <vena1028@gmail.com>

# Install Keystone
RUN apt-get update
RUN apt-get install -y git python-setuptools python-pip python-dev mailutils
RUN pip install pbr
RUN git clone -b stable/juno http://github.com/openstack/keystone.git /usr/local/keystone
ADD core.py /usr/local/keystone/keystone/identity/
ADD keystone.conf.sample /usr/local/keystone/etc/
ADD email-success.html /usr/local/keystone/
RUN cd /usr/local/keystone && python setup.py install
RUN cp /usr/local/keystone/etc/keystone.conf.sample /usr/local/keystone/etc/keystone.conf
ADD startkeystone.sh /usr/local/keystone/

EXPOSE 5000 35357

# Start Keystone
CMD ["/bin/bash", "-c", "/usr/local/keystone/startkeystone.sh"]

# build docker image and run docker container by
# docker build -t keystone .
# mkdir keystone_db
# docker run --rm -p 5000:5000 -p 35357:35357 -v /vagrant/resources/keystone/keystone_db:/var/lib/keystone -v /var/spool/postfix:/var/spool/postfix keystone
