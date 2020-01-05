FROM python:3.7-slim
WORKDIR /Project/demo
#RUN apt-get update
#RUN apt-get install -y gcc
#定义时区参数
ENV TZ=Asia/Shanghai

#设置时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' > /etc/timezone

#设置编码
ENV LANG C.UTF-8
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]