FROM python:3.6-buster
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

CMD [ "python", "app.py" ]