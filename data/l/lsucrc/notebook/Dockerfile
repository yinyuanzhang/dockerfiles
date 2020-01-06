#Version 1.1
#add the base image
FROM lsucrc/crcbase
RUN  yum install -y python-pip python-devel sqlite3 libpng-devel freetype-devel netcdf-devel
RUN  pip install ipython==5.4.0
RUN  pip install scipy jupyter matplotlib netCDF4

# Add a notebook profile.
RUN mkdir -p -m 700 /root/.jupyter/custom && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = u'sha1:e6df9ba93bbb:01e2f7ad57bc7dc604037ff41922006dc28b7b14'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.tornado_settings = { 'headers': { 'Content-Security-Policy': \"frame-ancestors * \" } }" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "define(['base/js/namespace'], function(Jupyter){ Jupyter._target = '_self'; });" >> /root/.jupyter/custom/custom.js
#    echo "#ipython_notebook img{display:block; background: url(logo.png) no-repeat; background-size: contain; width: 233px; height: 33px; padding-left: 233px; -moz-box-sizing: border-box; box-sizing: border-box; }" >> /root/.jupyter/custom/custom.css 

#ADD https://raw.githubusercontent.com/lsucrc/notebook/master/logo.png /root/.jupyter/custom/logo.png
#    echo "div#site{ height: 100%; }" >> /root/.jupyter/custom/custom.css

VOLUME /notebooks
WORKDIR /notebooks

# Add Tini. Tini operates as a process subreaper for jupyter to prevent crashes.
ENV TINI_VERSION v0.9.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
