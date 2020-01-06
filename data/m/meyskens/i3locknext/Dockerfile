FROM debian:stretch

RUN apt-get update && apt-get install -y libimlib2-dev fontconfig libxrandr2 git build-essential libx11-dev libxrandr-dev libxcb1 libpam-dev libcairo-dev libxcb-composite0 libxcb-composite0-dev libxcb-xinerama0-dev libev-dev libx11-dev libx11-xcb-dev libxkbcommon-dev libxkbcommon-x11-dev libxcb-dpms0-dev libxcb-image0-dev libxcb-util0-dev libxcb-xkb-dev libxkbcommon-x11-dev

RUN git clone https://github.com/chrjguill/i3lock-color.git && \
    cd i3lock-color && make && make install && \
    cd .. && rm -fr i3lock-color

RUN git clone https://github.com/owenthewizard/i3lock-next.git && \
    cd i3lock-next && make && make install && \
    cd .. && rm -fr i3lock-next

ENTRYPOINT i3lock-next
