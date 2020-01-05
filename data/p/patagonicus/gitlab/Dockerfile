FROM sameersbn/gitlab:8.4.2
MAINTAINER Philipp Adolf <derphilippadolf@googlemail.com>

ADD entrypoint-custom.sh /sbin/
ENTRYPOINT ["/sbin/entrypoint-custom.sh"]
CMD ["app:start"]
