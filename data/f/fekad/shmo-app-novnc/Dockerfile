FROM ubuntu:14.04

LABEL maintainer="Adam Fekete <adam.fekete@kcl.ac.uk>"

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /root/

RUN apt-get update -y \
 && apt-get install -yq --no-install-recommends \
			Xvfb \
			x11vnc \
			openbox \
			menu \
			novnc \
			python-xdg \
			supervisor \
			wget \
			xterm \
			icedtea-7-plugin \
			libxt6 \
			libdbus-glib-1-2 \
			libgtk-3-0 \
			libxt6 \
			libstartup-notification0 \
			libxcb-util0 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*


RUN wget https://ftp.mozilla.org/pub/firefox/releases/51.0b9/linux-x86_64/en-GB/firefox-51.0b9.tar.bz2 \
 && tar xvjf firefox-51.0b9.tar.bz2 \
 && rm firefox-51.0b9.tar.bz2

# Add files.
COPY rootfs/ /

# Set environment variables.
ENV APP_NAME="Firefox" \
    DISPLAY=:1 \
    DISPLAY_WIDTH=1280  \
    DISPLAY_HEIGHT=768

RUN chmod 0755 /root/startapp.sh
CMD ["/root/startapp.sh"]

# Expose ports.
#   - 5800: VNC web interface
#   - 5900: VNC
EXPOSE 5800
