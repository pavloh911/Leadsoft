# Evaluation development task
## Solution consists of 3 components, which are connected with each other:
1. Simple website with several pages, theme/style is up to you. End-user gets its own id number,  which is stored in cookie. For each web page visiting, information of {end_user_id,  web_page_url} is sent to a server (second component).
2. Server gets the information from the first component and sent this information to the third  component.
3. Admin website, which gets the information from the Server {end_user_id, web_page_url} and  list this information grouped by end_user_id. It is up to you how to present the information.

# Additional technical requirements
1. Communication between second and third component is done via websocket.

#Next languages and technologies, which used in the task:

• Python (Django)
• Websockets

## Setup
### Front
```bash
cd front
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Server
```bash
cd server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 7000
```
view http://127.0.0.1:7000/ and server start to work

