FROM python:3-alpine

# Install requirements
COPY requirements.txt /root
RUN pip install -r /root/requirements.txt
# Define default dropbox folder in docker
ENV DROPBOX_TOKEN=""
ENV DROPBOX_FOLDER="/"
ENV DROPBOX_ROOTDIR="/dropbox"

VOLUME ["/dropbox"]

COPY DropBoxSync.py /root

WORKDIR "/root"

ENTRYPOINT ["python", "DropBoxSync.py" ]
CMD ["--fromLocal"]
