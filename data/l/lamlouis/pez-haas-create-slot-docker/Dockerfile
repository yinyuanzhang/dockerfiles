FROM centos:7

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm

RUN yum -y install git curl wget jq  python-pip python-devel openssl openssl-devel libxml2-devel libxslt-devel libffi-devel gcc

RUN pip install pyvmomi tabulate nsxramlclient

RUN cd /tmp && git clone https://github.com/vmware/vsphere-automation-sdk-python.git \
  && cd /tmp/vsphere-automation-sdk-python \
  && pip install --upgrade --force-reinstall -r requirements.txt --extra-index-url file:///tmp/vsphere-automation-sdk-python/lib 

