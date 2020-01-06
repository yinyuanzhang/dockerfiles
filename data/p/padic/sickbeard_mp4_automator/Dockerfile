FROM python:2.7-slim

RUN \
	mkdir /tmp/.sbm4a_setup && \
	mkdir /sickbeard_mp4_automator && \
	mkdir /var/log/sickbeard_mp4_automator && \
	mkdir /mnt/host
	
WORKDIR /tmp/.sbm4a_setup

# Dependencies
RUN apt -yq update && apt -yq upgrade && apt -yq install wget git curl nano xz-utils

# Requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Get sickbeard_mp4_automator from git
RUN git clone git://github.com/padic-dev/sickbeard_mp4_automator.git /sickbeard_mp4_automator

# Get ffmpeg static release
RUN curl https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz -o ffmpeg-release-64bit-static.tar.xz
RUN tar -xf ffmpeg-release-64bit-static.tar.xz
RUN rm ffmpeg-release-64bit-static.tar.xz
#RUN cd ffmpeg-*-static
RUN cp ffmpeg-*-static/ffmpeg /usr/bin
RUN cp ffmpeg-*-static/ffprobe /usr/bin
RUN chmod 0777 /usr/bin/ffmpeg
RUN chmod 0777 /usr/bin/ffprobe

# Create profile directory
RUN mkdir /sickbeard_mp4_automator/profiles

# Add autoProcess versions
ADD ./autoprocess.ini /sickbeard_mp4_automator/autoProcess.ini

# Add built in profiles
ADD ./autoprocess.ini /sickbeard_mp4_automator/profiles/default.profile
ADD ./autoprocess-480hq.ini /sickbeard_mp4_automator/profiles/dvd.profile
ADD ./autoprocess-720hq.ini /sickbeard_mp4_automator/profiles/hd.profile
ADD ./autoprocess-1080hq.ini /sickbeard_mp4_automator/profiles/fullhd.profile
ADD ./autoprocess-avcmini.ini /sickbeard_mp4_automator/profiles/avcmini.profile
ADD ./autoprocess-hevcmini.ini /sickbeard_mp4_automator/profiles/hevcmini.profile
ADD ./autoprocess-tag.ini /sickbeard_mp4_automator/profiles/tag.profile

# Link custom profiles
RUN ln -s /config_mp4_automator /sickbeard_mp4_automator/profiles/custom

# Reset Permissions
RUN chmod 0777 -R /sickbeard_mp4_automator
RUN chmod 0777 -R /var/log/sickbeard_mp4_automator

# Create shortcuts
COPY ./sbm4a /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a

COPY ./sbm4a-dvd /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-dvd

COPY ./sbm4a-hd /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-hd

COPY ./sbm4a-fullhd /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-fullhd

COPY ./sbm4a-avcmini /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-avcmini

COPY ./sbm4a-hevcmini /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-hevcmini

COPY ./sbm4a-tag /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-tag

WORKDIR /

RUN echo 'alias ll="ls -laHh"' >> ~/.bashrc

# Cleanup
RUN rm -fR /tmp/.sbm4a_setup

VOLUME ["/mnt/host"]

CMD ["/init"]
