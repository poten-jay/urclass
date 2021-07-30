# __init__.py

from flask import Flask,  render_template
from ck_app.routes import user_routes   # 블루프린트 관련 나중에 추가한 것

app = Flask(__name__)  # 실행하면 ck_app 이 앱의 이름이 됨
app.register_blueprint(user_routes.bp)  # 블루프린트 관련 나중에 추가한 것

# FLASK_APP=ck_app flask run 


# @ <- 데코레이트
@app.route('/')   # 어플 주소 + / 일때 실행하라. -> http://127.0.0.1:5000/
def index():
    apple = 'apple'     # 설정한 apple 은 index.html 에서 쓸수 잇음 진자: 8분 
    return render_template('index.html', apple=apple) 


## 세부 엔드포인트  

# http://127.0.0.1:5000/index/4
@app.route('/index/<num>')
def index_number(num):
    return 'Welcome to Index %i' % int(num)

# http://127.0.0.1:5000/user/kelly
@app.route('/user/', defaults={'user_id': 'Check your id'})  # 주소에 /user/ 까지만 했을 때 오류 방지
@app.route('/user/<user_id>')
def user_index(user_id):
    return f'Here is your user id: {user_id}'


########### 라우팅이 많아지면 개 복잡아짐 => 블루프린트 사용
# app 폴더 하위에 routes 폴더 만들고, routes 폴더 하위에 user_routes.py 를 만들고 코드를 씀

# from ck_app.routes import user_routes

# app.register_blueprint(user_routes.bp)

#를 위에서 설정해 줘야 작동을 함