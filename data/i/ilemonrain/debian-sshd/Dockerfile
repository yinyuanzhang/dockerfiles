FROM debian:wheezy

LABEL MAINTAINER="iLemonrain <ilemonrain@ilemonrain.com>" \
      CODE_VERSION="20190321"

# 导入构建前使用到的文件
COPY _import/build/pre-build.sh /tmp/build/pre-build.sh

# 执行构建前准备
RUN [ "/bin/sh", "/tmp/build/pre-build.sh" ]

# 导入构建前使用到的文件
COPY _import/build/build.sh /tmp/build/build.sh

# 执行构建过程
RUN [ "/bin/sh", "/tmp/build/build.sh" ]

# 导入构建后使用到的文件
COPY _import/build/post-build.sh /tmp/build/post-build.sh

# 执行构建后工作
RUN [ "/bin/sh", "/tmp/build/post-build.sh" ]

EXPOSE 22


# 启动命令行
CMD ["/usr/sbin/sshd", "-D"]