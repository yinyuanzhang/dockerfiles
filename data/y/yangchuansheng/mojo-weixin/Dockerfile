FROM perl:5.22
MAINTAINER sjdy521 <sjdy521@163.com>
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN cpanm Encode::Locale IO::Socket::SSL Mojolicious Mojo::Weixin \
    && cpanm Mojo::SMTP::Client \
    && cpanm IP::IPwhere IP::QQWry \
    && cpanm --mirror http://mirrors.163.com/cpan/ ZHOUYI::ZhanPu \
    && cpanm Term::ANSIColor \
    && mkdir /root/weixin
WORKDIR /root/weixin
CMD perl weixin.pl -e 'Mojo::Weixin->new(log_encoding=>"utf8")'