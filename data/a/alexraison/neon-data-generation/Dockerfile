FROM python:3

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./generate_test_data.py" ]
