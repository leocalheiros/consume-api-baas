# Consume API BaaS DynamoDB

## Descrição do Projeto

Este é um projeto feito para consumir APIs especificando seu type (que seria o nome fictício da api que queremos lidar) e o action (que seria a ação da rota da api desejada) ou chamando os endpoints de forma separada caso desejar. Neste projeto consumo uma api de BaaS (que se encontra no repositório api-baas-dynamodb) e faço toda sua lógica a partir do conceito do projeto. 


## Configuração do Ambiente

Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas:

```bash
pip install -r requirements.txt
```

Como o projeto foi feito para rodar em uma lambda, não temos um arquivo de inicialização, porém fique a vontade para criar e testar localmente.
Caso implemente no lambda, crie a pasta package e instale os requirements nela com:
```bash
pip install --target ./package nomedapackage
```

## Como usar a API:
**Utilizando o endpoint geral execute**:
- **Endpoint único**: `/execute`
- **Método**: POST
- **Entrada**: JSON contendo "type" e "action" obrigatórios
- **Exemplo**:{
  "type": "baas",
  "action": "action-desejada"
  ...resto do json
  }
  
**Utilizando os endpoints separados**:
  - **Endpoints**:
   - para operações com os account controllers: `/account/{action}` Ex: `/account/login`
  - para operações com os payments controllers: `/payments/{action}` Ex: `/payments/create-payment`
  - para operações com os saldo controllers: `/balance/{action}` Ex: `/balance/deposit`
  
## Autenticação JWT
- **Headers**:
- **Bearer token gerado no login**
- **Email do login**

## Actions da API BaaS
### Criar pessoa

- **Action**: `create-person`
- **Exemplo**: {
    "type": "baas",
    "action": "create-person"
    "email": "joao@gmail.com",
    "senha": "123",
    "saldo": 100 (int)
}

### Login

- **Action**: `login`
- **Exemplo**: {
    "type": "baas",
    "action": "login"
    "email": "joao@gmail.com",
    "senha": "123"
}

### Consultar dados via e-mail (necessário autenticação jwt)

- **Action**: `get-person`
- **Exemplo**: {
    "type": "baas",
    "action": "login"
    "email": "joao@gmail.com",
}

### Depositar saldo (necessário autenticação jwt)

- **Action**: `deposit-saldo`
- **Exemplo**: {
    "type": "baas",
    "action": "deposit-saldo"
    "email": "joao@gmail.com",
    "amount": 100 (int)
}

### Transferir saldo entre contas (necessário autenticação jwt)

- **Action**: `transfer-saldo`
- **Exemplo**: {
    "type": "baas",
    "action": "transfer-saldo"
    "source_email": "joao@gmail.com",
    "target_email": "pedro@gmail.com",
    "amount": 100 (int)
}

### Sacar saldo (necessário autenticação jwt)

- **Action**: `withdraw-saldo`
- **Exemplo**: {
    "type": "baas",
    "action": "withdraw-saldo"
    "email": "joao@gmail.com",
    "amount": 100 (int)
}

### Registrar cartão de crédito na conta já existente (necessário autenticação jwt)

- **Action**: `register-credit-card`
- **Exemplo**: {
    "type": "baas",
    "action": "register-credit-card",
    "email": "joao@gmail.com",
    "card_number": "5502902593408544", 
    "expiration_month": 12, 
    "expiration_year": 2027, 
    "security_code": "123", 
    "holder_name": "Julio Alvarenga" 

}


### Criar pagamento fictício (necessário autenticação jwt)

- **Action**: `create-payment`
- **Exemplo**: {
    "type": "baas",
    "action": "create-payment"
    "email": "joao@gmail.com",
    "amount": 100 (int)
}

