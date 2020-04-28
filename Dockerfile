FROM python:3.8

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app

ADD ./download_model.py /app/download_model.py

RUN python /app/download_model.py

#ADD ./demo_python.py /app/demo_python.py
#ADD ./demo_dag.py /app/demo_dag.py

RUN mkdir test_data
ADD ./static_templates.json /app/test_data/demo_templates.json
# RUN echo "[]" > ./test_data/demo_templates.json

ADD ./config.yaml /app/config.yaml

#RUN python /app/demo_python.py
#RUN python /app/demo_dag.py

ADD ./demo /app/demo
ADD ./setup.py /app/setup.py
RUN python setup.py install

RUN python ./demo/demo_python.py

CMD ["echo", "hello world"]
