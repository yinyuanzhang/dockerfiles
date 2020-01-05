FROM ubuntu:14.04
MAINTAINER krystism "krystism@gmail.com"
# To enable the OpenStack repository
RUN echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-updates/juno main" > /etc/apt/sources.list.d/ubuntu-cloud-archive-juno-trusty.list
RUN apt-get update && apt-get -y install ubuntu-cloud-keyring

# To install openstackclient
RUN apt-get -y update && apt-get -y install \
	python-ceilometerclient \
	python-cinderclient \
	python-glanceclient \
	python-heatclient \
	python-keystoneclient \
	python-novaclient \
	python-neutronclient \
	python-saharaclient \
	python-swiftclient \
	python-troveclient
CMD ["bash"]
