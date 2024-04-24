# stgからdumpして、localにloadする。

事故を減らすためには、dumpとloadはスクリプトを分けて、vpn接続などを切ってからlocalにloadした方がいいと思います。

## dump例
`mysqlsh -h stg_hostname -u root -P 3306  --py < dump_stg.py`

## load例
`mysqlsh -h 127.0.0.1 -u root -P 3306  --py < load_local.py`

## .env読み込み
`export $(cat .env | grep -v ^# | xargs)`
