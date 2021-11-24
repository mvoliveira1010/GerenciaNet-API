from flask import Flask, render_template, request, redirect, url_for, flash
from gerencianet import Gerencianet
import json
from datetime import datetime,timedelta

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

credentials = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'sandbox': True
        }

gn = Gerencianet(credentials)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transacao', methods=['GET','POST'])
def transacao(gn=gn):
    if request.method == 'POST':
        item = request.form.to_dict()
        if int(item['value'][0])<5:
            flash('Valor mínimo para transação: 5,00')
            return redirect(url_for('index'))
        item['value'] = int(item['value'].replace(',','').replace('.',''))
        item['amount'] = int(item['amount'])
        nova_transacao = {
            'items':[item]
            }
        result = gn.create_charge(body=nova_transacao)
        id_transacao = result['data']['charge_id']
        response_transacao = gn.detail_charge(params={'id':int(id_transacao)})
        transacao = response_transacao['data']
        transacao['created_at'] = transacao['created_at'][:10]
        transacao['items'][0]['value'] = f"R$ {str(transacao['items'][0]['value'])[:-2]},00"
        transacao['total'] = f"R$ {str(transacao['total'])[:-2]},{str(transacao['total'])[-2]}{str(transacao['total'])[-1]}"
        novo_pagamento = {
            'expire_at':str(datetime.strptime(transacao['created_at'], '%Y-%m-%d').date()+timedelta(days=3)),
            'request_delivery_address':False,
            'payment_method':'all'
            }
        params = {'id':id_transacao}
        response_pagamento = gn.link_charge(params=params, body=novo_pagamento)
        pagamento = response_pagamento['data']
        transacao['created_at'] = str(datetime.strptime(transacao['created_at'], '%Y-%m-%d').strftime('%d/%m/%Y'))
        pagamento['expire_at'] = str(datetime.strptime(pagamento['expire_at'], '%Y-%m-%d').strftime('%d/%m/%Y'))
    else:
        transacao = False
        pagamento = False
    return render_template('transacoes.html', transacao=transacao, pagamento=pagamento)

@app.route('/voltar')
def voltar():
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)