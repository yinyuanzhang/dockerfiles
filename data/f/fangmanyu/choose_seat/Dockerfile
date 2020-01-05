FROM python:3.7

WORKDIR /usr/src/app/

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -i https://pypi.douban.com/simple -r requirements.txt 
# 设置时区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

COPY . .

VOLUME ['/usr/src/app/logs', '/usr/src/app/errors']

ENTRYPOINT ["python", "/usr/src/app/main.py"]
