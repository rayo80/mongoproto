
1) Genere el archivo proto usando GRPC asi que esto ya no se usa
comando de generacion com
python -m grpc_tools.protoc -I./ zenbus.proto --python_out=. --grpc_python_out=.   
-I./ significa el directorio grande de trabajo
lo sgte es el directorio relativo del archivo en este caso solo va el proto file 
pues esta libre.

