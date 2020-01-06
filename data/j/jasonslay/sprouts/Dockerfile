FROM jasonslay/python-selenium

ADD requirements.txt requirements.txt
ADD sprouts.py sprouts.py
RUN pip3 install --upgrade pip wheel setuptools --upgrade -r requirements.txt

ENTRYPOINT ["python3", "./sprouts.py"]
