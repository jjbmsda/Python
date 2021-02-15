Python 3.7.2rc1 (v3.7.2rc1:75a402a217, Dec 11 2018, 18:05:25) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> 
 RESTART: /Users/jangjungbu/Desktop/스터디/대학원/컴퓨터네트워크/python/hello.py 
Hello World
>>> 
 RESTART: /Users/jangjungbu/Desktop/스터디/대학원/컴퓨터네트워크/python/UDP Server.py 
Traceback (most recent call last):
  File "/Users/jangjungbu/Desktop/스터디/대학원/컴퓨터네트워크/python/UDP Server.py", line 6, in <module>
    serverSocket.bind((''.serverPort))
AttributeError: 'str' object has no attribute 'serverPort'
>>> 
 RESTART: /Users/jangjungbu/Desktop/스터디/대학원/컴퓨터네트워크/python/UDP Server.py 
The server is ready to receive

 RESTART: /Users/jangjungbu/Desktop/스터디/대학원/컴퓨터네트워크/python/UDP_Client.py 
Traceback (most recent call last):
  File "/Users/jangjungbu/Desktop/스터디/대학원/컴퓨터네트워크/python/UDP_Client.py", line 7, in <module>
    message = INPUT('Input lowercase sentence:')
NameError: name 'INPUT' is not defined
>>> 
 RESTART: /Users/jangjungbu/Desktop/스터디/대학원/컴퓨터네트워크/python/UDP_Client.py 
Input lowercase sentence:abcde
