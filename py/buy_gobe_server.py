# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from concurrent import futures

import eatery_pb2
import eatery_pb2_grpc
import grpc


# Redefine the BuyGobe method with your own logic
class Buyer(eatery_pb2_grpc.earteryServicer):
    def BuyGobe(self, request, context):
        total_amount = request.plantain + request.rice + request.beans
        if request.vegetables:
            return eatery_pb2.MenuResponse(
                message=f"Gobe costs -  {total_amount}. You bought Gobe without Veges"
            )
        return eatery_pb2.MenuResponse(
            message=f"Gobe costs -  {total_amount}. You bought Gobe with Veges"
        )


def serve():
    port = "50051"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    eatery_pb2_grpc.add_earteryServicer_to_server(Buyer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()

    print("Server started, listening on " + port)

    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
