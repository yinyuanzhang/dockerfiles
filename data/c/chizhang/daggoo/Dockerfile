from store/oracle/database-instantclient:12.2.0.1
# Update the sources list
WORKDIR /data
# 环境变量
ENV LANG en_US.UTF-8
# 添加requestments.txt
ADD requirements.txt /data/

ADD celeryd /etc/default/
ADD init.d/celeryd /etc/init.d/


RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
		&& yum -y update \
		&& yum install -y wget telnet net-tools gcc-c++ openssl-devel zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel xz xz-devel libffi-devel git make libxml2-devel build-essential xorg-x11-fonts-75dpi libjpeg-turbo libX11 fontconfig libXrender libXext xorg-x11-fonts-Type1.noarch psmisc vim poppler poppler-cpp-devel poppler-utils \
		&&  curl https://pyenv.run | bash \
		&& echo 'export PATH="~/.pyenv/bin:$PATH"' >> ~/.bashrc \
		&& echo 'eval "$(pyenv init -)"' >> ~/.bashrc \
		&& echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc \
		&& source ~/.bashrc \
		&& pyenv install 3.7.2 \
		&& pyenv global 3.7.2 \
		&& source ~/.bashrc \
		&& pip install --upgrade pip \
		&& pip install -r requirements.txt
#-i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# EXPOSE 8000

ADD celery_term /celery_term
CMD ["/celery_term"]
