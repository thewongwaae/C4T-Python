from datetime import datetime
import pytz

local_timezone = pytz.timezone('Asia/Kuala_Lumpur')
local_time = datetime.now(pytz.utc).astimezone(local_timezone)

print(local_time.time())