FROM ilix/debian-cron

# Setup overviewer in aptitude.
ADD http://overviewer.org/debian/overviewer.gpg.asc /tmp/overviewer.gpg.asc
RUN echo "deb http://overviewer.org/debian ./" >> /etc/apt/sources.list
RUN apt-key add /tmp/overviewer.gpg.asc

# Install overviewer and dependencies.
RUN apt-get update
RUN apt-get -y install wget python-gdbm python-imaging python-numpy minecraft-overviewer

# Get Minecraft (required for texture resources).
RUN wget https://s3.amazonaws.com/Minecraft.Download/versions/1.12.2/1.12.2.jar -P ~/.minecraft/versions/1.12.2/

# Add crontab.
COPY config /config
COPY crontab /etc/cron.d/crontab
