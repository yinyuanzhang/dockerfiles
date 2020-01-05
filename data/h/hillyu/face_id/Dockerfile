From hillyu/keras-gpu:latest
RUN pip3 install --upgrade pip setuptools && \
        pip3 install flask && \
        pip3 install redis && \
	    rm -r /root/.cache
COPY fd.py /root/
COPY server.py /root/
#COPY unicode.txt /root/
WORKDIR "/root"
EXPOSE 8080
#RUN chmod +x /bin/myawesomescript
CMD  python server.py
