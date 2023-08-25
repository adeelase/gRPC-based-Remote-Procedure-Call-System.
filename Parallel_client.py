import ParallelSum_pb2_grpc
import ParallelSum_pb2
import time
import grpc



def run():
    with grpc.insecure_channel("localhost:3001") as channel:
        stub = ParallelSum_pb2_grpc.ParallelSumStub(channel)

        print("Enter The Arrays to be Added")

        #arr1 = input()
        #arr2 = input()
        #print(arr1,type(arr1))
        #print(arr2)
        ARR1 = ParallelSum_pb2.ARR1(arr1 ="1 2 3 4 5",arr2 = "1 2 3 4 5")
        result  = stub.ReturnSum(ARR1)
        print("The sum of Both arrays is:")
        print(result)

if __name__=="__main__":
    run()