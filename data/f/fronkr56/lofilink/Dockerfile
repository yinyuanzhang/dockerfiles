FROM fronkr56/alpinebase
RUN sed -i -e 's/debug/info/' /etc/supervisord.conf
EXPOSE 8080
ADD *.sh /home/vlc/
ADD *.conf /etc/supervisor/conf.d/
RUN chmod +x /home/vlc/*.sh && rm /etc/supervisor/conf.d/keepalive.conf
