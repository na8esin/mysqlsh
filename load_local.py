import os
from datetime import datetime

# localにloadする

now_ymd = datetime.today().strftime('%Y-%m-%d')

dump_dir = f'{os.environ["HOME"]}/dumps/{os.environ["STG_SCHEMA"]}-{now_ymd}'
print(dump_dir)

util.load_dump(
  dump_dir,
  {"schema": os.environ['LOCAL_SCHEMA'], "showProgress": True, "ignoreExistingObjects": True}
)
