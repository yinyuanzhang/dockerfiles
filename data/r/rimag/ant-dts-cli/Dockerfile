FROM python:3.7.2

WORKDIR /opt

RUN git clone https://github.com/rimag-cloud/ant-dts-cli.git \
    && cp ant-dts-cli/start.sh ./ \
    && pip install -U setuptools \
    && pip install flask flask-restful APScheduler flasgger pynsq retry PyYAML zc.lockfile SQLAlchemy PyMySQL requests gunicorn pymssql psycopg2-binary psycopg2 suds-jurko xmltodict reportlab \
    && pip install esdk-obs-python --trusted-host pypi.org \
    && mkdir /opt/dts \
    && chmod +x start.sh \
    && rm -rf ant-dts-cli

CMD ["./start.sh"]
