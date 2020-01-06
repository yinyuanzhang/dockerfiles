FROM ratsgo/embedding-cpu:1.4
MAINTAINER jistim <jiyong@yonsei.ac.kr>

RUN pip install torch==1.3.0+cpu torchvision==0.4.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

RUN pip install jupyter

RUN mkdir /notebooks/jupyter && chmod a+rwx /notebooks/jupyter
RUN mkdir /.local && chmod a+rwx /.local
WORKDIR /notebooks/jupyter
EXPOSE 8888

CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/notebooks/jupyter --ip 0.0.0.0 --no-browser --allow-root"]
