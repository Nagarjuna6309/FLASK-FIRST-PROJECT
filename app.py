from flask import Flask,render_template


FAI=Flask(__name__)

@FAI.route('/naga')
def naga():
    return ('brock lesnar')

@FAI.route('/brock')
def brock():
    return render_template('brock.html')


if __name__=='__main__':
    FAI.run(debug=True)