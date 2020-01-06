FROM base/archlinux
LABEL name="archweechat"
MAINTAINER adjivas <adjivas@student.42.fr>
ENV HOME /root
ENV LANG en_US.UTF-8
ENV AWAY_CHECK 15
RUN pacman -Syy ;
RUN pacman -S --noconfirm weechat ;
CMD weechat --run-command "/server add freenode sendak.freenode.net -port 7000 ; \
                           /set irc.server.freenode.addresses sendak.freenode.net/7000 ; \
                           /set irc.server.freenode.ssl on ; \
                           /set irc.server.freenode.ssl_dhkey_size 1024 ; \
                           /set irc.server.freenode.autojoin \"#leloop\" ; \
                           /set irc.server.freenode.autorejoin on ; \
                           /set irc.server.freenode.autoconnect on ; \
                           /set irc.server.freenode.autoreconnect on ; \
                           /set irc.server.freenode.nicks \"$NICKS\" ; \
                           /set irc.server.freenode.username \"$USERNAME\" ; \
                           /set irc.server.freenode.realname \"$REALNAME\" ; \
                           /set irc.server.freenode.away_check $AWAY_CHECK ; \
                           /server add mozilla irc.mozilla.org -port 6697 -auto ; \
                           /set irc.server.mozilla.autojoin \"#rust-fr,#rust\" ; \
                           /set irc.server.mozilla.autorejoin on ; \
                           /set irc.server.mozilla.autoconnect on ; \
                           /set irc.server.mozilla.autoreconnect on ; \
                           /set irc.server.mozilla.nicks \"$NICKS\" ; \
                           /set irc.server.mozilla.username \"$USERNAME\" ; \
                           /set irc.server.mozilla.realname \"$REALNAME\" ; \
                           /set irc.server.mozilla.away_check $AWAY_CHECK ; \
                           /set logger.file.auto_log on ; \
                           /set weechat.look.buffer_time_format \"%H:%M\" ; \
                           /set weechat.look.separator_horizontal \"~\" ; \
                           /set weechat.bar.nicklist.position right ; \
                           /set weechat.color.chat_time gray ; \
                           /set weechat.bar.status.color_bg gray ; \
                           /set weechat.color.chat_nick_self *!lightgreen ; \
                           /set buffers.color.current_bg cyan ; \
                           /set buffers.color.number black ; \
                           /set buffers.color.hotlist_message_bg green  ; \
                           /set buffers.color.hotlist_message_fg white ; \
                           /set weechat.bar.status.hidden off ; \
                           /set weechat.bar.status.color_bg darkgray ; \
                           /set weechat.bar.status.items \"buffer_number+:+buffer_name+{buffer_nicklist_count}+buffer_filter,completion,scroll\" ; \
                           /script autoload ; \
                           /connect -all" ;
WORKDIR $HOME
