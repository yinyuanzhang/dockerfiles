FROM python:latest
WORKDIR /usr/src/dfs_namenode
COPY . .
RUN pip install --no-cache -r requirements.txt
EXPOSE 5000
CMD ["python","server.py"]
