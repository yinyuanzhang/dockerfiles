FROM yurz/pybase:latest

LABEL authors="Yuri Zhylyuk yuri@zhylyuk.com"

RUN \
    apt-get -y update \
    && apt-get -y install git \
    && conda update conda \
    && conda install -y -c conda-forge pip pandas azure \
        requests lxml pytz SQLAlchemy psycopg2 pymssql mysql \
        pysftp pysmbclient xlrd openpyxl xlsxwriter \
    && pip install --upgrade \
        git+https://bitbucket.org/yurz/datautils-python \
    && conda clean -y -a \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{cache,log}/ \
    mkdir /app
WORKDIR /app
CMD ["python", "./app.py"]