FROM fronkr56/alpinebase
RUN sed -i -e 's/debug/info/' /etc/supervisord.conf

ADD config /config
ADD cron/* /cron/

ADD configure/* /home/vlc/configure/
ADD *.conf /etc/supervisor/conf.d/
RUN chmod +x /home/vlc/configure/*.sh && bash /home/vlc/configure/run.sh && mv /home/vlc/*.conf /etc/supervisor/conf.d/
