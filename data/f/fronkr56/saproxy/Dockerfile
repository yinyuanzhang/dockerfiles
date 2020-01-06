FROM fronkr56/alpinebase
EXPOSE 8082
ADD *.py /home/vlc/
ADD *.sh /home/vlc/
ADD streamlinkrc /home/vlc/
ADD *.conf /etc/supervisor/conf.d/
RUN chmod +x /home/vlc/*.sh && rm /etc/supervisor/conf.d/keepalive.conf
