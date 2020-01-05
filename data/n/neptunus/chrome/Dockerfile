FROM neptunus/chrome

ADD get-pip.py /tmp/

USER root

RUN apt-get update && \
    apt-get install -y  curl && \	
    cd /tmp &&  python3 get-pip.py  && \
    pip3 install -U selenium        && \
    pip3 install requests           

USER seluser

CMD ["/opt/bin/entry_point.sh"]
