<p align="center">
  <img width="600" height="200" src="https://gerencianet.com.br/wp-content/themes/Gerencianet/assets/images/portal-da-marca/versoes-da-marca/horizontal/h-p-positivo.png">
</p>

# GerenciaNet API
App de cobrança de pagamentos.

# Sobre
O intuito deste projeto é desenvolver uma aplicação de cobrança de pagamentos utilizando a plataforma GerenciaNet.

# Instalação
```bash
pip install gerencianet
```

# Usage
```python
from gerencianet import Gerencianet

credentials = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'sandbox': True
        }

gn = Gerencianet(credentials)

Para pobter as credenciais de acesso à API, realize seu cadastro no site da [GerenciaNet](http://gerencianet.com.br/) e acesse a área de API para criar uma aplicação.
