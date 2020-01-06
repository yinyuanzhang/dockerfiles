FROM alpine
RUN apk --update add logrotate
RUN echo "*/5 * * * * /usr/sbin/logrotate /etc/logrotate.conf --state /logrotate-state --verbose" >> /etc/crontabs/root
ADD logrotate.conf /etc/logrotate.conf
CMD ["crond", "-f"]