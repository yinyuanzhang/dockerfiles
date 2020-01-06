FROM python:alpine
WORKDIR /
ENV WEB_CONCURRENCY=1
COPY ./app /app
RUN pip install -r app/requirements.txt &&\
    mkdir /home/shop &&\
    cp app/static/images/* /home/shop
CMD echo $FLAG > /app/flag.txt; export FLAG=not_flag; $FLAG=not_flag;export SECRET_KEY=`python -c "import string;import random;print(''.join(random.sample(string.ascii_letters*5+string.digits*5,40)));"`;export;python app/app.py
