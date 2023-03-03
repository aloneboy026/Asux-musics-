from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQBqj_mZaVxdqi4LaUfWsHoZahYdH1Fj-4GLZuU_uFyRPcXN38i3ILugt-k5pKT8FtHrt5K_HHp800bGBNpQsHyDcLiZIVy_9I-OubclsCCcjlwckfJrN7rDj4sh00i7WxE9IP8l3hqk-ZbycFHWBXBbwp1w8o9B6y26eKBCLsBhHAEuykQqkrGOAR8I3k9AydDIvgj6ydskF2-RKI-k1Pc6L8RGZEF2Vgx_OV9CnKVsRC_XT1O45FQr2tfeqftM6z6KiYuMXX9j4SW_6r-XdCFHZ4Li5R24O69t2A6DdF0g820V7q0dprhP6hr0ktjVhBzKkmWfTXjfF6wVhdL0fkrAAAAAAXML5aUA")

BOT_TOKEN = getenv("BOT_TOKEN", "5791761493:AAHyW5vB8ReVXS789EINMHE36bRuedObCCY")
API_ID = int(getenv("API_ID", "10284859"))
API_HASH = getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "team_comradesss")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mondo_lover")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5613528193").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5613528193").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
