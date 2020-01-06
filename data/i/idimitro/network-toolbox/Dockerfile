FROM ubuntu
RUN apt-get update && apt-get install dnsutils curl wget -y
ENTRYPOINT /bin/bash
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
