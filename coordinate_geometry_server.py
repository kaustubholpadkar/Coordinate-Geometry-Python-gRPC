from concurrent import futures
import time
import grpc

import coordinate_geometry_pb2
import coordinate_geometry_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class CoordinateGeometryServicer(coordinate_geometry_pb2_grpc.CoordinateGeometryServiceServicer):

    def __init__(self):
        pass

    def Magnitude(self, request, context):
        x = request.x
        y = request.y
        dist = coordinate_geometry_pb2.Distance()
        dist.distance =  x * x + y * y
        return dist

    def CartesianDistance(self, request, context):
        point1 = request.point1
        point2 = request.point2
        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y
        dist = coordinate_geometry_pb2.Distance()
        dist.distance = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        return dist

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    coordinate_geometry_pb2_grpc.add_CoordinateGeometryServiceServicer_to_server(
        CoordinateGeometryServicer(), server
    )
    server.add_insecure_port('[::]:60051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
