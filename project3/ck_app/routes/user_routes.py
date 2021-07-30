# user_routes.py

from flask import Blueprint

            # 'user' : 블루프린트의 이름
            # __name__ : 실제 블루프린트의 임폴트 했을 때 이름
            # url_prefix : 해당 블루프린트 앞에 모든 주소 앞에 붙음 , / 는 필수
bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/')  #=>  http://127.0.0.1:5000 + /main + /
def index():
    return 'MAIN index kkkkkk'


