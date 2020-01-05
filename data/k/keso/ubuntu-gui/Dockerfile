FROM ubuntu:14.04.4
MAINTAINER wilson

RUN apt-get update && apt-get install -y xauth libwxgtk2.8-0 libxslt1.1 libpq5

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer
ENV DISPLAY=unix:0

VOLUME ["/tmp/.X11-unix"]

CMD /bin/bash

