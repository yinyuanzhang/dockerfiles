FROM python:2
RUN pip install --no-cache-dir -I jupyter
RUN useradd -m -s /bin/bash jupyter
USER jupyter
WORKDIR /home/jupyter
CMD ["sh", "-c", "jupyter notebook --ip=0.0.0.0 --no-browser"]
