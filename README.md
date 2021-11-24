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
```

Para obter as credenciais de acesso à API:
  - Realize seu cadastro no site da [GerenciaNet](http://gerencianet.com.br/);
  - Acesse a área de API para criar uma aplicação:
  ![image](https://user-images.githubusercontent.com/67582983/143180542-4952e6c8-82dc-49f2-8d60-842ae6d54274.png)
  - Crie uma nova aplicação para utilizar a API:
  ![image](https://user-images.githubusercontent.com/67582983/143180801-9a2386b1-5cf0-4c9b-9c9e-e893e92f78a6.png)

