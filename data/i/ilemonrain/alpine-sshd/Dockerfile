# Docker AlpineLinux (Linux-on-Docker 企划的一个分支)
# 
# Dockerfile版本：20180901
# 镜像名称：ilemonrain/alpine-sshd:latest
# 作者：iLemonrain <ilemonrain@ilemonrain.com>
# 我的Blog：https://blog.ilemonrain.com/
# Docker Hub：https://hub.docker.com/r/ilemonrain/alpine-sshd/
#
# 欢迎自由使用及转载，但请保留原作者信息
# 如有任何BUG反馈，或者有好的建议，欢迎E-mail到：
# ilemonrain@ilemonrain.com

# 使用镜像源
FROM alpine:latest

# 镜像作者信息
LABEL MAINTAINER="iLemonrain <ilemonrain@ilemonrain.com>"

# 系统环境变量
ENV Env_System_RootPassword="alpine" \
    Env_System_Timezone="Asia/Shanghai"

COPY source/entrypoint.sh /usr/sbin/entrypoint.sh
COPY source/motd /etc/motd

# 系统核心组件升级
RUN ( apk --no-cache upgrade ;\
      apk --no-cache add openssh-server ;\
      sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config ;\
      echo "root:${Env_System_RootPassword}" | chpasswd ;\
      apk --no-cache add tzdata ;\
      echo "${Env_System_Timezone}" > /etc/timezone ;\
      ln -sf /usr/share/zoneinfo/${SYS_TIMEZONE} /etc/localtime ;\
      chmod +x /usr/sbin/entrypoint.sh ;\
      rm -rf /var/cache/apk/* /tmp/* )

# 默认开放端口 22
EXPOSE 22

# 启动命令行
CMD [ "sh", "/usr/sbin/entrypoint.sh" ]