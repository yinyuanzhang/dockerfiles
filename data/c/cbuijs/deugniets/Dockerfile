# To build: 
#     docker build -t deugniets .
# To run:
#     docker run -p 53:53/udp deugniets
#
# !!! NOTE: IPv6 needs fixing

FROM python:3
EXPOSE 53/udp
ADD deugniets.py /opt/deugniets/deugniets.py
ADD cache.py /opt/deugniets/cache.py
ADD requirements.txt /opt/deugniets/requirements.txt
ADD deugniets.conf.docker /opt/deugniets/deugniets.conf
ADD local.list.docker /opt/deugniets/local.list
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade chardet==3.0.4
RUN pip3 install --upgrade urllib3==1.25.7
RUN pip3 install --upgrade git+https://github.com/opendns/dnspython-clientsubnetoption@master
RUN pip3 install --upgrade git+https://github.com/rthalley/dnspython@master
RUN pip3 install --upgrade git+https://github.com/psf/requests@master
RUN pip3 install --upgrade -r /opt/deugniets/requirements.txt
CMD [ "python3", "/opt/deugniets/deugniets.py", "/opt/deugniets/deugniets.conf" ]

