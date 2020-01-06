FROM python
MAINTAINER Soumyadeep Paul <soumypau1@gmail.com>
RUN pip install netaddr && \
	pip install flask && \
	pip install flask-pymongo
ADD /dockerfiles/python/ipmanagement.py /ipmanagement.py
EXPOSE 5000
CMD ["python", "/ipmanagement.py"]
