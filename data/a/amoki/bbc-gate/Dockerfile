FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV API_URL=http://localhost

ADD NFC-Reader-Library-4.010-2.deb /opt

RUN apt-get update && \
	apt-get install -y build-essential cmake && \
	yes | dpkg -i /opt/NFC-Reader-Library-4.010-2.deb

RUN pip3 install pipenv
WORKDIR /opt
ADD Pipfile /opt
ADD Pipfile.lock /opt
RUN pipenv install --deploy --system
COPY ./ /opt
CMD ["sh", "/opt/entrypoint.sh"]
