FROM python:3.6-onbuild

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "bot/main.py" ]