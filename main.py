from flask import Flask, jsonify, render_template, request ,redirect, send_file , flash, url_for, session
from gps2 import distancia

pontos = []
raio = 3 #Raio de cada área
#print(  )

app = Flask(__name__)

@app.route("/", methods=['GET']) #Rota para o home da api
def H():
    argumento = request.args.get('nome')
    return argumento


#Exemplo do corpo da requisição: {"lon1" : -23.46426120901994, "lat1" : -46.46672902051893 }
@app.route("/opa", methods=['POST']) #Recebimento da denuncia
def Ha():
    if  pontos != [] :#Caso o vetor de pontos não esteja vazio 
        flag = False#Flag para indicar que esse ponto está em uma área existente 
        for ponto in pontos: #Varre todos os pontos exitentes
            print(ponto)
            dist = distancia(request.json["lon1"] ,  request.json["lat1"] ,ponto[0][0] , ponto[0][1]) #Verica a distância entre o ponto recebido e os existentes
            if dist < raio: #Se a distancia for menor que o raio definido
                ponto[1] = ponto[1] + 1 #incrementa 1 a variável que armazena o total de pontos dentro da mesma área
                flag = True #Sinaliza uma compatibilidade do ponto recebido com a área
                break

        if(not flag):#Caso não tenha tido uma compatibilidade
            pontos_tempo = [[request.json["lon1"] ,  request.json["lat1"]] , 1] #Cria um novo ponto
            pontos.append(pontos_tempo)
    else:#Caso o vetor esteja vazio, cria o primeiro ponto
        pontos_tempo = [[request.json["lon1"] ,  request.json["lat1"]] , 1]
        pontos.append(pontos_tempo)
        

    return str(pontos)#Retorna a lista de áreas existentes e a quantia de pontos em cada área



if __name__ == "__main__":
    app.run(port=8923, host='0.0.0.0', debug=True, threaded=True)


