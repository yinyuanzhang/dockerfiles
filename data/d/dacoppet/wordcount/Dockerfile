FROM python:3.6.4-alpine3.7
LABEL Maintainers="David COPPET - Twitter (@davidcoppet)" \
    GitRepo="https://github.com/dacoppet/aci-wordcount" \
    Version="1.X"
COPY * /
RUN pip install html2text && pip install urllib3 && pip install sh
ENV NumWords=10 MinLength=0
CMD python wordcount.py http://blog.coppet.fr/2017/01/09/get-started-with-windows-iot/