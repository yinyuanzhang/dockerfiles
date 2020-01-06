FROM python:alpine

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./
# TODO: add Makefile command to update requirements before building
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install -e '.'
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
