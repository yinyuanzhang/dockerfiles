FROM linuxserver/rutorrent

# add ghost config file
COPY root/ /

WORKDIR /usr/local/bin

# add default post process
COPY rtorrent-postprocess.sh rtorrent-postprocess.sh
RUN chmod +rx rtorrent-postprocess.sh
