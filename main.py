from sanic import Sanic, response
from sanic.response import json
from sanic_auth import Auth
import database as db

app = Sanic("API")
auth = Auth(app)


@app.route('/registration', methods=['POST'])
async def login(request):
    print(request.body) # clean after
    data = eval(request.body)
    username = data.get('username')
    password = data.get('password')
    db.register_user_data_db(username, password)
    print(f"User: {username}, password: {password}")
    return json({'usernname': {username},
                 'password':{password}})


@app.route('/login', methods=['POST'])
async def login(request):
    message = ''
    data = eval(request.body)
    username = data.get('username')
    password = data.get('password')
    # fetch user from db
    token = db.login_user_db(username, password)
    #auth.login_user(request, user=username)
        #return response.redirect('/profile')    что это. что надо вместо этого error message?
    return response.json({'usernname': {username},
                          'password':{password},
                          'token':{token}})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
  db.create_table()



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