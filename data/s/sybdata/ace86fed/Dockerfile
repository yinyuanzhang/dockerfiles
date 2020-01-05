FROM fedora:rawhide

# set ports
EXPOSE 8621 6878 8081

RUN \
dnf update -yq && \
dnf -y install python3 python3-pip python3-devel wget tzdata mc nano && \
dnf -y group install "C Development Tools and Libraries" && \
pip3 install --upgrade psutil && \
pip3 install --upgrade gevent && \

#acestream
wget -o - https://sybdata.de/data/acestream/acestream_3.1.33.1_x86_wbUI.tar.gz && \
tar -zxvf acestream_3.1.33.1_x86_wbUI.tar.gz && \
mv acestream.engine/ /opt/ && \
dnf -y autoremove && \

# install aceproxy
wget -o - https://github.com/pepsik-kiev/HTTPAceProxy/archive/master.zip -O aceproxy.zip && \
unzip aceproxy.zip -d /opt/ && \

# cleanup
dnf -y remove python3-devel && \
dnf -y group remove "C Development Tools and Libraries" && \
dnf clean packages && \
rm -rf acestream_3.1.33.1_x86_wbUI.tar.gz aceproxy.zip

ADD aceconfig.py /opt/HTTPAceProxy-master/aceconfig.py
ADD acestream.conf /opt/acestream.engine/androidfs/acestream.engine/acestream.conf
ADD start.sh /bin/start.sh
RUN chmod +x /bin/start.sh

CMD ["/bin/start.sh"]







