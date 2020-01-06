FROM simsemand/python-ffmpeg:3.7

ENV MOVIES_PATH=/movies
ENV MOVIES_DEST_PATH=/lauritz
ENV CONFIG_PATH=/config

EXPOSE 5000

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD python lauritz.py run