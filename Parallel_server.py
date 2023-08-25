from concurrent import futures
import time
import grpc
import ParallelSum_pb2
import ParallelSum_pb2_grpc
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
class ParallelSumservicer(ParallelSum_pb2_grpc.ParallelSumServicer):
    def ReturnSum(self,request,context):
        print("Parallel Server Started:")
        print(request)
        ARR2=  ParallelSum_pb2.ARR2()
        arr1 = list(request.arr1.split(" "))
        arr2 = list(request.arr2.split(" "))
        arr3 = [0 for element in range(len(arr2))]
    
        def parallel_sum(i):
                arr3[i]=int(arr1[i])+int(arr2[i])
                return arr3
        start = time()

        processes = []
        with ThreadPoolExecutor(max_workers=5) as executor:
            for i in range(len(arr1)):
                processes.append(executor.submit(parallel_sum, i))

        # for task in as_completed(processes):
        #     print(task.result())


        # for i in range(len(arr1)):
        #     arr3[i] = int(arr1[i])+int(arr2[i])
        ARR2.message = f"sum of array is : {arr3}"
        return ARR2
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ParallelSum_pb2_grpc.add_ParallelSumServicer_to_server(ParallelSumservicer(),server)
    server.add_insecure_port("localhost:3001")
    server.start()
    server.wait_for_termination()

if __name__=="__main__":
    serve()