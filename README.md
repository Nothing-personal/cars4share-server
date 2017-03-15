# cars4share-server
Server, which provides Cars4Share API. This project is based on Python 3.5

## Prerequisites:
* sudo apt-get install python3-pip
* pip install Django (version 1.10.6)
* pip install djangorestframework (version 3.6.2)
* pip install psycopg2 (version 2.7.1)

## API utilization examples using curl:
* GET request to API list: 
  * curl \<host>/api/
* GET request to users list:
  * curl \<host>/api/users/
* GET requset to user details: 
  * curl \<host>/api/users/{id}/; where id is 24-symbols hex number
* POST request to add User: 
  * curl --data 'your data here' \<host>/api/users/
