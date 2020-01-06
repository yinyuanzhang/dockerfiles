FROM buildpack-deps:jessie-scm
ADD execute.sh /opt
RUN chmod 755 /opt/execute.sh
ENV EXECUTE_HOME /execute
RUN apt-get update && apt-get -y install autoconf automake build-essential libass-dev libfreetype6-dev  libsdl2-dev libtheora-dev libtool libva-dev libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev  libxcb-xfixes0-dev pkg-config texinfo zlib1g-dev && wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-32bit-static.tar.xz && mkdir ffmpeg  && tar xvfJ ffmpeg-release-32bit-static.tar.xz -C ffmpeg --strip-components=1 && rm -R ffmpeg/manpages ffmpeg/qt-faststart ffmpeg/*.txt && mv ffmpeg/* /usr/bin/ && rm -R ffmpeg && rm -R *.tar.xz