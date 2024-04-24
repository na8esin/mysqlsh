import os
import shutil
from datetime import datetime

# stgからdump

now_ymd = datetime.today().strftime('%Y-%m-%d')

dump_dir = f'{os.environ["HOME"]}/dumps/{os.environ["STG_SCHEMA"]}-{now_ymd}'
# 同じ日にすでに取得していれば、dump削除
shutil.rmtree(dump_dir, ignore_errors=True)
print(dump_dir)

util.dump_tables(
  os.environ['STG_SCHEMA'],
  [],
  dump_dir,
  { "all": True, "showProgress": True, "dataOnly": True }
)
