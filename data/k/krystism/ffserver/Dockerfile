# ffmpeg
#
# VERSION               2.8
#
FROM          alpine
MAINTAINER    krystism <krystism@gmail.com>
ENV FFMPEG_VERSION=2.8
ENV FFMPEG_DOWNLOAD_URL http://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-static.tar.xz
RUN mkdir /input /output
WORKDIR /input
RUN apk add --update curl \
	&& curl -sSL "$FFMPEG_DOWNLOAD_URL" -o ffmpeg.tar.xz \
	&& tar -xvJf ffmpeg.tar.xz \
	&& mv ffmpeg-* ffmpeg \
	&& cp ffmpeg/ffserver /usr/bin/ \
    	&& rm -rf ffmpeg \
	&& rm -rf ffmpeg.tar.xz \
	&& apk del --purge curl \
	&& rm -rf /var/cache/apk/*
CMD ["ffserver","--help"]
