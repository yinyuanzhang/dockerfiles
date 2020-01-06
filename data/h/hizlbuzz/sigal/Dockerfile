FROM python:3.6
RUN pip3 install sigal 
RUN mkdir /sigal /src /html
COPY ./sigal.conf.py /sigal
CMD cd /sigal && sigal build /src /html
