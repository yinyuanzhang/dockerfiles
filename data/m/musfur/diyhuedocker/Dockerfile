FROM python:2.7
RUN apt-get update
RUN apt-get install nmap -y
WORKDIR /app
RUN git clone https://github.com/mariusmotea/diyHue.git
WORKDIR /app/diyHue/BridgeEmulator
EXPOSE 80
CMD ["python", "HueEmulator.py"]
