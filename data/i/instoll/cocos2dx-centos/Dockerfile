FROM centos:7

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
ENV NDK_ROOT /opt/android-ndk
ENV ANDROID_SDK_ROOT /opt/android-sdk
ENV PATH="$ANDROID_SDK_ROOT/tools/bin:${PATH}"
ENV COCOS_X_ROOT /cocos2dx
ENV COCOS_CONSOLE_ROOT /cocos2dx/tools/cocos2d-console/bin
ENV COCOS_TEMPLATE_ROOT /cocos2dx/templates
ENV ANT_ROOT /opt/apache-ant-1.10.5/bin/
ENV PATH="/cocos2dx/tools/cocos2d-console/bin:${PATH}"
ENV PATH="/cocos2dx/template:${PATH}"
ENV JAVA_HOME /usr/java/jdk1.8.0_131
ENV PATH="$JAVA_HOME/bin:${PATH}"
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"

RUN yum install -y epel-release && \
    rpm -Uvh https://rpm.nodesource.com//pub_8.x/el/6/x86_64/nodejs-8.14.0-1nodesource.x86_64.rpm && \
    yum install -y libtool bison tk-devel zip unzip wget which nodejs tar patch libyaml-devel libffi-devel autoconf automake make kernel-devel kernel-headers gcc gcc-c++ bzip2-devel git python perl file zlib zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel gdbm-devel python-devel python-pip && \
    pip install pip --upgrade && \
    git clone https://github.com/yyuu/pyenv.git $HOME/.pyenv && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    eval "$(pyenv init -)" && \
    pyenv install 3.6.0 && \
    pyenv install 2.7.10 && \
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm && \
    rpm -ivh jdk-8u131-linux-x64.rpm && rm -rf jdk-8u131-linux-x64.rpm && \
    cd /opt && \
      wget -q https://dl.google.com/android/repository/android-ndk-r17b-linux-x86_64.zip && \
      unzip *ndk*linux*.zip && \
      rm *ndk*linux*.zip && \
      mv *ndk* /opt/android-ndk && \
      mkdir -p /opt/android-sdk && cd /opt/android-sdk && \
      wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip && \
      unzip *tools*linux*.zip && \
      rm *tools*linux*.zip && \
    cd /opt && \
      wget http://ftp.jaist.ac.jp/pub/apache/ant/binaries/apache-ant-1.10.5-bin.tar.gz && \
      tar zxvf apache-ant-1.10.5-bin.tar.gz && \
      ln -fs /opt/apache-ant-1.10.5/bin/ant /usr/bin/ant && \
      rm -rf apache-ant-1.10.5-bin.tar.gz && \
    git clone https://github.com/cocos2d/cocos2d-x.git /cocos2dx && \
    cd /cocos2dx && \
      git checkout cocos2d-x-3.17 && \
      /cocos2dx/download-deps.py --remove-download yes && \
    cd /cocos2dx && \
      git submodule update --init && \
    (while sleep 1; do echo "y"; done) | sdkmanager --licenses && \
    cd /cocos2dx && \
      ./setup.py && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
