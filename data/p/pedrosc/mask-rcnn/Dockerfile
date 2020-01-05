FROM waleedka/modern-deep-learning
RUN git clone https://github.com/pchataignier/Mask_RCNN.git \
	&& cd Mask_RCNN && pip3 install -r requirements.txt \
	&& python3 setup.py install
WORKDIR /root/Models
COPY preTrainedModelsList ./.preTrainedModelsList
RUN cat .preTrainedModelsList | cut -d ' ' -f 2 >> tmp \
	&& wget -i tmp \
	&& rm tmp \
	&& echo 'export DOWNLOADED_MODELS_FILEPATH=/root/Models/.preTrainedModelsList' >> ~/.bashrc
