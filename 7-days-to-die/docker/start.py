#!/usr/bin/env python3

import subprocess
import sys

from xml.dom import minidom
from dgs.game.config import Config, String, Integer, Boolean

class SevenDaysToDieConfig(Config):
  ServerName = String("SERVER_NAME", default="My Game Host", description="The name of the server as it will appear in the server browser")
  ServerDescription = String("SERVER_DESCRIPTION", default="A 7 Days to Die Server", description="The description of the server as it will appear in the server browser")
  ServerWebsiteURL = String("SERVER_WEBSITE_URL", default="", description="The URL to the server's website")
  ServerPassword = String("SERVER_PASSWORD", default="", description="The password required to join the server")
  ServerLoginConfirmationText = String("SERVER_LOGIN_CONFIRMATION_TEXT", default="", description="The text that will be displayed to players when they join the server")
  Region = String("REGION", default="NorthAmericaEast", description="The region the server is located in")
  Language = String("LANGUAGE", default="English", description="The primary language of the server")

  ServerPort = Integer("SERVER_PORT", default=26900, description="The port the server will listen on")
  ServerVisibility = Integer("SERVER_VISIBILITY", default=2, description="The visibility of the server in the server browser")
  ServerDisabledNetworkProtocols = String("SERVER_DISABLED_NETWORK_PROTOCOLS", default="SteamNetwork", description="The network protocols that the server will not use")
  ServerMaxWorldTransferSpeedKiBs = Integer("SERVER_MAX_WORLD_TRANSFER_SPEED_KBS", default=512, description="The maximum speed at which the server will transfer world data to clients in kilobytes per second")

  ServerMaxPlayerCount = Integer("SERVER_MAX_PLAYER_COUNT", default=8, description="The maximum number of players that can join the server")
  ServerReservedSlots = Integer("SERVER_MAX_PLAYER_COUNT", default=0, description="The number of reserved slots for players with the reserved slot permission")
  ServerReservedSlotsPermission = Integer("SERVER_RESERVED_SLOTS_PERMISSION", default=100, description="The permission level required to use a reserved slot")
  ServerAdminSlots = Integer("SERVER_ADMIN_SLOTS", default=0, description="The number of admin slots")
  ServerAdminSlotsPermission = Integer("SERVER_ADMIN_SLOTS_PERMISSION", default=0, description="The permission level required to use an admin slot")

  WebDashboardEnabled = Boolean("WEB_DASHBOARD_ENABLED", default=True, description="Whether the web dashboard is enabled")
  WebDashboardPort = Integer("WEB_DASHBOARD_PORT", default=8080, description="The port the web dashboard will listen on")
  WebDashboardUrl = String("WEB_DASHBOARD_URL", default="", description="The URL to the web dashboard")
  EnableMapRendering = Boolean("ENABLE_MAP_RENDERING", default=False, description="Whether map rendering is enabled")

  TelnetEnabled = Boolean("TELNET_ENABLED", default=False, description="Whether the telnet server is enabled")
  TelnetPort = Integer("TELNET_PORT", default=8081, description="The port the telnet server will listen on")
  TelnetPassword = String("TELNET_PASSWORD", default="", description="The password required to connect to the telnet server")
  TelnetFailedLoginLimit = Integer("TELNET_FAILED_LOGIN_LIMIT", default=10, description="The number of failed login attempts allowed before the client is blocked")
  TelnetFailedLoginsBlockTime = Integer("TELNET_FAILED_LOGINS_BLOCK_TIME", default=10, description="The time in minutes that the client will be blocked after reaching the failed login limit")

  TerminalWindowEnabled = Boolean("TERMINAL_WINDOW_ENABLED", default=True, description="Whether the terminal window is enabled")

  AdminFileName = String("ADMIN_FILE_NAME", default="serveradmin.xml", description="The name of the admin file")

  UserDataFolder = String("USER_DATA_FOLDER", default="", description="The folder where user data is stored")
  SaveGameFolder = String("SAVE_GAME_FOLDER", default="", description="The folder where save game data is stored")

  EACEnabled = Boolean("EAC_ENABLED", default=True, description="Whether EAC is enabled")
  HideCommandExecutionLog = Integer("HIDE_COMMAND_EXECUTION_LOG", default=0, description="The level of command execution logging")

  MaxUncoveredMapChunksPerPlayer = Integer("MAX_UNCOVERED_MAP_CHUNKS_PER_PLAYER", default=131072, description="The maximum number of map chunks that can be uncovered per player")
  PersistentPlayerProfiles = Boolean("PERSISTENT_PLAYER_PROFILES", default=False, description="Whether player profiles are persistent")

  GameWorld = String("GAME_WORLD", default="Navezgane", description="The name of the game world")

  WorldGenSeed = String("WORLD_GEN_SEED", default="", description="The seed used to generate the game world")
  WorldGenSize = Integer("WORLD_GEN_SIZE", default=6144, description="The size of the game world")

  GameName = String("GAME_NAME", default="My Game", description="The name of the game")
  GameMode = String("GAME_MODE", default="GameModeSurvival", description="The game mode")

  GameDifficulty = Integer("GAME_DIFFICULTY", default=1, description="The game difficulty")

  BlockDamagePlayer = Integer("BLOCK_DAMAGE_PLAYER", default=100, description="The damage players deal to blocks as a percentage")
  BlockDamageAI = Integer("BLOCK_DAMAGE_AI", default=100, description="The damage AI deal to blocks as a percentage")
  BlockDamageAIBM = Integer("BLOCK_DAMAGE_AI_BM", default=100, description="The damage dealt to blocks by AI during blood moons")
  XPMultiplier = Integer("XP_MULTIPLIER", default=100, description="The experience multiplier as a percentage")
  PlayerSafeZoneLevel = Integer("PLAYER_SAFE_ZONE_LEVEL", default=5, description="The level at which death penalties start to be applied to players")
  PlayerSafeZoneHours = Integer("PLAYER_SAFE_ZONE_HOURS", default=5, description="The number of hours a player is safe from death penalties for after dying")

  BuildCreate = Boolean("BUILD_CREATE", default=False, description="Whether create mode is enabled")
  DayNightLength = Integer("DAY_NIGHT_LENGTH", default=60, description="The length of the day-night cycle in minutes")
  DayLightLength = Integer("DAY_LIGHT_LENGTH", default=18, description="The length of the day in hours")
  DeathPenalty = Integer("DEATH_PENALTY", default=1, description="The death penalty mode")
  DropOnDeath = Integer("DROP_ON_DEATH", default=1, description="The drop on death mode")
  DropOnQuit = Integer("DROP_ON_QUIT", default=0, description="The drop on quit mode")

  BedrollDeadZoneSize = Integer("BEDROLL_DEAD_ZONE_SIZE", default=15, description="The size of the dead zone around bedrolls")
  BedrollExpiryTime = Integer("BEDROLL_EXPIRY_TIME", default=45, description="The time in days before bedrolls expire")

  MaxSpawnedZombies = Integer("MAX_SPAWNED_ZOMBIES", default=64, description="The maximum number of spawned zombies")
  MaxSpawnedAnimals = Integer("MAX_SPAWNED_ANIMALS", default=50, description="The maximum number of spawned animals")

  ServerMaxAllowedViewDistance = Integer("SERVER_MAX_ALLOWED_VIEW_DISTANCE", default=12, description="The maximum allowed view distance for the server")

  MaxQueuedMeshLayers = Integer("MAX_QUEUED_MESH_LAYERS", default=1000, description="The maximum number of queued mesh layers")

  EnemySpawnMode = Boolean("ENEMY_SPAWN_MODE", default=True)

  EnemyDifficulty = Integer("ENEMY_DIFFICULTY", default=0, description="The enemy difficulty")
  ZombieFeralSense = Integer("ZOMBIE_FERAL_SENSE", default=0, description="When and if zombies have Feral Sense.")

  ZombieMove = Integer("ZOMBIE_MOVE", default=0, description="The move speed of zombies")
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

if __name__ == "__main__":
  game_config = SevenDaysToDieConfig()
  rendered_config = game_config.render()

  with open("serverconfig.xml", "w") as f:
    f.write(rendered_config)

  subprocess.run(["bash", "-c", "startserver.sh", "-configfile=serverconfig.xml"],
               stdout=sys.stdout,
               stderr=sys.stderr,
               )