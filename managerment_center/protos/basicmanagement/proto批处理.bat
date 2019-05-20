for  %%f  in  (*.proto)  do (
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. %%f
)