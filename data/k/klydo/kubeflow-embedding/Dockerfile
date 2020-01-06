FROM klydo/kubeflow-base

# Install modules first so this is cached and won't be rebuilt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /src/
