FROM debian:bullseye

COPY *.sh /
RUN chmod +x install-inkscape.sh && sleep 1 && ./install-inkscape.sh && rm install-inkscape.sh

EXPOSE 3389 8080
