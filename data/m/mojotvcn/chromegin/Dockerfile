FROM centos:7.6.1810

# 安装中文字体和chrome
RUN yum install -y wget && \
    yum install -y wqy-microhei-fonts wqy-zenhei-fonts && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
    yum install -y ./google-chrome-stable_current_*.rpm && \
    google-chrome --version && \
    rm -rf *.rpm

# 设置go mod proxy 国内代理
# 设置golang path
ENV GOPROXY=https://goproxy.io GOPATH=/gopath PATH="${PATH}:/usr/local/go/bin"
# 定义使用的Golang 版本
ARG GO_VERSION=1.13.3

# 安装 golang 1.13.3
RUN wget "https://dl.google.com/go/go$GO_VERSION.linux-amd64.tar.gz" && \
    rm -rf /usr/local/go && \
    tar -C /usr/local -xzf "go$GO_VERSION.linux-amd64.tar.gz" && \
    rm -rf *.tar.gz && \
    go version && go env;


WORKDIR $GOPATH
COPY . chromegin

RUN cd chromegin && go build -o app;

EXPOSE 6666

# 保存图片网页图片截图
VOLUME /data

CMD ["chromegin/app"]