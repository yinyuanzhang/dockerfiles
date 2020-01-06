FROM python:3-buster

RUN apt update && apt install -y git

RUN git clone https://github.com/byt3bl33d3r/SILENTTRINITY /opt/SILENTTRINITY &&\
	pip3 install -r /opt/SILENTTRINITY/requirements.txt

EXPOSE 5000

CMD '/opt/SILENTTRINITY/st.py'
