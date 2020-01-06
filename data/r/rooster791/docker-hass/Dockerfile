FROM homeassistant/home-assistant
RUN apt-get update && apt-get install samba-common jq dnsutils ipmitool libpython-dev libffi-dev libssl-dev git -y
RUN git clone https://github.com/web-push-libs/pywebpush.git /pyweb
RUN cd /pyweb && python setup.py develop
RUN chown nobody:nogroup /config

