import socket
import cv2
import numpy

# server address and port
host='localhost'
port=8000
address = (host, port)

# create a client that connects to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

# read the image to be sent through the network
img = cv2.imread('img_fjords.jpg', 0)

# encoding parameters
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

# encoded value saved in imgEncode
result, imgEncode = cv2.imencode('.jpg', img, encode_param)

# convert to numpy array
image_array = numpy.array(imgimgEncodeencode)

# convert numpy array to string
string_data = image_array.tostring()

# sent the lenght of the image string
client_socket.send( str(len(string_data)).ljust(16));

# sent the data to the server
client_socket.send( string_data );

# close the socket connection
client_socket.close()
