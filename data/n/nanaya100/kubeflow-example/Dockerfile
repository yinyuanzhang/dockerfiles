FROM python:3.7

COPY requirements.txt .
RUN pip3 install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com -r requirements.txt
COPY model.py .
RUN chmod +x model.py

ENTRYPOINT ["python3"]
CMD ["model.py"]
