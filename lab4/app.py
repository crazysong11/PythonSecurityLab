from flask import Flask, redirect, url_for, render_template, request
import uuid

app = Flask(__name__, template_folder='./templates')

# 用户名和密码字典
users = {'admin': '123', 'user1': '456', 'user2': '789'}

# 登录状态保存字典
sessions = {}

# 登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # 生成随机的 session_id
            session_id = uuid.uuid4().hex
            # 将 session_id 保存到 sessions 字典中
            sessions[session_id] = username
            # 设置 session_id 为 cookie
            response = redirect(url_for('index'))
            response.set_cookie('session_id', session_id)
            return response
        else:
            return "Invalid username or password"
    else:
        return render_template('login.html')

# 首页
@app.route('/')
def index():
    # 获取 cookie 中的 session_id
    session_id = request.cookies.get('session_id')
    if session_id not in sessions:
        # 如果 session_id 不存在，则重定向到登录页面
        return redirect(url_for('login'))
    else:
        # 根据用户名判断用户类型
        username = sessions[session_id]
        if username == 'admin':
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('user'))

# admin页面
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

# 普通用户页面
@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html')

if __name__ == '__main__':
    app.run()
