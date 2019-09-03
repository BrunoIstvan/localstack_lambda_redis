aws --endpoint-url=http://localhost:4574 lambda delete-function --function-name lambda-demo
cp lambda_function.py .venv/lib/python3.6/site-packages
cd .venv/lib/python3.6/site-packages
zip -r lambda.zip lambda_function.py redis*
mv lambda.zip ${OLDPWD}
cd ${OLDPWD}
aws --endpoint-url=http://localhost:4574 lambda create-function --region 'us-west-1' \
    --function-name lambda-demo --runtime python3.7 \
    --role arn:aws:iam::123456:role/irrelevant --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda.zip
