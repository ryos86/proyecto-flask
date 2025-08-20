from flask import Blueprint

taskRoute = Blueprint('task',__name__,url_prefix='/tasks')

@taskRoute.route('/')
def index():
    return 'Index'

@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show '+str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    return 'Delete '+str(id)

@taskRoute.route('/create', methods=('GET','POST'))
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    return 'Update '+str(id)