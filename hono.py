from flask import *#Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def entry_page() ->str:
    return render_template('entry.html',
                           the_title='HONOexcange')#最初画面

@app.route('/kansha')
def kansha_page() ->str:
    return render_template('kansha.html',
                           the_title='kannsha')#感謝画面

@app.route('/kanshacomp', methods=['POST'])
def kanshacomp_page() ->str:
    myname = request.form['myname']
    yourname = request.form['yourname']
    department = request.form['department']
    return render_template('kanshacomp.html',
                            the_title='kanshacomp',
                            the_department=department,
                            the_myname=myname,
                            the_yourname=yourname,)#感謝完了画面

@app.route('/shazai')
def shazai_page() -> str:
    return render_template('shazai.html',
                           the_title='shazai')#謝罪画面

@app.route('/shazaicomp', methods=['POST'])
def shazaicomp_page() ->str:
    myname = request.form['myname']
    yourname = request.form['yourname']
    department = request.form['department']
    return render_template('shazaicomp.html',
                            the_title='shazaicomp',
                            the_department=department,
                            the_myname=myname,
                            the_yourname=yourname,)#謝罪完了画面

@app.route('/yoyaku')
def yoyaku_page() -> str:
    return render_template('yoyaku.html',
                           the_title='yoyaku')#予約画面

@app.route('/yoyakucomp', methods=['POST'])
def yoyakucomp_page() ->str:
    myname = request.form['myname']
    yourname = request.form['yourname']
    department = request.form['department']
    return render_template('yoyakucomp.html',
                            the_title='yoyakucomp',
                            the_department=department,
                            the_myname=myname,
                            the_yourname=yourname,)#予約完了画面


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
