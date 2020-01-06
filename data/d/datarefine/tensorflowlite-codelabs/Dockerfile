  FROM tensorflow/tensorflow:1.9.0-py3
  #MAINTAINER Yusuke Saito

  RUN apt-get update && apt-get install -y --no-install-recommends \
              git

  RUN pip install --upgrade  "tensorflow==1.9.*" && \
      pip install PILLOW

  RUN git clone https://github.com/googlecodelabs/tensorflow-for-poets-2 && \
      cd tensorflow-for-poets-2 && \
      git checkout end_of_first_codelab

# copy file
 COPY TensorFlow_for_Poets_2_TFLite_Android.ipynb /notebooks/tensorflow-for-poets-2

# TensorBoard
 EXPOSE 6006
# IPython
 EXPOSE 8888

 WORKDIR "/notebooks/tensorflow-for-poets-2"

 CMD ["/run_jupyter.sh", "--allow-root"]

