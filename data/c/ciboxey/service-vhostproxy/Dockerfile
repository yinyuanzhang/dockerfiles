FROM docksal/vhost-proxy:1.0

COPY conf/nginx/default.conf.tmpl /etc/nginx/default.conf.tmpl

ENTRYPOINT ["/usr/local/bin/startup.sh"]

CMD ["supervisord", "-n"]
