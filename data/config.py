from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")
GAVE_FEEDBACK = env.list("GAVE_FEEDBACK")
RESIDENTS_ARRIVED = env.dict("RESIDENTS_ARRIVED")
RESIDENTS_NOT_ARRIVED = env.dict("RESIDENTS_NOT_ARRIVED")

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}"
