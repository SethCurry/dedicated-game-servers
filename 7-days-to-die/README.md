# 7 Days To Die Server Configuration
## Configuration
### Environment Variables
| Environment Variable | Config Option | Type | Description | Default |
| --- | --- | --- | --- | --- |
| ADMIN_FILE_NAME | AdminFileName | string | The name of the admin file | serveradmin.xml |
| BEDROLL_DEAD_ZONE_SIZE | BedrollDeadZoneSize | integer | The size of the dead zone around bedrolls | 15 |
| BEDROLL_EXPIRY_TIME | BedrollExpiryTime | integer | The time in days before bedrolls expire | 45 |
| BLOCK_DAMAGE_AI | BlockDamageAI | integer | The damage AI deal to blocks as a percentage | 100 |
| BLOCK_DAMAGE_AI_BM | BlockDamageAIBM | integer | The damage dealt to blocks by AI during blood moons | 100 |
| BLOCK_DAMAGE_PLAYER | BlockDamagePlayer | integer | The damage players deal to blocks as a percentage | 100 |
| BLOOD_MOON_ENEMY_COUNT | BloodMoonEnemyCount | integer |  | 8 |
| BLOOD_MOON_FREQUENCY | BloodMoonFrequency | integer |  | 7 |
| BLOOD_MOON_RANGE | BloodMoonRange | integer |  | 0 |
| BLOOD_MOON_WARNING | BloodMoonWarning | integer |  | 8 |
| BUILD_CREATE | BuildCreate | boolean | Whether create mode is enabled | False |
| DAY_LIGHT_LENGTH | DayLightLength | integer | The length of the day in hours | 18 |
| DAY_NIGHT_LENGTH | DayNightLength | integer | The length of the day-night cycle in minutes | 60 |
| DEATH_PENALTY | DeathPenalty | integer | The death penalty mode | 1 |
| DROP_FREQUENCY | DropFrequency | integer |  | 7 |
| DROP_MARKER | DropMarker | boolean |  | True |
| DROP_ON_DEATH | DropOnDeath | integer | The drop on death mode | 1 |
| DROP_ON_QUIT | DropOnQuit | integer | The drop on quit mode | 0 |
| DYNAMIC_MESH_ENABLED | DynamicMeshEnabled | boolean |  | True |
| DYNAMIC_MESH_LAND_CLAIM_BUFFER | DynamicMeshLandClaimBuffer | integer |  | 3 |
| DYNAMIC_MESH_LAND_CLAIM_ONLY | DynamicMeshLandClaimOnly | boolean |  | True |
| DYNAMIC_MESH_MAX_ITEM_CACHE | DynamicMeshMaxItemCache | integer |  | 3 |
| EAC_ENABLED | EACEnabled | boolean | Whether EAC is enabled | True |
| ENABLE_MAP_RENDERING | EnableMapRendering | boolean | Whether map rendering is enabled | False |
| ENEMY_DIFFICULTY | EnemyDifficulty | integer | The enemy difficulty | 0 |
| ENEMY_SPAWN_MODE | EnemySpawnMode | boolean |  | True |
| GAME_DIFFICULTY | GameDifficulty | integer | The game difficulty | 1 |
| GAME_MODE | GameMode | string | The game mode | GameModeSurvival |
| GAME_NAME | GameName | string | The name of the game | My Game |
| GAME_WORLD | GameWorld | string | The name of the game world | Navezgane |
| HIDE_COMMAND_EXECUTION_LOG | HideCommandExecutionLog | integer | The level of command execution logging | 0 |
| LAND_CLAIM_COUNT | LandClaimCount | integer |  | 3 |
| LAND_CLAIM_DEAD_ZONE | LandClaimDeadZone | integer |  | 30 |
| LAND_CLAIM_DECAY_MODE | LandClaimDecayMode | integer |  | 0 |
| LAND_CLAIM_EXPIRY_TIME | LandClaimExpiryTime | integer |  | 7 |
| LAND_CLAIM_OFFLINE_DELAY | LandClaimOfflineDelay | integer |  | 0 |
| LAND_CLAIM_OFFLINE_DURABILITY_MODIFIER | LandClaimOfflineDurabilityModifier | integer |  | 4 |
| LAND_CLAIM_ONLINE_DURABILITY_MODIFIER | LandClaimOnlineDurabilityModifier | integer |  | 4 |
| LAND_CLAIM_SIZE | LandClaimSize | integer |  | 41 |
| LANGUAGE | Language | string | The primary language of the server | English |
| LOOT_ABUNDANCE | LootAbundance | integer |  | 100 |
| LOOT_RESPAWN_DAYS | LootRespawnDays | integer |  | 7 |
| MAX_CHUNK_AGE | MaxChunkAge | integer |  | -1 |
| MAX_QUEUED_MESH_LAYERS | MaxQueuedMeshLayers | integer | The maximum number of queued mesh layers | 1000 |
| MAX_SPAWNED_ANIMALS | MaxSpawnedAnimals | integer | The maximum number of spawned animals | 50 |
| MAX_SPAWNED_ZOMBIES | MaxSpawnedZombies | integer | The maximum number of spawned zombies | 64 |
| MAX_UNCOVERED_MAP_CHUNKS_PER_PLAYER | MaxUncoveredMapChunksPerPlayer | integer | The maximum number of map chunks that can be uncovered per player | 131072 |
| PARTY_SHARED_KILL_RANGE | PartySharedKillRange | integer |  | 100 |
| PERSISTENT_PLAYER_PROFILES | PersistentPlayerProfiles | boolean | Whether player profiles are persistent | False |
| PLAYER_KILLING_MODE | PlayerKillingMode | integer |  | 3 |
| PLAYER_SAFE_ZONE_HOURS | PlayerSafeZoneHours | integer | The number of hours a player is safe from death penalties for after dying | 5 |
| PLAYER_SAFE_ZONE_LEVEL | PlayerSafeZoneLevel | integer | The level at which death penalties start to be applied to players | 5 |
| REGION | Region | string | The region the server is located in | NorthAmericaEast |
| SAVE_DATA_LIMIT | SaveDataLimit | integer |  | -1 |
| SAVE_GAME_FOLDER | SaveGameFolder | string | The folder where save game data is stored |  |
| SERVER_ADMIN_SLOTS | ServerAdminSlots | integer | The number of admin slots | 0 |
| SERVER_ADMIN_SLOTS_PERMISSION | ServerAdminSlotsPermission | integer | The permission level required to use an admin slot | 0 |
| SERVER_DESCRIPTION | ServerDescription | string | The description of the server as it will appear in the server browser | A 7 Days to Die Server |
| SERVER_DISABLED_NETWORK_PROTOCOLS | ServerDisabledNetworkProtocols | string | The network protocols that the server will not use | SteamNetwork |
| SERVER_LOGIN_CONFIRMATION_TEXT | ServerLoginConfirmationText | string | The text that will be displayed to players when they join the server |  |
| SERVER_MAX_ALLOWED_VIEW_DISTANCE | ServerMaxAllowedViewDistance | integer | The maximum allowed view distance for the server | 12 |
| SERVER_MAX_PLAYER_COUNT | ServerMaxPlayerCount | integer | The maximum number of players that can join the server | 8 |
| SERVER_MAX_WORLD_TRANSFER_SPEED_KBS | ServerMaxWorldTransferSpeedKiBs | integer | The maximum speed at which the server will transfer world data to clients in kilobytes per second | 512 |
| SERVER_NAME | ServerName | string | The name of the server as it will appear in the server browser | My Game Host |
| SERVER_PASSWORD | ServerPassword | string | The password required to join the server |  |
| SERVER_PORT | ServerPort | integer | The port the server will listen on | 26900 |
| SERVER_MAX_PLAYER_COUNT | ServerReservedSlots | integer | The number of reserved slots for players with the reserved slot permission | 0 |
| SERVER_RESERVED_SLOTS_PERMISSION | ServerReservedSlotsPermission | integer | The permission level required to use a reserved slot | 100 |
| SERVER_VISIBILITY | ServerVisibility | integer | The visibility of the server in the server browser | 2 |
| SERVER_WEBSITE_URL | ServerWebsiteURL | string | The URL to the server's website |  |
| TELNET_ENABLED | TelnetEnabled | boolean | Whether the telnet server is enabled | False |
| TELNET_FAILED_LOGIN_LIMIT | TelnetFailedLoginLimit | integer | The number of failed login attempts allowed before the client is blocked | 10 |
| TELNET_FAILED_LOGINS_BLOCK_TIME | TelnetFailedLoginsBlockTime | integer | The time in minutes that the client will be blocked after reaching the failed login limit | 10 |
| TELNET_PASSWORD | TelnetPassword | string | The password required to connect to the telnet server |  |
| TELNET_PORT | TelnetPort | integer | The port the telnet server will listen on | 8081 |
| TERMINAL_WINDOW_ENABLED | TerminalWindowEnabled | boolean | Whether the terminal window is enabled | True |
| TWITCH_BLOOD_MOON_ALLOWED | TwitchBloodMoonAllowed | boolean |  | False |
| TWITCH_SERVER_PERMISSION | TwitchServerPermission | integer |  | 90 |
| USER_DATA_FOLDER | UserDataFolder | string | The folder where user data is stored |  |
| WEB_DASHBOARD_ENABLED | WebDashboardEnabled | boolean | Whether the web dashboard is enabled | True |
| WEB_DASHBOARD_PORT | WebDashboardPort | integer | The port the web dashboard will listen on | 8080 |
| WEB_DASHBOARD_URL | WebDashboardUrl | string | The URL to the web dashboard |  |
| WORLD_GEN_SEED | WorldGenSeed | string | The seed used to generate the game world |  |
| WORLD_GEN_SIZE | WorldGenSize | integer | The size of the game world | 6144 |
| XP_MULTIPLIER | XPMultiplier | integer | The experience multiplier as a percentage | 100 |
| ZOMBIE_BM_MOVE | ZombieBMMove | integer |  | 3 |
| ZOMBIE_FERAL_MOVE | ZombieFeralMove | integer |  | 3 |
| ZOMBIE_FERAL_SENSE | ZombieFeralSense | integer | When and if zombies have Feral Sense. | 0 |
| ZOMBIE_MOVE | ZombieMove | integer | The move speed of zombies | 0 |
| ZOMBIE_MOVE_NIGHT | ZombieMoveNight | integer |  | 3 |
