FROM magicalion/singleuser:build

USER $NB_UID

## install test job env
#RUN source $LOCAL_DIR/bin/virtualenvwrapper.sh && \
#    workon basenv && \
#    pip --default-timeout=100 install redis

EXPOSE 8888
WORKDIR /home/$NB_USER/work

USER root

ADD course_tests /home/jovyan/work/course_tests
RUN chown jovyan:users /home/jovyan/work/course_tests

ADD run_test_job.sh /home/jovyan/run_job.sh
RUN chown jovyan:users /home/jovyan/run_job.sh

ADD job_funcs.py /home/jovyan
RUN chown jovyan:users /home/jovyan/job_funcs.py

USER $NB_UID

RUN mkdir -p /home/jovyan/submissions/

CMD ['bash', '/home/jovyan/run_job.sh']
