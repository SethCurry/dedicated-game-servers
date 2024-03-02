#!/usr/bin/env python3
from xml.dom import minidom
from dgs.game.config import Config, String, Integer, Boolean

class SevenDaysToDieConfig(Config):
  ServerName = String("SERVER_NAME", default="My Game Host")
  ServerDescription = String("SERVER_DESCRIPTION", default="A 7 Days to Die Server")
  ServerWebsiteURL = String("SERVER_WEBSITE_URL", default="")
  ServerPassword = String("SERVER_PASSWORD", default="")
  ServerLoginConfirmationText = String("SERVER_LOGIN_CONFIRMATION_TEXT", default="")
  Region = String("REGION", default="NorthAmericaEast")
  Language = String("LANGUAGE", default="English")

  ServerPort = Integer("SERVER_PORT", default=26900)
  ServerVisibility = Integer("SERVER_VISIBILITY", default=2)
  ServerDisabledNetworkProtocols = String("SERVER_DISABLED_NETWORK_PROTOCOLS", default="SteamNetwork")
  ServerMaxWorldTransferSpeedKiBs = Integer("SERVER_MAX_WORLD_TRANSFER_SPEED_KBS", default=512)

  ServerMaxPlayerCount = Integer("SERVER_MAX_PLAYER_COUNT", default=8)
  ServerReservedSlots = Integer("SERVER_MAX_PLAYER_COUNT", default=0)
  ServerReservedSlotsPermission = Integer("SERVER_RESERVED_SLOTS_PERMISSION", default=100)
  ServerAdminSlots = Integer("SERVER_ADMIN_SLOTS", default=0)
  ServerAdminSlotsPermission = Integer("SERVER_ADMIN_SLOTS_PERMISSION", default=0)

  WebDashboardEnabled = Boolean("WEB_DASHBOARD_ENABLED", default=True)
  WebDashboardPort = Integer("WEB_DASHBOARD_PORT", default=8080)
  WebDashboardUrl = String("WEB_DASHBOARD_URL", default="")
  EnableMapRendering = Boolean("ENABLE_MAP_RENDERING", default=False)

  TelnetEnabled = Boolean("TELNET_ENABLED", default=False)
  TelnetPort = Integer("TELNET_PORT", default=8081)
  TelnetPassword = String("TELNET_PASSWORD", default="")
  TelnetFailedLoginLimit = Integer("TELNET_FAILED_LOGIN_LIMIT", default=10)
  TelnetFailedLoginsBlockTime = Integer("TELNET_FAILED_LOGINS_BLOCK_TIME", default=10)

  TerminalWindowEnabled = Boolean("TERMINAL_WINDOW_ENABLED", default=True)

  AdminFileName = String("ADMIN_FILE_NAME", default="serveradmin.xml")

  UserDataFolder = String("USER_DATA_FOLDER", default="")
  SaveGameFolder = String("SAVE_GAME_FOLDER", default="")

  EACEnabled = Boolean("EAC_ENABLED", default=True)
  HideCommandExecutionLog = Integer("HIDE_COMMAND_EXECUTION_LOG", default=0)

  MaxUncoveredMapChunksPerPlayer = Integer("MAX_UNCOVERED_MAP_CHUNKS_PER_PLAYER", default=131072)
  PersistentPlayerProfiles = Boolean("PERSISTENT_PLAYER_PROFILES", default=False)

  GameWorld = String("GAME_WORLD", default="Navezgane")

  WorldGenSeed = String("WORLD_GEN_SEED", default="")
  WorldGenSize = Integer("WORLD_GEN_SIZE", default=6144)

  GameName = String("GAME_NAME", default="My Game")
  GameMode = String("GAME_MODE", default="GameModeSurvival")

  GameDifficulty = Integer("GAME_DIFFICULTY", default=1)

  BlockDamagePlayer = Integer("BLOCK_DAMAGE_PLAYER", default=100)
  BlockDamageAI = Integer("BLOCK_DAMAGE_AI", default=100)
  BlockDamageAIBM = Integer("BLOCK_DAMAGE_AI_BM", default=100)
  XPMultiplier = Integer("XP_MULTIPLIER", default=100)
  PlayerSafeZoneLevel = Integer("PLAYER_SAFE_ZONE_LEVEL", default=5)
  PlayerSafeZoneHours = Integer("PLAYER_SAFE_ZONE_HOURS", default=5)

  BuildCreate = Boolean("BUILD_CREATE", default=False)
  DayNightLength = Integer("DAY_NIGHT_LENGTH", default=60)
  DayLightLength = Integer("DAY_LIGHT_LENGTH", default=18)
  DeathPenalty = Integer("DEATH_PENALTY", default=1)
  DropOnDeath = Integer("DROP_ON_DEATH", default=1)
  DropOnQuit = Integer("DROP_ON_QUIT", default=0)

  BedrollDeadZoneSize = Integer("BEDROLL_DEAD_ZONE_SIZE", default=15)
  BedrollExpiryTime = Integer("BEDROLL_EXPIRY_TIME", default=45)

  MaxSpawnedZombies = Integer("MAX_SPAWNED_ZOMBIES", default=64)
  MaxSpawnedAnimals = Integer("MAX_SPAWNED_ANIMALS", default=50)

  ServerMaxAllowedViewDistance = Integer("SERVER_MAX_ALLOWED_VIEW_DISTANCE", default=12)

  MaxQueuedMeshLayers = Integer("MAX_QUEUED_MESH_LAYERS", default=1000)

  EnemySpawnMode = Boolean("ENEMY_SPAWN_MODE", default=True)

  EnemyDifficulty = Integer("ENEMY_DIFFICULTY", default=0)
  ZombieFeralSense = Integer("ZOMBIE_FERAL_SENSE", default=0)

  ZombieMove = Integer("ZOMBIE_MOVE", default=0)
  ZombieMoveNight = Integer("ZOMBIE_MOVE_NIGHT", default=3)
  ZombieFeralMove = Integer("ZOMBIE_FERAL_MOVE", default=3)
  ZombieBMMove = Integer("ZOMBIE_BM_MOVE", default=3)

  BloodMoonFrequency = Integer("BLOOD_MOON_FREQUENCY", default=7)
  BloodMoonRange = Integer("BLOOD_MOON_RANGE", default=0)
  BloodMoonWarning = Integer("BLOOD_MOON_WARNING", default=8)
  BloodMoonEnemyCount = Integer("BLOOD_MOON_ENEMY_COUNT", default=8)

  LootAbundance = Integer("LOOT_ABUNDANCE", default=100)
  LootRespawnDays = Integer("LOOT_RESPAWN_DAYS", default=7)
  DropFrequency = Integer("DROP_FREQUENCY", default=7)
  DropMarker = Boolean("DROP_MARKER", default=True)

  PartySharedKillRange = Integer("PARTY_SHARED_KILL_RANGE", default=100)
  PlayerKillingMode = Integer("PLAYER_KILLING_MODE", default=3)

  LandClaimCount = Integer("LAND_CLAIM_COUNT", default=3)
  LandClaimSize = Integer("LAND_CLAIM_SIZE", default=41)
  LandClaimDeadZone = Integer("LAND_CLAIM_DEAD_ZONE", default=30)
  LandClaimExpiryTime = Integer("LAND_CLAIM_EXPIRY_TIME", default=7)
  LandClaimDecayMode = Integer("LAND_CLAIM_DECAY_MODE", default=0)
  LandClaimOnlineDurabilityModifier = Integer("LAND_CLAIM_ONLINE_DURABILITY_MODIFIER", default=4)
  LandClaimOfflineDurabilityModifier = Integer("LAND_CLAIM_OFFLINE_DURABILITY_MODIFIER", default=4)
  LandClaimOfflineDelay = Integer("LAND_CLAIM_OFFLINE_DELAY", default=0)

  DynamicMeshEnabled = Boolean("DYNAMIC_MESH_ENABLED", default=True)
  DynamicMeshLandClaimOnly = Boolean("DYNAMIC_MESH_LAND_CLAIM_ONLY", default=True)
  DynamicMeshLandClaimBuffer = Integer("DYNAMIC_MESH_LAND_CLAIM_BUFFER", default=3)
  DynamicMeshMaxItemCache = Integer("DYNAMIC_MESH_MAX_ITEM_CACHE", default=3)

  TwitchServerPermission = Integer("TWITCH_SERVER_PERMISSION", default=90)
  TwitchBloodMoonAllowed = Boolean("TWITCH_BLOOD_MOON_ALLOWED", default=False)

  MaxChunkAge = Integer("MAX_CHUNK_AGE", default=-1)
  SaveDataLimit = Integer("SAVE_DATA_LIMIT", default=-1)

  def render(self):
    root = minidom.Document()

    xml = root.createElement("ServerSettings")
    root.appendChild(xml)

    for key, value in self.read().items():
      prop = root.createElement("property")

      str_value = value

      if type(value) == bool:
        str_value = "true" if value else "false"
      elif type(value) == int:
        str_value = str(value)

      prop.setAttribute("name", key)
      prop.setAttribute("value", str_value)

      xml.appendChild(prop)
    
    return root.toprettyxml(indent="  ")

game_config = SevenDaysToDieConfig()
print(game_config.render())