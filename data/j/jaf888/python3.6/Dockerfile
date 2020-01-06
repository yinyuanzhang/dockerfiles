FROM alpine:latest
MAINTAINER jianganfu
# 设置时区变量
ENV TIME_ZONE Asia/Shanghai
# 此时alpine的3.8库比较完善
RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.8/main/" > /etc/apk/repositories \
	&& echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.8/community/" >> /etc/apk/repositories \
	&& apk update \
	&& apk upgrade \
	#安装bash
	&& apk add --no-cache bash \
	python3 \
	build-base python3-dev openssl openssl-dev libffi-dev ca-certificates py3-pip \
	# 内核编译时需要用到linux-headers
	linux-headers pcre-dev \
	# 因为需要使用PIL库，所以需要添加PIL的依赖库，如果不需要可删除
	jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
	# 设置全局pip下载加速
	&& pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
	# 更新pip3，但会安装pip,当只有python3时，pip3和pip是一样的效果
	&& pip3 install --default-timeout=100 --no-cache-dir --upgrade pip \
	# 设置链接
	&& if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \
	&& if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi \
	# 修改默认的bash
	&& sed -i '1{/root/s;/bin/ash;/bin/bash;}' /etc/passwd \
	#删除缓存
	&& rm -rf /root/.cache /root/.bash_history /tmp/*
# 默认进入bash
CMD ["/bin/bash"]
	


