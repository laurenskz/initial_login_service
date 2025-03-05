FROM python:3.12
COPY requirements.txt .
WORKDIR /
RUN pip install -r requirements.txt
COPY protos.sh .
COPY food_opt_protos2/src/main/proto ./protos/foodopt/
RUN sh /protos.sh
COPY login ./login
#COPY test ./test
EXPOSE 50053

CMD python -m login.main