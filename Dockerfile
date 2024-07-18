FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY protos.sh .
COPY food_opt_protos2/src/main/proto ./protos/foodopt/
RUN sh /protos.sh
COPY parse ./parse
COPY integration_test.textproto .
COPY test ./test
RUN python -m unittest

CMD python -m parse.KafkaRecipeParser