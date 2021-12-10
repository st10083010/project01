from flask import Flask, request, render_template, url_for
# import seriesFunction as s
import model

app = Flask(__name__, static_url_path='/static/css/style.css')
# , static_url_path='/source', static_folder='./static' -> 當不想把static寫進網址時，可以上面那行的參數加上這串就可以更改名稱(/source)
# 預設都會是static


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/hello/<username>')
def hello(username):
    return 'Hello {}'.format(username)

@app.route('/hello2/<username>')
def hello2(username):
    return render_template('hello.html', username=username)
# -> jinja用法 return render_template('模板名稱', username=username)
# 第二個參數以後是把PYTHON的操作放進去



## /hello_get?name=Allen&age=22
@app.route('/hello_get')
def hello_get():
    name = request.args.get('name')
    age = request.args.get('age')
    if name == None:
        return 'Who are you?'
    if age == None:
        return 'Hello {}.'.format(name)
    outputString = "<h1>Hello {}, you are {} years old.</h1>"
    return outputString.format(name, age)

@app.route('/hello_get2')
def hello_get2():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('hello_get.html', name=name, age=age)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <form action="/hello_post" method="POST">
        What is your name?
        <br>
        <input name="username">
        <button type="submit">SUBMIT</button>
    </form>
    """
    requestMethod = request.method
    # 回傳使用者是用什麼形式將資料送進來
    if requestMethod == 'POST':
        username = request.form.get('username')
        outStr += """
        <h1>Hello {}!</h1>
        """.format(username)

    return outStr
# /hello_post說明在11/06 11:16分(以前)

#
# @app.route('/hello_post2')
# def hello_post2():
#     username = ''
#     requestMethod = request.method
#
#     if requestMethod == 'POST':
#         username = request.form.get('username')
#     return render_template(
#         'hello_post.html',
#         username=username,
#         requestMethod=requestMethod
#     )


@app.route('/showIkea')
def showIkea():
    ikeaData = model.getStaff()
    column = ['_id', 'name', 'id', 'price', 'URL', 'imgPath']
    return render_template('showIkea.html', ikeaData=ikeaData,
                                              column=column)

# 用函數呼叫MODEL 把MySQL欄位資料拿出來

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#11/06 13:45 Jinja2
#11/06 15:52 Jinja2 Model 開始