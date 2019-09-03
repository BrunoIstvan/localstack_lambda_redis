# localstack_lambda_redis

Executar o script para subir os containers:

```bash
docker-compose up
```

Em outra janela, executar o seguinte comando para preparar os serviços em cada container:

```bash
sh run.sh
```

Após a finalização, basta invocar a função lambda. Para isso, exe

```bash
aws --endpoint-url=http://localhost:4574 lambda invoke --function-name lambda-demo out --log-type Tailcutar o comando:
```
