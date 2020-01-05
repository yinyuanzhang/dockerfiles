FROM python:3.6-stretch

COPY start.sh /start.sh
VOLUME /notebooks
WORKDIR /notebooks
EXPOSE 8888
CMD ["/start.sh"]

RUN apt-key adv --keyserver pgp.skewed.de --recv-key 612DEFB798507F25
RUN echo deb http://downloads.skewed.de/apt/stretch stretch main >> /etc/apt/sources.list
RUN echo deb-src http://downloads.skewed.de/apt/stretch stretch main >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y r-recommended
RUN apt-get install -y python3-graph-tool
RUN pip3 --no-cache-dir install numpy pandas
RUN pip3 --no-cache-dir install seaborn jupyter numexpr nibabel scikit-learn scikit-image python-slugify openpyxl xlrd
RUN pip3 --no-cache-dir install nilearn
RUN pip3 --no-cache-dir install statsmodels
RUN pip3 --no-cache-dir install requests
RUN pip3 --no-cache-dir install iptk
RUN pip3 --no-cache-dir install certifi
RUN pip3 --no-cache-dir install "elasticsearch>=6.0.0,<7.0.0"
RUN pip3 --no-cache-dir install tqdm
