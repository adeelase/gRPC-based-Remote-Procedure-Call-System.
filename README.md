# gRPC-based-Remote-Procedure-Call-System.
This project was created for the completion of Distributed Systems course during my Mtech 2nd semester,Here I have designed a gRPC-based Remote Procedure Call system wherein the client dispatches two integer arrays to the server. Subsequently, the server efficiently computes the sum of their corresponding indices in parallel through multithreading, returning the result of this operation in the form of another array to the client.

About Remote Procedure Implemented in this Project:

In this Assignment the task of the server is:

⦁ Take 2 Integer Arrays as Input.

⦁ Calculate the sum of their corresponding Indices in Parallel using
  Multithreading and
  
⦁ Finally Output the result of the above operation in another array and return it to the client which will then print the result.

#DESIGN SPECIFICATIONS.

Used the following Parameters to Develop Our System:

Programming Language - Python 3.0 or Above.

Framework - gRPC.

IDE - VS Code.

#Files involved:

⦁ A .proto file.

⦁ Server.py

⦁ Client.py


#Procedure:

⦁ Firstly ,We created .proto file stating the proto version that
we will use( proto3 here) and the service that our Server will
Provide and Defining the message type that it will take as
Input and give as Output.

⦁ Then we are going to compile this .proto file using the
command "py -m grpc_tools.protoc -I./ --python_out =. --
grpc_python_out =. parallel_sum.proto" which will
generate two stub files namely ParallelSum_pb2 and
ParallelSum_pb2_grpc.

⦁ Then we run our Server on one terminal/machine using the command "py .\ParallelSearver.py" which is build upon a 
grpc.server Framework and contains the definition of the
service ParallelSum present in our proto file.

⦁ Server will be listening on Port no. 3001


⦁ Lastly we run our Client on a different terminal/machine using the command  "py .\Parallelclient.py" Which will call the Procedure
Parallel Sum Take the Two Input Arrays and will pass them
to the server to be executed on the server.

