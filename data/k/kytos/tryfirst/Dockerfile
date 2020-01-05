FROM kytos/base

RUN python3.6 -m pip install --upgrade pip setuptools wheel
RUN python3.6 -m pip install python-openflow --pre
RUN python3.6 -m pip install kytos-utils --pre
RUN python3.6 -m pip install kytos --pre

EXPOSE 6653
EXPOSE 8181

ADD kytos-welcome.txt /tmp/kytos-welcome.txt
ADD init.sh /init.sh
CMD /bin/bash /init.sh
