FROM kukielka/nginx-rtmp-ffmpeg
ADD video.mp4_* /opt/nginx/html/vod/
ADD   nginx.conf /opt/nginx/conf/nginx.conf
ADD ENTRYPOINT.SH /ENTRYPOINT.SH
RUN cat /opt/nginx/html/vod/video.mp4_* > /opt/nginx/html/vod/video.mp4 \
  && rm -f /opt/nginx/html/vod/video.mp4_*
EXPOSE 1935
EXPOSE 8080
WORKDIR /
ENTRYPOINT ["sh","ENTRYPOINT.SH"]