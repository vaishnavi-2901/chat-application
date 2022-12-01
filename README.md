# chat-application
real time chat application for PoC purpose using django channels


# websocket-chat-application


pre-requisites


pip install django==2.2.6
pip install channels
pip install asgiref


Run redis server using command: redis-cli on terminal

# migrate 
run python ./manage.py migrate

# create superuser
run python ./manage.py createsuperuser

# to start server
run python ./manage.py runserver
