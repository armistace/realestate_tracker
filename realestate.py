from flask import Flask,render_template,request
from connector import connector

app = Flask(__name__)

# @app.route("/houses")
# def houses():
#     conn = connector.connection()
#     results = conn.get_houses()
#     return_string = ""
#     for result in results:
#         return_string = return_string + result + " | "
#     return return_string

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/houses')
def houses():
    conn = connector.connection()
    ratings=conn.get_ratings()
    suburbs=conn.get_subrubs()
    return render_template('houses.html', ratings=ratings, suburbs=suburbs)

@app.route('/suburbs')
def suburbs():
    return render_template('suburbs.html')

@app.route('/ratings')
def ratings():
    return render_template('ratings.html')


@app.route('/data_houses', methods = ['POST', 'GET'])
def data_houses():
    if request.method == 'GET':
        return f"The URL /data_houses is accessed directly. Try going to '/houses' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print ("Addind house data to DB")
        conn = connector.connection()
        conn.insert_houses(form_data)
        return render_template('data_houses.html',form_data = form_data)


@app.route('/data_ratings', methods = ['POST', 'GET'])
def data_ratings():
    if request.method == 'GET':
        return f"The URL /data_ratings is accessed directly. Try going to '/ratings' to submit form"
    if request.method == 'POST':
        form_data = request.form
        rating = str(form_data['rating'])
        print("Inserting " + rating + "into db")
        conn = connector.connection()   
        conn.insert_ratings(rating)  
        return render_template('data_ratings.html',form_data = form_data)

@app.route('/data_suburbs', methods = ['POST', 'GET'])
def data_suburbs():
    if request.method == 'GET':
        return f"The URL /data_suburbs is accessed directly. Try going to '/suburbs' to submit form"
    if request.method == 'POST':
        form_data = request.form
        suburb = str(form_data['suburb'])
        print("Inserting " + suburb + "into db")
        conn = connector.connection()   
        conn.insert_suburb(suburb)     
        return render_template('data_suburbs.html',form_data = form_data)