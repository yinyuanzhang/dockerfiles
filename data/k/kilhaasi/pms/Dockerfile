FROM plexinc/pms-docker:latest

RUN apt update && apt install -y cron unionfs-fuse nmon unzip
RUN curl https://rclone.org/install.sh | bash
COPY root /

ENTRYPOINT ["/init"]
