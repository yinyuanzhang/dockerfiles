FROM python:3

WORKDIR /opt

RUN pip install flask requests wasp-eureka mysql-connector python-jose pytest pytest-allure-adaptor jsonify 
COPY API.py /opt/

COPY searchController.py /opt/
COPY register.py /opt/
COPY runAll.py /opt/
COPY search.json /opt/

EXPOSE 5001

CMD python3 ./runAll.py
