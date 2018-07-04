import grpc

import coordinate_geometry_pb2
import coordinate_geometry_pb2_grpc

def magnitude(x, y, stub):
    point = coordinate_geometry_pb2.Point(x=x, y=y)
    dist = stub.Magnitude(point)
    return dist.distance

def distance(x1, y1, x2, y2, stub):
    point1 = coordinate_geometry_pb2.Point(x=x1, y=y1)
    point2 = coordinate_geometry_pb2.Point(x=x2, y=y2)
    lineSegment = coordinate_geometry_pb2.LineSegment(point1=point1, point2=point2)
    dist = stub.CartesianDistance(lineSegment)
    return dist.distance

def run():
    channel = grpc.insecure_channel('localhost:60051')
    stub = coordinate_geometry_pb2_grpc.CoordinateGeometryServiceStub(channel)

    print("--------------------Magnitude--------------------")
    x = 3.
    y = 4.
    print('x : ' + str(x))
    print('y : ' + str(y))
    print(magnitude(x, y, stub))

    print("--------------------Distance--------------------")
    x1 = 3.
    y1 = 0.
    x2 = 0.
    y2 = 4.
    print('x1 : ' + str(x1) + '   ' + 'y1 : ' + str(y1))
    print('x2 : ' + str(x2) + '   ' + 'y2 : ' + str(y2))
    print(distance(x1, y1, x2, y2, stub))

if __name__ == '__main__':
    run()
