FROM python:3-stretch
RUN pip install rio-rgbify
RUN sed -i.bak "s/init='epsg:3857'/epsg:3857/" /usr/local/lib/python3.7/site-packages/rio_rgbify/mbtiler.py
WORKDIR /data
ENTRYPOINT ["rio", "rgbify"]
CMD ["rio", "rgbify"]
