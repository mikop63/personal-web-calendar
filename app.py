from flask import Flask, render_template, request
import BDquery


app = Flask(__name__)

@app.route('/')
def home():
    try:
        con = sql.connect("DataBase.db")
        BDquery.create()
        return render_template('index.html')
    except:
        return 'error'



if __name__ == '__main__':
   app.run(debug=True,
            host='0.0.0.0',
            port=8080)
