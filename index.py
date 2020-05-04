from sanic import Sanic, response
from sanic.response import json
from sanic_auth import Auth
import tables
import database
import random
import string

def

app = Sanic("API")

@app.route('/registration', methods=['POST'])
async def login(request):
    print(request.body) #clean
    data = eval(request.body)
    username = data.get('username')
    password = data.get('password')
    if not user_exist_chesk(username, password):
        return msg'Pair user+password not found in db'#error massage

    print(f"User: {username}, password: {password}")
    return json({'usernname': {username},
                 'password':{password}})

#tables.registration_new_user_db(name=username, password=password) #откуда вызывать записть данных в бд

auth = Auth(app)

@app.route('/login', methods=['POST'])
async def login(request):
    message = ''

    username = request.form.get('username')
    password = request.form.get('password')
    # fetch user from database
    user = database.DEFAULT_PATH.get(name=username) #how to pass database
    if user and user.check_password(password):   # check_password????
        auth.login_user(request, user)
        #return response.redirect('/profile')    что это. что надо вместо этого error message?
    return response.json({'usernname': {username},
                          'password':{password}})

'''
@app.route('/login', methods=['POST'])    # пример
async def login(request):
    print(request)
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"User: {username}, password: {password}")
    return json({'usernname': {username},
                 'password':{password}})
'''

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)

'''
#def registration_info():


 async def registration(request):
    return json({'login':'password'})


if __name__ == "__main__":
    web_app = Sanic()
    web_app.add_route(registration,'/registration')
    web_app.run(host='0.0.0.0', port=8000)

    @web_app.route(methods=['GET'], uri='/api/users/<user_id>')
    async def get_user_by_id_method(request, user_id):
        user = await db_api.get_user_by_id(user_id)
        return json(user, status=200)

    @web_app.route(methods=['PUT', url='/api/users/<user_id>'])
    async def update_user_by_id_method(request, user_id)
        user = await db_api.update_user_by_id(user_id,request.json)
        return json(user,status=200)

'''