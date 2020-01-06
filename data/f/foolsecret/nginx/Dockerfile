FROM    alpine
LABEL   Author Titor <foolsecret@163.com>

# 创建服务器默认 web 根目录
WORKDIR /
RUN     mkdir www && \
        cd www && \
        echo "Hello world!" > index.html

# 创建 nginx PID 文件
WORKDIR /run/
RUN     mkdir nginx && \
        cd nginx && \
        touch nginx.pid

# 更改配置文件
WORKDIR /etc/nginx/conf.d/
COPY    conf.d/default.conf .

# 更新系统
WORKDIR /
RUN     apk update && \
        apk upgrade

RUN     apk add nginx

# 对外端口号
EXPOSE  80

# 挂载目录
VOLUME  www

# 启动命令
CMD ["nginx", "-g", "daemon off;"]