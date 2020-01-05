FROM ubuntu:latest

RUN apt-get update && apt-get install -y \ 
python \
snmp \
xvfb \
wkhtmltopdf

ENV TZ=America/Sao_Paulo

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD [ "python", "/repository/python/heatmap.py" ]
