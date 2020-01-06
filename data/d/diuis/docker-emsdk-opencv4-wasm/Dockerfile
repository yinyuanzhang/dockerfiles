FROM diuis/docker-emsdk-opencv4:v1.1.10

USER root
RUN mkdir /opencv_wasm && chown appuser /opencv_wasm

USER appuser
SHELL ["/bin/bash", "-c"]
RUN source /emsdk/emsdk_env.sh && \
    python /opencv/opencv-4.0.0/platforms/js/build_js.py --build_wasm /opencv_wasm