from flask import Flask, render_template, request

app = Flask(__name__)

# reads results from qr code and loads agreement
@app.route("/")
def nowt():
    return f"<p>Nothing to see here...</p>"

# reads results from qr code and loads agreement
@app.route("/<town>/<park>")
def survey(town, park):
    # TODO: Create User ID from DB
    userid=666
    return render_template('pis.html', userid=userid, town=town, park=park)

# reads results from qr code and loads agreement
@app.route("/s1", methods=['POST'])
def survey1():
    # TODO: Load into DB
    return render_template('s1.html', userid=request.form['userid'], town=request.form['town'], park=request.form['park'])

# reads results from qr code and loads agreement
@app.route("/s2", methods=['POST'])
def survey2():
    # TODO: Load into DB
    return render_template('s2.html', userid=request.form['userid'], town=request.form['town'], park=request.form['park'], dog=request.form['dogs'])

# reads results from qr code and loads agreement
@app.route("/s3", methods=['POST'])
def survey3():
    # TODO: Load into DB
    return render_template('s3.html', userid=request.form['userid'], town=request.form['town'], park=request.form['park'], dog=request.form['dog'])

# reads results from qr code and loads agreement
@app.route("/thankyou", methods=['POST'])
def thankyou():
    # TODO: Load into DB
    return render_template('thankyou.html')