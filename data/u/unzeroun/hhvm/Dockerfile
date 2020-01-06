FROM unzeroun/base

RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449
ADD hhvm.list /etc/apt/sources.list.d/hhvm.list

RUN aptitude update -y
RUN aptitude install -y hhvm

ADD hhvm.ini /etc/hhvm/hhvm.ini

EXPOSE 9000

ENTRYPOINT ["hhvm"]
CMD ["--config", "/etc/hhvm/hhvm.ini", "--mode", "server"]
