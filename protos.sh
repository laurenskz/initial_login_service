#!/bin/bash
mkdir -p ./com/baboea/models ./com/baboea/services
python3 -m grpc_tools.protoc -I./protos/foodopt --python_out=./ --pyi_out=./ --grpc_python_out=./ ./protos/foodopt/com/baboea/models/*.proto
python3 -m grpc_tools.protoc -I./protos/foodopt --python_out=./ --pyi_out=./ --grpc_python_out=./ ./protos/foodopt/com/baboea/*.proto
python3 -m grpc_tools.protoc -I./protos/foodopt --python_out=./ --pyi_out=./ --grpc_python_out=./ ./protos/foodopt/com/baboea/services/*.proto