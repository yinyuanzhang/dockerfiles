FROM gcr.io/tensorflow/tensorflow:latest-devel

RUN git clone https://github.com/MarvinTeichmann/KittiBox.git && \
    cd KittiBox && git submodule update --init --recursive && \
    cd submodules/utils && make

RUN cd KittiBox && mkdir DATA && curl ftp://mi.eng.cam.ac.uk/pub/mttt2/models/vgg16.npy -o DATA/vgg16.npy && \
    pip install -r requirements.txt && python demo.py --input_image data/demo.png

WORKDIR /root/KittiBox
