FROM python:3
ADD _version.py /
ADD __main__.py /
COPY requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python","__main__.py","-H","0.0.0.0"]