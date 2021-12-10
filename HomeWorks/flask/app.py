from flask import Flask, request, render_template, url_for
# import seriesFunction as s
import model
import Mysql_pwd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static/css/style.css')
# , static_url_path='/source', static_folder='./static' -> 當不想把static寫進網址時，可以上面那行的參數加上這串就可以更改名稱(/source)
# 預設都會是static
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = Mysql_pwd.pwd["pwd"]
db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = "item"

    ItemNo = db.Column(db.String(10), primary_key=True, nullable=False)
    ItemName = db.Column(db.String(60), nullable=False)
    PFNo = db.Column(db.SmallInteger, nullable=False)
    ItemID = db.Column(db.SmallInteger, nullable=False)
    Price = db.Column(db.Float)
    Brand = db.Column(db.String(16))
    Cate = db.Column(db.String(45))
    URL = db.Column(db.Text, nullable=False)
    IMG_Path = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "Item %s" % self.ItemName

# @app.route('/') # 自己的模板，暫時作廢
# def index():
#     return render_template("index.html")


@app.route('/trend.html', methods= ['GET'])
def trend():
    return render_template('trend.html')


@app.route('/showIkea')
def showIkea():
    ikeaData = model.getStaff()
    column = ['_id', 'name', 'id', 'price', 'URL', 'imgPath']
    return render_template('showIkea.html', ikeaData=ikeaData,
                                              column=column)
# 用函數呼叫MODEL 把MySQL欄位資料拿出來

@app.route('/showPinkoi')
def showPinkoi():
    pinkoiData = model.getStaff()
    column = ['_id', 'name', 'id', 'price', 'URL', 'imgPath']
    return render_template('showPinkoi.html', pinkoiData=pinkoiData, column=column)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#11/06 13:45 Jinja2
#11/06 15:52 Jinja2 Model 開始