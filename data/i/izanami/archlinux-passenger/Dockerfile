FROM izanami/archlinux-base
FROM izanami/archlinux-ruby
RUN pacman -Syu --noconfirm
RUN pacman -S base-devel --noconfirm
RUN gem install passenger
RUN $(ruby -e 'puts Gem.user_dir')/bin/passenger-install-nginx-module --auto --auto-download --prefix=/opt/nginx
RUN echo "daemon off;" >> /opt/nginx/conf/nginx.conf
WORKDIR /opt/nginx
EXPOSE 80
ENTRYPOINT ["/opt/nginx/sbin/nginx"]
