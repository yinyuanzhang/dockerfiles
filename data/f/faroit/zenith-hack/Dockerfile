FROM pytorch/pytorch

RUN conda install pandas
#RUN conda install torchvision -c pytorch

WORKDIR /workspace

COPY model-training/dataset.py /workspace
COPY model-training/train.py /workspace
