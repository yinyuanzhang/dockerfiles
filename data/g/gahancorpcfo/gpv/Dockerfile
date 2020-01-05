FROM ubuntu:16.04 
RUN apt-get -y update 
RUN apt-get -y install wget=1.17.1-1ubuntu1.3
RUN apt-get -y install linux-headers-$(uname -r)
RUN apt-get -y install python3=3.5.1-3; wget https://bootstrap.pypa.io/get-pip.py; python3 get-pip.py; rm -r get-pip.py; ln -sf /usr/bin/pip3 /usr/bin/pip; ln -sf /usr/bin/python3 /usr/bin/python
RUN pip3 install ansible==2.4.2.0
ADD apt.yml /tmp/apt.yml
RUN ansible-playbook /tmp/apt.yml; rm /tmp/apt.yml
ADD pip.yml /tmp/pip.yml
RUN ansible-playbook /tmp/pip.yml; rm /tmp/pip.yml
RUN git clone https://github.com/gahancorpcfo/gpv /opt/gpv
WORKDIR /opt/gpv
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb -O /tmp/wk.deb; dpkg -i /tmp/wk.deb; rm -r /tmp/wk.deb
EXPOSE 8069
EXPOSE 8072
ADD rc /root/.odoorc
CMD /opt/gpv/odoo-bin
