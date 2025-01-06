openssl genpkey -algorithm RSA -out key.pem

rem Создание запроса на сертификат (CSR)
openssl req -new -key key.pem -out csr.pem

rem Подписание сертификата с использованием ключа (самоподписанный сертификат)
openssl x509 -req -in csr.pem -signkey key.pem -out cert.pem