FROM wood1986/virtualbox

RUN echo -e "#!/bin/sh\n./vboxdrv.sh setup && ./vboxwebsrv && export KONTROLURL=http://koding.wensley.eu/kontrol/kite; curl -sL https://sandbox.kodi.ng/c/d/kd | bash -s \$* && sleep infinity" > start.sh

RUN chmod +x start.sh

ENTRYPOINT ["./start.sh"]
