# Mercadobitcoin MMS

### Build do projeto
Antes de qualquer coisa, deve ser criado um arquivo .env na raíz do projeto com as variáveis de ambiente:
```
DEBUG=False
DJANGO_ENV=dev
ALLOWED_HOSTS=*
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_PASSWORD=123456
POSTGRES_USER=user_mb
POSTGRES_DB=mercadobitcoin
SECRET_KEY=SKS$$^dsfbvxcsd()*
CANDLE_MB_URL=https://mobile.mercadobitcoin.com.br/v4/{pair}/candle?from={ts_from}&to={ts_to}&precision=1d
CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
CELERY_TIMEZONE=America/Sao_Paulo
LOGGING_FILE_NAME=log.txt
EMAIL_HOST=
EMAIL_HOST_USER=
DEFAULT_FROM_EMAIL=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=587
EMAIL_USE_TLS=True
PAIRS=BRLBTC,BRLETH
MIN_DAYS_QUERY=365
ADMINS="(('nomeadmin', 'admin@email_admin.com'),)"
```
Se possível dê preferência para o uso do Makefile, ele abstrai vários comandos longos (verificar arquivo Makefile)
```bash
make build migrate up
Ou
docker-compose -f docker-compose.yaml build
docker-compose -f docker-compose.yaml run --rm --entrypoint="" web python manage.py migrate
docker-compose -f docker-compose.yaml up --force-recreate
```
O processo pode demorar um pouco, pois será realizado o build da image e o pull das imagens dos demais serviços.

Após o build e a inicializaç~so de todos os serviços, rodar o seguinte comando para realizar o import inicial da base:
```
make initial-import
Ou
docker-compose -f docker-compose.yaml run --rm --entrypoint="" web python manage.py initial_import
```
Para rodar os testes, utilizar o comando:
```
make pytest
Ou
docker-compose -f docker-compose.yaml run --rm --entrypoint="" web pytest -s
```
saída:
```bash
======================================== test session starts ========================================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
django: settings: mercadobitcoin.settings (from ini)
rootdir: /app, configfile: pytest.ini
plugins: anyio-3.3.0, cov-2.12.1, django-4.4.0
collected 7 items

apps/mms/tests/test_missing_dates.py ..
apps/mms/tests/test_signal_create_mms.py .
apps/mms/tests/test_view.py ..
apps/mms/tests/test_utils.py .
apps/mms/tests/test_utils_date.py .

----------- coverage: platform linux, python 3.9.7-final-0 -----------
Coverage HTML written to dir htmlcov

Required test coverage of 60% reached. Total coverage: 71.57%

========================================= 7 passed in 5.06s =========================================

```
# Documentação da API
ex:
GET http://0.0.0.0:8000/{PAR}/mms?to={TIMESTAMP_TO}&from=TIMESTAMP_FROM&range={RANGE_INT}
PAR: tipo string com os valores BRLBTC ou BRLETH
TIMESTAMP_TO, TIMESTAMP_FROM: tipo inteiro com o timestamp correspondente
RANGE_INT: tipo inteiro com os possíveis valores (200, 50, 20)
```
GET http://0.0.0.0:8000/BRLETH/mms?to=1630897199&from=1614999599&range=200
```
retorno com status code (200):
```json
[
  {
    "timestamp":1615075200,
    "mms":4272.03
  },
  {
    "timestamp":1615161600,
    "mms":4308.78},
  {
    "timestamp":1615248000,
    "mms":4348.45
  }
  ...
]
```
retorno para requisições com range_from fora do limite de 365 dias. Bad request, status code (400):
```json
{
  "error": "Range fora do limite"
}
```
# Explicações gerais sobre o teste

- Foi respeitada a organização padrão dos apps do Framework Django
- Foram incluídos elementos como Use Cases, como defendido por Martin Fowler, para organizar os requisitos da aplicação MMS.
- Foi criado um handler customizado para manipular as exceções conhecidas da API.
- Foram escritos testes de Ponta a Ponta e unitários.
- Configurei os testes para ter uma cobertura mínima de 60%.
- Muitas funções ficaram dentro do app mms, pois assim é possível compartilhar apps django ou criar LIB's caso seja necessário.

### Script de import
Para o acionamento do script foi criado um comando customizado django. Facilita os imports necessários e ajuda na organização.
O script e a aplicação se utilizam de várias funções encontradas na pasta "utils".

### sobre os requisitos assíncronos
Foram criadas tasks com os seguintes agendamentos:
- check_missing_dates: roda de hora em hora procurando por registros faltantes no banco de dados. Caso encontre algumas datas, será adicionado ao log como erro e automaticamente será enviado um email para os admins do sistema. Para o envio de email é necessário preencher as credenciais do serviço escolhido no .env.
- A função que verifica no banco as datas faltantes fica em um manager customizado do model MMS e é chamada pelos usecases.
- import_yesterday: realiza o import incremental e roda diariamente as 00:01h
- Caso a task que faz o import incremental falhe por algum motivo, será realizadas N tentativas a cada 10 minutos.


#### Obs. para utilizar o admin do django com o CSS devidamente carregado, é necessário rodar com runserver, não foi configurado um servidor de arquivos estáticos par aser utilizado com o ASGI Server Daphne (Não era requisito do teste).