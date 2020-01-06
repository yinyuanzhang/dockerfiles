FROM ubuntu:16.04

RUN echo 'deb http://mirrors.163.com/ubuntu/ xenial main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ xenial-security main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ xenial-updates main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ xenial-proposed main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ xenial-backports main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-security main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-updates main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-proposed main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-backports main restricted universe multiverse' > /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends \
        openssl vim curl netcat ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装nodejs
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get install -y nodejs cron && npm install -g pm2

# 安装mongo client
RUN curl https://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/3.4/multiverse/binary-amd64/mongodb-org-shell_3.4.23_amd64.deb -o mongodb-org-shell.deb \
    && dpkg -i mongodb-org-shell.deb \
    && rm mongodb-org-shell.deb

# 设置时区文件
COPY docker/conf/localtime docker/conf/timezone /etc/

WORKDIR /code

# 构建代码结构
COPY app.js package.json cmd.sh /code/
COPY common                     /code/common/
COPY config                     /code/config/
COPY controllers                /code/controllers/
COPY models                     /code/models/
COPY routes                     /code/routes/
COPY schemas                    /code/schemas/
COPY services                   /code/services/
COPY scripts                    /code/scripts/

ENV NODE_ENV production

RUN npm --registry=https://registry.npm.taobao.org install --verbose
COPY docker/qiniu/conf.js docker/qiniu/zone.js node_modules/qiniu/qiniu/

RUN (crontab -l 2>/dev/null; \
    echo 'SHELL=/bin/bash'; \
    echo '0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57  * * * * cd /code && . env.sh && node scripts/poll_sub_task.js >> poll_sub_task.log 2>&1'; \
    echo '1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52,55,58 * * * * cd /code && . env.sh && node scripts/poll_task_date_record.js >> poll_task_date_record.log 2>&1'; \
    echo '2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50,53,56,59 * * * * cd /code && . env.sh && node scripts/poll_convert_task.js >> poll_convert_task.log 2>&1'; \
    ) | crontab -

EXPOSE 3588
CMD ./cmd.sh
