FROM centos:centos7.3.1611

LABEL maintainer="Hiro Maru <hiro.maruhashi@nysol.co.jp>"

# 基本ライブラリ
RUN yum -y update; \
    yum -y groupinstall "Development Tools"; \
    yum -y install boost-devel libxml2-devel \
                   quota \
                   nano; \
    rm -rf /var/cache/yum/*; yum clean all;

# 言語を日本語に設定（必ずyum updateやyum reinstall glibcの後に実行)
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"
# 日付を日本語に設定
RUN echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock; \
    rm -f /etc/localtime; \
    ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime;

# Work Directories
WORKDIR /work
WORKDIR /github

# ruby
RUN cd /github; git clone https://github.com/sstephenson/rbenv.git;\
    echo 'export RBENV_ROOT="/github/rbenv"' >> ~/.bash_profile;\
    echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> ~/.bash_profile;\
    echo 'eval "$(rbenv init -)"' >> ~/.bash_profile;
ENV RBENV_ROOT="/github/rbenv" \
    PATH="/github/rbenv/bin:$PATH"
RUN rbenv init -;\
    cd /github; git clone git://github.com/sstephenson/ruby-build.git;\
    cd ruby-build;\
    ./install.sh; \
    yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel; \
    rm -rf /var/cache/yum/*; yum clean all; \
    rbenv install 2.6.3; rbenv rehash; rbenv global 2.6.3;

# python
RUN cd /github; git clone https://github.com/pyenv/pyenv.git;\
    echo 'export PYENV_ROOT="/github/pyenv"' >> ~/.bash_profile;\
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile;\
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile;
ENV PYENV_ROOT="/github/pyenv" \
    PATH="/github/pyenv/bin:$PATH"
RUN yum install -y libffi-devel;\
    rm -rf /var/cache/yum/*; yum clean all;\
    pyenv init -; pyenv install 3.7.3; pyenv global 3.7.3;

# rbenv/pyenv関連パス設定
ENV PATH="$PYENV_ROOT/shims:$RBENV_ROOT/shims:$RBENV_ROOT/plugins/ruby-build/bin:$PATH"

# mcmd, mdmdex ( mbomsai, mkmeans, etc )
RUN cd /github; git clone https://github.com/nysol/mcmd.git;\
    cd mcmd; aclocal; autoreconf -i; ./configure; make; make install;\
    rm -rf /github/mcmd;\
    \
    cd /github; git clone https://github.com/nysol/mcmdex.git;\
    cd mcmdex; aclocal; autoreconf -i; ./configure; make; make install;\
    rm -rf /github/mcmdex.git;

###<<< step-b1

# zdd, take, mining, mruby, meach, view, fumi, nysol_python,etc
RUN gem install nysol-zdd;\
    gem install nysol-take;\
    gem install nysol-mining;\
    gem install nysol;\
    gem install nysol-view;\
    gem install nysol-fumi;\
    \
    cd /github; git clone https://github.com/nysol/nysol_python.git;\
    cd nysol_python; python setup.py build; python setup.py install;

# nysol_ruby
# RUN gem install nysol-ruby

#  gpmetis, JUMAN, KNP, ENJU, nkf, graphviz, R
RUN rpm -Uvh http://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/m/metis-5.1.0-12.el7.x86_64.rpm;\
    \
    cd /work; curl -O http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/juman/juman-7.01.tar.bz2; tar jxvf juman-7.01.tar.bz2;\
    cd juman-7.01; ./configure; make; make install;\
    \
    cd /work; curl -O http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/knp-4.19.tar.bz2; tar jxvf knp-4.19.tar.bz2;\
		cd knp-4.19; ./configure; make; make install; rm -rf /work/*;\
    \
		cd /github; git clone https://github.com/mynlp/enju.git;\
    cd enju; ./configure; make; make install;\
    rm -rf /github/enju;\
    \
    yum -y install epel-release nkf; \
    yum -y install 'graphviz'; \
    yum -y install R; \
    rm -rf /var/cache/yum/*; yum clean all;

###<<< step-b2

# TeX
RUN yum -y install fontconfig-dev;\
    mkdir /work/install-tl-unx; cd /work/install-tl-unx; curl -O http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz;\
    tar xvf install-tl-unx.tar.gz --strip-components=1;\
    echo "selected_scheme scheme-basic" >> /work/install-tl-unx/texlive.profile;\
    /work/install-tl-unx/install-tl -profile /work/install-tl-unx/texlive.profile --repository http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/tlnet/;\
    TEX_LIVE_VERSION=$(/work/install-tl-unx/install-tl --version | tail -n +2 | awk '{print $5}');\
    ln -s "/usr/local/texlive/${TEX_LIVE_VERSION}" /usr/local/texlive/latest;\
    yum -y install http://mirrors.ctan.org/support/texlive/texlive-dummy/EnterpriseLinux-7/texlive-dummy-2012a-1.el7.noarch.rpm;\
    rm -rf /var/cache/yum/*; yum clean all;
ENV PATH="/usr/local/texlive/latest/bin/x86_64-linux:$PATH"
RUN tlmgr install latexmk;\
    tlmgr install collection-langjapanese;\
    tlmgr install collection-latexextra;\
    tlmgr install collection-fontsrecommended;\
    tlmgr install collection-fontutils;\
    tlmgr install multirow;

###<<< step-b3

# 日本語フォント for matplotlib
COPY IPAfont00303.zip /usr/share/fonts
RUN unzip -d /usr/share/fonts /usr/share/fonts/IPAfont00303.zip

# application用 (python, ruby, node.js)
RUN pip install --upgrade pip;\
    pip install flask;\
    pip install -U flask-cors;\
    pip install gevent-websocket;\
    \
    gem install thin;\
    gem install sinatra;\
    gem install sinatra-contrib;\
    \
    yum -y install nodejs;\
    rm -rf /var/cache/yum/*; yum clean all;

# Rライブラリ
RUN R -e "install.packages('igraph', repos='http://cran.rstudio.com/')";\
    R -e "install.packages('glmnet', repos='http://cran.rstudio.com/')";\
    R -e "install.packages('ROCR', repos='http://cran.rstudio.com/')";\
    R -e "install.packages('tgp', repos='http://cran.rstudio.com/')";\
    R -e "install.packages('arulesSequences', repos='http://cran.rstudio.com/')";\
    R -e "install.packages('LPCM', repos='http://cran.rstudio.com/')";\
    R -e "install.packages('LICORS', repos='http://cran.rstudio.com/')";

# pythonライブラリ
RUN pip install pip-review;\
    \
    pip install jupyterhub;\
    npm install -g configurable-http-proxy;\
    pip install notebook;\
    \
    pip install numpy;\
    pip install scipy;\
    pip install pandas -U;\
    pip install matplotlib;\
    pip install bokeh;\
    pip install plotly;\
    pip install 'holoviews[recommended]';\
    pip install mglearn;\
    pip install scikit-learn;\
    pip install scikit-image;\
    pip install opencv-python;\
    pip install python-Levenshtein;\
    pip install python-igraph;\
    pip install param;\
    pip install pyper;\
    pip install keract;\
    pip install pydot;\
    pip install pydotplus;\
    pip install networkx;\
    pip install ipywidgets;\
    pip install requests;\
    pip install beautifulsoup4;\
    pip install lxml;\
    \
    rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm;\
    yum -y install mysql-community-client; rm -rf /var/cache/yum/*; yum clean all;\
    pip install pymysql;\
    pip install ipython-sql;

# ユーザー環境設定
ENV LD_LIBRARY_PATH /usr/local/lib

RUN yum -y install sudo;\
    rm -rf /var/cache/yum/*; yum clean all;\
    groupadd -g 79357 nysol;\
    useradd -g 79357 -m -u 79357 nysol;\
    echo "nysol:nysol" | chpasswd;\
    echo "nysol ALL=(ALL) ALL" >> /etc/sudoers;\
    echo "Defaults secure_path=\"$PYENV_ROOT/shims:$RBENV_ROOT/shims:$RBENV_ROOT/plugins/ruby-build/bin:$PYENV_ROOT/bin:$RBENV_ROOT/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"" >> /etc/sudoers
RUN rm -rf /work/*

WORKDIR /home/nysol
