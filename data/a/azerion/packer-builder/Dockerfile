FROM python:3.6-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qyy update && apt-get -qqy install unzip git
RUN pip install -qqq pyyaml ansible yamllint boto3

RUN ansible -m unarchive -a 'src=https://releases.hashicorp.com/packer/1.3.2/packer_1.3.2_linux_amd64.zip dest=/usr/local/bin remote_src=yes' localhost
