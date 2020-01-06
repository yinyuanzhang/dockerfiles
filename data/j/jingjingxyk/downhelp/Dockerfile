#FROM ubuntu:latest
FROM registry.cn-beijing.aliyuncs.com/jingjingxyk/ubuntu:latest
#RUN apt-get update \
#    && apt-get install -y wget vim git curl \
#    && rm -rf /var/lib/apt/lists/*

WORKDIR /
RUN mkdir /down
ADD ./endpoint.sh /
RUN chmod a+x /endpoint.sh
WORKDIR /down
#FROM registry.cn-beijing.aliyuncs.com/jingjingxyk/ubuntu:latest

#RUN wget https://dl.pstmn.io/download/latest/linux64 -o Postman-linux-x64-6.2.2.tar.gz
#RUN  git clone https://github.com/kubernetes-incubator/external-storage.git
#RUN  git clone https://github.com/ECNUdase/pdf.git

#RUN wget http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-15.6.0.tar.gz
#RUN wget http://downloads.asterisk.org/pub/telephony/asterisk/webmin/webmin.tgz
#RUN wget http://downloads.asterisk.org/pub/telephony/dahdi-linux-complete/releases/dahdi-linux-complete-2.11.1+2.11.1.tar.gz
#RUN wget http://downloads.asterisk.org/pub/telephony/libpri/releases/libpri-1.6.0.tar.gz
#RUN wget http://downloads.asterisk.org/pub/telephony/libss7/releases/libss7-2.0.0.tar.gz
#RUN wget https://files.freeswitch.org/releases/freeswitch/freeswitch-1.8.1.tar.gz

#RUN wget https://storage.googleapis.com/kubernetes-helm/helm-v2.11.0-linux-amd64.tar.gz
#RUN curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /docker-compose
#RUN curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-Linux-x86_64" -o /down/docker-compose
#RUN curl -L "http://director.downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2018-06-29/2018-06-27-raspbian-stretch-lite.zip" -o /down/2018-06-27-raspbian-stretch-lite.zip
#RUN curl -L "http://director.downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2018-06-29/2018-06-27-raspbian-stretch-lite.zip" -o /down/2018-06-27-raspbian-stretch-lite.zip

#RUN wget https://opensource.apple.com/source/FastCGI/FastCGI-4/fcgi-2.4.0.tar.gz  -O /down/fcgi-2.4.0.tar.gz

#RUN cd /down &&  git clone https://github.com/KomaBeyond/chinese-poetry-mysql.git
#RUN cd /down &&  git clone https://github.com/chinese-poetry/chinese-poetry-zhCN.git
#RUN cd /down &&  git clone https://github.com/chinese-poetry/chinese-poetry.git
#RUN cd /down &&  git clone https://github.com/BYVoid/OpenCC.git
#RUN cd /down &&  git clone https://github.com/DoubangoTelecom/sipml5.git
#RUN cd /down &&   git clone https://github.com/versatica/JsSIP.git
#RUN cd /down &&   wget https://github.com/FiloSottile/mkcert/releases/download/v1.1.2/mkcert-v1.1.2-linux-amd64
#RUN cd /down &&   wget https://github.com/asterisk/asterisk/archive/16.0.0.zip -o asterisk-16.0.0.zip
#RUN cd /down &&   wget https://storage.googleapis.com/kubernetes-helm/helm-v2.12.3-linux-amd64.tar.gz
#RUN wget https://storage.googleapis.com/harbor-releases/release-1.7.0/harbor-offline-installer-v1.7.1.tgz
#RUN git clone https://github.com/fighting41love/funNLP.git
#RUN git clone https://github.com/CyC2018/CS-Notes.git
#RUN git clone https://github.com/shimohq/chinese-programmer-wrong-pronunciation.git
#RUN git clone https://github.com/imhuster/Enterprise-Registration-Data-of-Chinese-Mainland.git
#RUN git clone https://github.com/haoel/leetcode.git
#RUN git clone https://github.com/MisterBooo/LeetCodeAnimation.git
#RUN git clone https://github.com/huihut/interview.git
#RUN git clone https://github.com/apachecn/AiLearning.git
#RUN wget https://www.7-zip.org/a/7z1900-x64.exe
#RUN wget http://pcdown.ttrar.com/small/windowsloader_ttrar.zip
#RUN wget https://mpv.srsfckn.biz/mpv-x86_64-20181002.7z
#RUN wget http://js.xiazaicc.com/down2/windows_loader_downcc.zip
#RUN wget http://files.freeswitch.org/disk_images/FreeSWITCH-Deb8-TechPreview-latest.ova
#RUN git clone https://github.com/swoole/swoole-src.git
#RUN git clone https://github.com/chromium/chromium.git
RUN wget https://github.com/istio/istio/releases/download/1.2.5/istio-1.2.5-linux.tar.gz
RUN wget https://github.com/docker/compose/releases/download/1.25.0-rc2/docker-compose-Linux-x86_64
WORKDIR /
ENTRYPOINT exec /endpoint.sh


FROM registry.cn-beijing.aliyuncs.com/jingjingxyk/nginx-autoindex
# 清空默认存在文件
RUN rm -rf /usr/share/nginx/html/*
COPY --from=0 /down  /usr/share/nginx/html


