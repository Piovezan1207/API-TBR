from flask import Flask, jsonify, render_template, request ,redirect, send_file , flash, url_for, session
from gps2 import distancia

pontos = []

#print(  )

app = Flask(__name__)

@app.route("/", methods=['GET']) #Redirect para o Home
def H():
    argumento = request.args.get('nome')
    return argumento

@app.route("/opa", methods=['POST']) #Redirect para o Home
def Ha():
    if  pontos != [] :
        flag = False
        for ponto in pontos:
            print(ponto)
            dist = distancia(request.json["lon1"] ,  request.json["lat1"] ,ponto[0][0] , ponto[0][1])
            if dist < 3:
                print(ponto[1])
                ponto[1] = ponto[1] + 1
                flag = True 
                break

        if(not flag):
            pontos_tempo = [[request.json["lon1"] ,  request.json["lat1"]] , 0]
            pontos.append(pontos_tempo)
    else:
        pontos_tempo = [[request.json["lon1"] ,  request.json["lat1"]] , 0]
        pontos.append(pontos_tempo)
        

    return str(pontos)



if __name__ == "__main__":
    app.run(port=8923, host='0.0.0.0', debug=True, threaded=True)


