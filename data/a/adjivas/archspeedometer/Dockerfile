FROM base/archlinux
LABEL name="archspeedometer"
MAINTAINER adjivas <adjivas@student.42.fr>
ENV HOME /root
ENV LANG en_US.UTF-8
RUN pacman -Syy ;
RUN pacman -S --noconfirm python2 setuptools git ;
RUN git clone https://github.com/wardi/urwid.git /tmp/urwid && \
    cd /tmp/urwid && \ 
    python2 setup.py install ;
RUN git clone https://github.com/wardi/speedometer.git /tmp/speedometer && \
    cd /tmp/speedometer && \
    python2 setup.py install ;
CMD export LINK_IP=$(ip link | grep -Po "(?<=(: )).*(?=:)|.(?<=(: )).*(?=@)") && \
    export LINK_RX=$(echo $LINK_IP | sed -e "s: : -rx :g;s:^: -rx :g") && \
    export LINK_TX=$(echo $LINK_IP | sed -e "s: : -tx :g;s:^: -tx :g") && \
    export LINK=$(echo $LINK_RX $LINK_TX) && \
    speedometer $LINK -k $COLOR ;
ENV COLOR 256
