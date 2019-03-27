from flask import Flask, render_template

app = Flask(__name__)

def createMap(row,col):
    retList =[]
    retRow = []
    print('*'*50)
    for i in range(row):
        for j in range(col):
            # retList[i][j] = (i + j) % 2 + 1
            retRow.append((i + j) % 2 + 1)    
        retList.append(retRow)
        retRow = []      

    return retList            

@app.route('/')
def main():
    retMap = createMap(8,8)
    print(createMap(8,8))
    return render_template('index.html',mapping=retMap, color1='red',color2='black')

@app.route('/<x>')
def xRows(x):
    retMap = createMap(int(x),8)
    print(retMap)
    return render_template('index.html', mapping=retMap, color1='red', color2='black')   

@app.route('/<x>/<y>')
def ninja1(x,y):
    retMap = createMap(int(x),int(y))
    print(retMap)
    return render_template('index.html', mapping=retMap, color1='red', color2='black')

@app.route('/<x>/<y>/<color1>/<color2>')
def ninja2(x,y,color1,color2):
    retMap = createMap(int(x),int(y))
    print(retMap)
    print(color1, color2)
    return render_template('index.html', mapping=retMap, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)