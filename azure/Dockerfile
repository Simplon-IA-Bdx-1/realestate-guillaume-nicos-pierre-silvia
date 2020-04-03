FROM jupyter/minimal-notebook:latest

RUN conda install pandas==0.24.2 pyarrow==0.16.0
RUN pip install azureml-dataprep[fuse,pandas] azureml.core azureml.train azureml.pipeline
