# cfg

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# bot id
BOT_NAME = "HexVoid"
BOT_VERSION = "9.4.H"

# sec
BOT_TOKEN = os.getenv("BOT_TOKEN")
UPSTASH_REDIS_REST_URL = os.getenv("UPSTASH_REDIS_REST_URL", "")
UPSTASH_REDIS_REST_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN", "")
DATABASE_PATH = str(Path(os.getenv("DATABASE_PATH", "data/hexvoid.db")))
GITHUB_REPO_URL = os.getenv("GITHUB_REPO_URL", "")
GITHUB_PAT = os.getenv("GITHUB_PAT", "")
FORM_LINK = os.getenv("FORM_LINK", "")

VAULT_WEBHOOK = os.getenv("VAULT_WEBHOOK", "")

# sync ok ids
_raw_ids = os.getenv("SYNC_ALLOWED_USER_IDS", "")
SYNC_ALLOWED_USER_IDS = [int(x.strip()) for x in _raw_ids.split(",") if x.strip()]

# maint nodes
_mnt_nodes = os.getenv("MAINTENANCE_NODES", "")
MAINTENANCE_NODES = [int(x.strip()) for x in _mnt_nodes.split(",") if x.strip()]

# cls
COLOR_SUCCESS = 0x2ECC71
COLOR_WARNING = 0xF1C40F
COLOR_ERROR   = 0xE74C3C
COLOR_INFO    = 0x3498DB
COLOR_MUTE    = 0xE67E22
COLOR_BAN     = 0xC0392B
COLOR_KICK    = 0xE74C3C
COLOR_NOTE    = 0x9B59B6
COLOR_AUTOMOD = 0x1ABC9C
COLOR_MODLOG  = 0x7289DA
COLOR_DECAY   = 0x2ECC71
COLOR_STRIKE  = 0xE74C3C
COLOR_GIVEAWAY     = 0xFF73FA
COLOR_GIVEAWAY_END = 0x2ECC71
COLOR_VOICE    = 0x9B59B6
COLOR_FUN      = 0xE91E63
COLOR_REMINDER = 0x5865F2

# strk lvl
STRIKE_LADDER = [
    {"label": "Clean Slate",           "action": None,    "duration": None},
    {"label": "Strike 1 — Warning",    "action": "warn",  "duration": None},
    {"label": "Strike 2 — 2h Mute",   "action": "mute",  "duration": 7200},
    {"label": "Strike 3 — 24h Mute",  "action": "mute",  "duration": 86400},
    {"label": "Strike 4 — Kick",       "action": "kick",  "duration": None},
    {"label": "Strike 5 — 1 Week Ban", "action": "ban",   "duration": 604800},
    {"label": "Strike 6 — Perma-Ban",  "action": "ban",   "duration": None},
]

MAX_STRIKE_LEVEL = len(STRIKE_LADDER) - 1

# infra bkt
INFRACTION_BUCKET_LIMIT = 2
INFRACTION_WINDOW = 3600
WARNING_BUCKET_LIMIT = 2

DECAY_LOOP_HOURS = 1

# no nuke sc
PANIC_CHANNEL_DELETE_THRESHOLD = 3
PANIC_KICK_BAN_THRESHOLD = 15
PANIC_WINDOW = 60

# am defs
AUTOMOD_DEFAULTS = {
    "link_filter": {
        "enabled": True,
        "whitelist": [
            "youtube.com", "youtu.be", "tenor.com", "giphy.com",
            "github.com", "imgur.com", "reddit.com",
        ],
    },
    "toxicity_filter": {
        "enabled": True,
        "blacklist": [],
        "wildcard": True,
    },
    "caps_filter": {
        "enabled": True,
        "min_length": 15,
        "threshold": 70,
    },
    "emoji_filter": {
        "enabled": True,
        "max_emojis": 5,
        "block_zalgo": True,
    },
    "flood_filter": {
        "enabled": True,
        "soft_msg_count": 4,
        "soft_msg_window": 3,
        "hard_msg_count": 6,
        "hard_msg_window": 4,
        "dup_soft_count": 3,
        "dup_hard_count": 5,
        "raid_window": 5,
        "raid_slowmode": 15,
        "raid_cooldown": 60,
    },
    "strike_ladder": {
        "enabled": True,
        "cooldown_1": 24,
        "cooldown_2": 48,
        "cooldown_3": 72,
        "cooldown_4": 360,
        "cooldown_5": 720,
        "cooldown_6": 0,
        "duration_1": 0,
        "duration_2": 7200,
        "duration_3": 86400,
        "duration_4": 0,
        "duration_5": 604800,
        "duration_6": 0,
    },
}

# ga defs
GIVEAWAY_DEFAULTS = {
    "alt_protection_hours": 24,
    "min_account_age_days": 0,
    "min_join_age_days": 0,
    "bonus_roles": {},
}

# rnd nck
RANDOM_NICKNAMES = [
    "Fluffy Bunny", "Reformed Troll", "Cute Potato", "Snuggle Muffin",
    "Captain Compliance", "Sparkle Unicorn", "Rule Follower 9000",
    "Gentle Guardian", "Peaceful Penguin", "Wholesome Warrior",
    "Sir Behaves-a-Lot", "The Redeemed", "Friendly Frog",
    "Angel in Training", "Good Vibes Only", "Chat Champion",
    "Saint Silence", "Deputy Decorum", "Zen Zephyr", "Harmony Helper",
]

# gly wl
GALLERY_IMAGE_TYPES = {"jpg", "jpeg", "tiff", "png", "gif", "webp", "bmp"}
GALLERY_ALLOWED_DOMAINS = {"tenor.com", "giphy.com", "cdn.discordapp.com"}

# emb ftr
EMBED_FOOTER = f"{BOT_NAME} v{BOT_VERSION}"
EMBED_FOOTER_ICON = None
