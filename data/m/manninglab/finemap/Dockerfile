FROM python:2

MAINTAINER tmajaria@broadinstitute.org

RUN pip install numpy scipy matplotlib seaborn pandas lxml svglib
RUN pip install svgutils --user

RUN apt-get update && apt-get install python3 python3-pip -y
RUN pip3 install cairosvg

RUN cd / && \
	git clone https://github.com/manning-lab/fineMap.git