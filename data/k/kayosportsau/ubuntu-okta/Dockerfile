FROM kayosportsau/ubuntu-base:1.0.1

ADD add /tmp

RUN mkdir /opt/okta-utils && \
    cd /tmp && \
    mv oktashell.sh /usr/local/bin && \
    mv oktashell assumerole requirements.txt /opt/okta-utils && \
    pip3 install --no-cache-dir -r /opt/okta-utils/requirements.txt

ENTRYPOINT ["/bin/bash"]