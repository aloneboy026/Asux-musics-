from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQBqj_mZaVxdqi4LaUfWsHoZahYdH1Fj-4GLZuU_uFyRPcXN38i3ILugt-k5pKT8FtHrt5K_HHp800bGBNpQsHyDcLiZIVy_9I-OubclsCCcjlwckfJrN7rDj4sh00i7WxE9IP8l3hqk-ZbycFHWBXBbwp1w8o9B6y26eKBCLsBhHAEuykQqkrGOAR8I3k9AydDIvgj6ydskF2-RKI-k1Pc6L8RGZEF2Vgx_OV9CnKVsRC_XT1O45FQr2tfeqftM6z6KiYuMXX9j4SW_6r-XdCFHZ4Li5R24O69t2A6DdF0g820V7q0dprhP6hr0ktjVhBzKkmWfTXjfF6wVhdL0fkrAAAAAAXML5aUA")

BOT_TOKEN = getenv("BOT_TOKEN", "5791761493:AAETepzG4ZSeNuV66m1I4NYzpqWJg0S5tTY")
API_ID = int(getenv("API_ID", "29468174"))
API_HASH = getenv("API_HASH", "7700926f228c8928e8373e1f03563625"")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "team_comradesss")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mondo_lover")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5613528193").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5613528193").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/202c8e5a57f1f8597fe2a.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/53112d2692ac8d0b499c0.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/f13721b7511585e52a179.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/ae3abdcc33afe6822c61b.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/e8007311f301c0011b743.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/d773ecc7a29e068c9ec3a.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/485f912bde710ba31817d.jpg"
)
