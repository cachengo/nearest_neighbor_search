FROM python:3.6

WORKDIR /home/nn_search

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./
RUN chmod a+x boot.sh

ENV FLASK_APP=nn_search.py
ENV ANN_INDEX_LENGTH=3
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
