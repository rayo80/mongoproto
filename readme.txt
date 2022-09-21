
1) Genere el archivo proto usando GRPC. actualmente es la mejor y mas rapida forma que conozco
para hacer la compilacion.
python -m grpc_tools.protoc -I./ zenbus.proto --python_out=. 

-I./ significa el directorio grande de trabajo
lo sgte es el directorio relativo del archivo en este caso solo va el proto file 
pues esta libre.

