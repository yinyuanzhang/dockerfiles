FROM cerebriai/spark-py:v2.4.3


ENV EG_VER 2.0.0

RUN wget https://github.com/jupyter/enterprise_gateway/releases/download/v2.0.0/jupyter_enterprise_gateway_kernel_image_files-${EG_VER}.tar.gz && \
    tar -xvzf jupyter_enterprise_gateway_kernel_image_files-${EG_VER}.tar.gz -C /usr/local/bin/ && \
    ln -s  /usr/local/bin/kernel-launchers/scala/lib/toree-launcher_2.11-2.0.0.jar /usr/local/bin/kernel-launchers/scala/lib/toree-launcher_2.11-2.1.0.SNAPSHOT.jar

#ADD jupyter_enterprise_gateway_kernel_image_files*.tar.gz /usr/local/bin/

RUN adduser -S -u 1000 -G users jovyan && \
    chown jovyan:users /usr/local/bin/bootstrap-kernel.sh && \
	  chmod 0755 /usr/local/bin/bootstrap-kernel.sh && \
	  chmod 0777 /opt/spark/work-dir && \
    chown -R jovyan:users /usr/local/bin/kernel-launchers

USER jovyan
ENV KERNEL_LANGUAGE scala
CMD /usr/local/bin/bootstrap-kernel.sh

