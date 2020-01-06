FROM alpine:3.5

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
    
RUN apk add --no-cache git curl nmap nano
RUN pip3 install requests ws4py

WORKDIR /opt/hue-emulator/

RUN cd /tmp; git clone https://github.com/mariusmotea/diyHue.git
RUN cd /tmp/diyHue/BridgeEmulator/; cp HueEmulator3.py coap-client-linux config.json /opt/hue-emulator/

EXPOSE 80
EXPOSE 1900

ENTRYPOINT ["/opt/hue-emulator/HueEmulator3.py"]
