FROM rundeck/rundeck:SNAPSHOT
MAINTAINER Kazuhisa Kumagai <k-kumagai@ts.tv-osaka.co.jp>

USER root

RUN curl -Lo /home/rundeck/libext/rundeck-slack-incoming-webhook-plugin-0.11.jar https://github.com/higanworks/rundeck-slack-incoming-webhook-plugin/releases/download/v0.11.dev/rundeck-slack-incoming-webhook-plugin-0.11.jar
RUN (\
  mkdir /home/rundeck/etc/rundeck;\
  chown rundeck:rundeck /home/rundeck/etc/rundeck;\
  ln -s /home/rundeck/etc/rundeck /etc/rundeck;\
)
