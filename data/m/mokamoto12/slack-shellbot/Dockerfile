# Set your Bots API Token on SLACKBOT_API_TOKEN
FROM python:3.6.2

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 443
CMD ["python", "./run.py"]
