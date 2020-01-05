FROM python
ADD . /app
WORKDIR /app
RUN	apt-get update &&\
	apt-get install -y --no-install-recommends ruby-sass &&\
	pip install --no-cache-dir -r requirements.txt &&\
	pip install --no-cache-dir psycopg2 &&\
	make SASS=sass &&\
	apt-get purge -y ruby-sass && apt-get -y autoremove
CMD ["/app/docker-entry.sh"]
