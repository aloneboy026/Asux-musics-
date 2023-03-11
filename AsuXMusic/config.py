from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQCp74kggJj__lWkNav5VC8jMGbYsNB7vR0sodWWnonN1ODkMQJj6H3ZKlJwD_kW_99F_n0J4CxFzh3KSGEDUUJLpirRMgFc5S0r2nSc1Ho0zoOK3FQxdRu4QNlHs-gYdDOJA0B_9rhsJq-I9KwzARDeBDSd-mU14tn-xxoesAE3qrNal-NYz9_VqTLzf8O9LtyYENvvJBcN5IZ0MnC1L1FnTohpinefiNahWPQrwZpYF2GXaTjAeBMMVtWpRk37M9EELLgulMJM2xi-YjBg9gjvrYFQ9NuNkJbjrA0Bcjl69-cTwYsXrHaPm1440pF8LLia35ISqPMXjoywUhw5l8KrAAAAAXML5aUA")

BOT_TOKEN = getenv("BOT_TOKEN", "5791761493:AAETepzG4ZSeNuV66m1I4NYzpqWJg0S5tTY")
API_ID = int(getenv("API_ID", "10284859"))
API_HASH = getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")
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
