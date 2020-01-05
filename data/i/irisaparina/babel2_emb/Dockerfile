FROM strawberrypie/pytorch-cuda8:v0.3 

RUN git clone https://github.com/OpenNMT/OpenNMT-py.git && cd OpenNMT-py && pip install -r requirements.txt && python setup.py install
RUN curl -s -L https://gist.githubusercontent.com/saparina/4ff9fa105f69705627e9a7f134c58654/raw/5e87209c3f510ab0648621a9614faa9b8af79a02/embeddings.py -o ~/embeddings.py && chmod +x ~/embeddings.py 
RUN curl -s -L https://raw.githubusercontent.com/saparina/babel2_emb/master/run.sh?token=AVTxeH7p89aVLPbtD3Qu9wCcs4TteCYjks5afGLZwA%3D%3D -o ~/run.sh && chmod +x ~/run.sh
RUN curl -s -L https://gist.github.com/strawberrypie/ba1f630f17d59f71862417565ceaa6f8/raw -o ~/split_parallel_corpus.py && chmod +x ~/split_parallel_corpus.py
RUN pip install gensim nltk
RUN python -m nltk.downloader punkt
