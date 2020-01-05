FROM bash:4

RUN apk add bc bind-tools redis

RUN ln -s /usr/local/bin/bash /bin/bash

COPY ["run.sh", "/"]

CMD ["/run.sh"]

ENTRYPOINT ["bash", "-c"]
