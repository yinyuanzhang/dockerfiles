FROM sameersbn/ffmpeg:latest
MAINTAINER hialan.com@gmail.com 

#ENV FFMPEG_VERSION=2.7.2 \
# X264_VERSION=snapshot-20150829-2245-stable 

# http://ubuntuhandbook.org/index.php/2014/07/upgrade-mkvtoolnix-ubuntu-1404/
RUN apt-get update && apt-get install -y software-properties-common rsync\
 && add-apt-repository "deb http://www.bunkus.org/ubuntu/trusty/ ./" \ 
 && wget -O - http://www.bunkus.org/gpg-pub-moritzbunkus.txt | apt-key add - \
 && apt-get update && apt-get install -y mkvtoolnix 

# purge build dependencies, don't need 'em anymore
RUN apt-get purge -y --auto-remove software-properties-common

# cleanup
RUN rm -rf /var/lib/apt/lists/*

# please check https://raw.githubusercontent.com/JakeWharton/mkvdts2ac3/master/mkvdts2ac3.sh to get latest script
COPY mkvdts2ac3.sh /usr/bin/mkvdts2ac3.sh

VOLUME ["/data"]

ENTRYPOINT ["/usr/bin/mkvdts2ac3.sh"]
CMD ["--help"]
