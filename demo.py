from flask import Flask,request,jsonify
import getdata

app = Flask(__name__)

@app.route("/")
def getData():
    ObjgetData = getdata.getDatas()
    aData = ObjgetData.getAllData()
    
    if len(aData):
        response = jsonify({
            "result":aData,
            "status":200,
        })
    else:
        response = jsonify({
            "result":[],
            "status":400,
        })
    return response

@app.route("/insertData",methods=["POST"])
def insertData():
    data = request.json
    ObjgetData = getdata.getDatas()
    insertedCount = ObjgetData.insertData(data)
    
@app.route("/updateData/<int:usr_id>",methods=["PUT"])
def updateData(usr_id):
    data = request.json
    ObjgetData = getdata.getDatas()
    updatedCount = ObjgetData.updateData(data,usr_id)
    
    if updatedCount:
        response = jsonify({
            "status":200,
            "message": "updated successfully"
        })
    else:
        response = jsonify({
            "status":400,
            "message":"update failed"    
        })
        
    return response


app.run("0.0.0.0",debug=True)