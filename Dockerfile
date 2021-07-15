FROM jupyter/pyspark-notebook:8d32a5208ca1 as build

USER root

RUN apt-get update && apt-get install -y curl

USER jovyan

RUN pip install pandas==1.2.2 \
    && pip install pyarrow==2.0.0 \
    && pip install confluent-kafka==1.6.1 \
    && pip install Faker==7.0.1 \
    && pip install sseclient==0.0.27 \
    && pip install gdown==3.13.0 \
    && pip install pycld3==0.22 \
    && pip install wordcloud==1.8.1


ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

RUN echo "export PYTHONPATH=/home/jovyan/work" >> ~/.bashrc

WORKDIR /home/jovyan/work
