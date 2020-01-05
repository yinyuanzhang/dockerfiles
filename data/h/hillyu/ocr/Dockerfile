From hillyu/keras-gpu:latest
RUN pip3 install --upgrade pip setuptools && \
        pip3 install flask && \
        #pip3 install redis && \
	    rm -r /root/.cache
COPY ocr_engine.py /root/
COPY ocr_model_ep12_ba2048.h5 /root/
COPY unicode.txt /root/
WORKDIR "/root"
EXPOSE 8080
#RUN chmod +x /bin/myawesomescript
CMD  python ocr_engine.py
