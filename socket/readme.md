# curl
curl 127.0.0.1:5000

# ネットワークコマンド

## ポートがlisten状態かどうかを確認する
`netstat -ltn`
-l : display listening server sockets
-t : TCP接続のみを表示
-n : アドレスとポート番号を数値形式で表示

`ss -atn`
-a : display all sockets
-t : 
-p : show process using socket