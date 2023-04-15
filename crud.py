from flask import Flask, request, make_response,jsonify
from flask_cors import CORS
from functools import wraps
import pymysql

app = Flask(__name__)
cors = CORS(app)

@app.route('/users', methods=['GET'])
def get():
    conn = pymysql.connect(host="localhost", user="root", password="", db="group1")
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select * from student")
    output = cur.fetchall()

    for x in output:
        print(x);

    conn.close()
    return jsonify(output);

@app.route('/specificuser', methods=['GET'])
def getSpecific():
    conn = pymysql.connect(host="localhost", user="root", password="", db="group1")
    cur = conn.cursor(pymysql.cursors.DictCursor)
    rollno = int(str(request.args.get('rollno')))
    sql = f"SELECT * FROM student where RollNo={rollno}";
    cur.execute(sql)
    output = cur.fetchall()
    for x in output:
        print(x);

    conn.close()
    return jsonify(output);

@app.route('/users', methods=['DELETE'])
def delete():
    conn = pymysql.connect(host="localhost", user="root", password="", db="group1")
    cur = conn.cursor(pymysql.cursors.DictCursor)
    rollno = int(str(request.args.get('rollno')))
    sql = f"DELETE FROM student where RollNo={rollno}";
    cur.execute(sql)
    output = cur.fetchall()
    conn.commit()
    print(cur.rowcount,"record deleted")
    return jsonify("RECORD DELETED SUCCESSFULLY");


@app.route('/users', methods=['PUT'])
def insert_user():
    conn = pymysql.connect(host="localhost", user="root", password="", db="group1")
    raw_json = request.get_json();

    RollNo = raw_json['RollNo'];
    FirstName = raw_json['FirstName'];
    LastName = raw_json['LastName'];
    City = raw_json['City'];
    Age = raw_json['Age'];
    ItemList = raw_json['ItemList'];

    sql = f"INSERT INTO student(RollNo,FirstName,LastName,City,Age,ItemList) VALUES ('"+str(RollNo)+"','"+FirstName+"','"+LastName+"','"+City+"','"+str(Age)+"','"+ItemList+"')";
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return jsonify("RECORD INSERTED SUCCESSFULLY");

@app.route('/insertmarks', methods=['GET'])
def insert_marks():
    conn = pymysql.connect(host="localhost", user="root", password="", db="group1")
    raw_json = request.get_json();

    RollNo = raw_json['RollNo'];
    CN = raw_json['CN'];
    Python = raw_json['Python'];
    COA = raw_json['COA'];
    Pcom = raw_json['Pcom'];
    Maths = raw_json['Maths'];

    sql = f"INSERT INTO ise_marks(RollNo,CN,Python,COA,Pcom,Maths) VALUES ('"+str(RollNo)+"','"+str(CN)+"','"+str(Python)+"','"+str(COA)+"','"+str(Pcom)+"','"+str(Maths)+"')";
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return jsonify("MARKS INSERTED SUCCESSFULLY");

@app.route('/users', methods=['POST'])
def update():
    conn = pymysql.connect(host="localhost", user="root", password="", db="group1")
    raw_json = request.get_json()

    RollNo = raw_json['RollNo'];
    FirstName = raw_json['FirstName'];
    LastName = raw_json['LastName'];
    City = raw_json['City'];
    Age = raw_json['Age'];
    ItemList = raw_json['ItemList'];

    sql = f"UPDATE student SET RollNo = '{RollNo}', FirstName = '{FirstName}', LastName = '{LastName}', City = '{City}', Age = '{Age}', ItemList = '{ItemList}' WHERE RollNo = {RollNo}"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return jsonify("RECORD UPDATED SUCCESSFULLY")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int("1234"), debug=True)