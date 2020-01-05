FROM python:3

RUN apt-get update && apt-get install -y software-properties-common && apt-get install libdigest-sha3-perl && apt-get install -y git
RUN pip install pystrich

RUN git clone https://github.com/pflima92/ethereum-generate-wallet.git
RUN cd ethereum-generate-wallet && pip install -r requirements.txt

CMD ["./ethereum-generate-wallet/ethereum-wallet-generator.py"]
