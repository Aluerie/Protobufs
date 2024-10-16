# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: citadel_gcmessages_server.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class EGCCitadelServerMessages(betterproto.Enum):
    k_EMsgServerToGCMatchSignoutPermission = 10012
    k_EMsgServerToGCMatchSignoutPermissionResponse = 10013
    k_EMsgServerToGCMatchSignout = 10014
    k_EMsgServerToGCMatchSignoutResponse = 10015
    k_EMsgGCToServerAddSpectator = 10016
    k_EMsgGCToServerAddSpectatorResponse = 10017
    k_EMsgServerToGCIdlePing = 10018
    k_EMsgGCToServerRequestPing = 10019
    k_EMsgGCToServerAllocateForMatch = 10021
    k_EMsgGCToServerAllocateForMatchResponse = 10022
    k_EMsgServerToGCEnterMatchmaking = 10023
    k_EMsgGCToServerCancelAllocateForMatch = 10024
    k_EMsgServerToGCUpdateLobbyServerState = 10025
    k_EMsgServerToGCAbandonMatch = 10026
    k_EMsgServerToGCAbandonMatchResponse = 10027
    k_EMsgServerToGCTestConnection = 10028
    k_EMsgServerToGCTestConnectionResponse = 10029
    k_EMsgGCToServerSetServerConVar = 10039
    k_EMsgGCToServerSetServerConVarResponse = 10040
    k_EMsgServerToGCUpdateMatchInfo = 10041
    k_EMsgServerToGCReportCheater = 10042
    k_EMsgServerToGCReportCheaterResponse = 10043


class EGCServerLobbyData(betterproto.Enum):
    k_EServerLobbyData_PlayerMMR = 1
    k_EServerLobbyData_PlayerInfo = 2
    k_EServerLobbyData_PostMatchSurvey = 3
    k_EServerLobbyData_AutoTest = 4


class EGCServerSignoutData(betterproto.Enum):
    k_EServerSignoutData_Disconnections = 2
    k_EServerSignoutData_AccountStatChanges = 3
    k_EServerSignoutData_DetailedStats = 4
    k_EServerSignoutData_ServerPerfStats = 5
    k_EServerSignoutData_PerfData = 6
    k_EServerSignoutData_PlayerChat = 7
    k_EServerSignoutData_BookRewards = 8
    k_EServerSignoutData_PenalizedPlayers = 9
    k_EServerSignoutData_ReportCheaters = 10


class CSOCitadelServerStaticLobbyEAwardIDs(betterproto.Enum):
    k_eAward_KingPanda = 1


class CMsgServerSignoutData_PenalizedPlayersEPenaltyReason(betterproto.Enum):
    k_EPenaltyReason_Abandon = 0
    k_EPenaltyReason_DisconnectedTooLong = 1


class CMsgMatchDataEEndReason(betterproto.Enum):
    k_EEndReason_TeamWin = 0
    k_EEndReason_AllAbandoned = 2
    k_EEndReason_NetworkIssues = 3
    k_EEndReason_MatchLength = 4
    k_EEndReason_PlayerNeverConnected = 5


class CMsgServerToGCMatchSignoutResponseESignoutResult(betterproto.Enum):
    k_ESignout_Failed_Retry = 1
    k_ESignout_Failed_NoRetry = 2
    k_ESignout_Failed_InFlight = 3
    k_ESignout_Success = 4
    k_ESignout_Success_AlreadySignedOut = 5


class CMsgServerToGCAbandonMatchEReason(betterproto.Enum):
    eReason_ServerCrash = 1
    eReason_ClientsFailedToConnect = 2


class CMsgGCToServerAddSpectatorResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eServerFull = 2


@dataclass
class CMsgServerCrashSentinelFile(betterproto.Message):
    version: int = betterproto.uint32_field(1)
    server_steam_id: float = betterproto.fixed64_field(2)
    server_public_ip_addr: float = betterproto.fixed32_field(3)
    server_port: int = betterproto.uint32_field(4)
    server_cluster: int = betterproto.uint32_field(5)
    pid: int = betterproto.uint32_field(6)
    saved_time: int = betterproto.uint32_field(7)
    server_version: int = betterproto.uint32_field(8)
    game_info: "CMsgServerCrashSentinelFileGameInfo" = betterproto.message_field(9)
    server_private_ip_addr: int = betterproto.uint32_field(10)
    instance_id: int = betterproto.uint32_field(11)


@dataclass
class CMsgServerCrashSentinelFilePlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    hero_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgServerCrashSentinelFileGameInfo(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)
    lobby_id: float = betterproto.fixed64_field(2)
    server_state: int = betterproto.uint32_field(3)
    players: List["CMsgServerCrashSentinelFilePlayer"] = betterproto.message_field(5)
    match_mode: "ECitadelMatchMode" = betterproto.enum_field(6)
    game_mode: "ECitadelGameMode" = betterproto.enum_field(7)
    was_server_shutdown: bool = betterproto.bool_field(8)


@dataclass
class CServerLobbyData_PlayerMMR(betterproto.Message):
    players: List["CServerLobbyData_PlayerMMRPlayer"] = betterproto.message_field(1)


@dataclass
class CServerLobbyData_PlayerMMRPlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    player_mmr: int = betterproto.uint32_field(2)
    player_uncertainty: int = betterproto.uint32_field(3)
    hero_mmr: int = betterproto.uint32_field(4)


@dataclass
class CServerLobbyData_PlayerInfo(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    account_stats: List["CMsgAccountHeroStats"] = betterproto.message_field(2)
    mmr_level: int = betterproto.uint32_field(4)
    book_info: List["CMsgAccountBookStats"] = betterproto.message_field(5)


@dataclass
class CServerLobbyData_PostMatchSurvey(betterproto.Message):
    surveys: List[
        "CServerLobbyData_PostMatchSurveyPlayerSurvey"
    ] = betterproto.message_field(1)


@dataclass
class CServerLobbyData_PostMatchSurveyPlayerSurvey(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    question_id: int = betterproto.uint32_field(2)


@dataclass
class CServerLobbyData_AutoTest(betterproto.Message):
    max_duration_s: int = betterproto.uint32_field(2)


@dataclass
class CSOCitadelServerDynamicLobby(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    left_account_ids: List[int] = betterproto.uint32_field(2)
    broadcast_active: bool = betterproto.bool_field(3)
    spectator_count: int = betterproto.uint32_field(4)


@dataclass
class CSOCitadelServerStaticLobby(betterproto.Message):
    extra_messages: List["CExtraMsgBlock"] = betterproto.message_field(1)
    server_steam_id: float = betterproto.fixed64_field(2)
    lobby_id: int = betterproto.uint64_field(3)
    replay_salt: float = betterproto.fixed32_field(4)
    level_name: str = betterproto.string_field(5)
    members: List["CSOCitadelServerStaticLobbyMember"] = betterproto.message_field(6)
    dev_settings: "CSOCitadelServerStaticLobbyDevSettings" = betterproto.message_field(
        7
    )
    gc_provided_heroes: bool = betterproto.bool_field(8)
    bot_difficulty: "ECitadelBotDifficulty" = betterproto.enum_field(9)
    metadata_salt: float = betterproto.fixed32_field(10)
    match_start_time: int = betterproto.uint32_field(11)
    experimental_gameplay_state: int = betterproto.uint32_field(15)
    region_mode: "ECitadelRegionMode" = betterproto.enum_field(16)
    broadcast_url: str = betterproto.string_field(17)
    new_player_pool: bool = betterproto.bool_field(18)
    low_pri_pool: bool = betterproto.bool_field(19)
    is_restricted_access: bool = betterproto.bool_field(20)
    cheats_enabled: bool = betterproto.bool_field(21)


@dataclass
class CSOCitadelServerStaticLobbyMember(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    persona_name: str = betterproto.string_field(2)
    team: "ECitadelLobbyTeam" = betterproto.enum_field(3)
    player_slot: int = betterproto.uint32_field(4)
    hero_id: int = betterproto.uint32_field(5)
    party_index: int = betterproto.uint32_field(6)
    platform: "EGCPlatform" = betterproto.enum_field(7)
    award_ids: List["CSOCitadelServerStaticLobbyEAwardIDs"] = betterproto.enum_field(8)
    is_comms_restricted: bool = betterproto.bool_field(9)
    lane_id: int = betterproto.uint32_field(10)


@dataclass
class CSOCitadelServerStaticLobbyDevSettings(betterproto.Message):
    console_string: str = betterproto.string_field(1)


@dataclass
class CMsgServerSignoutData_ServerPerfStats(betterproto.Message):
    peak_memory_bytes: int = betterproto.uint64_field(1)
    end_memory_bytes: int = betterproto.uint64_field(2)
    frame_time_max_micro_s: int = betterproto.uint32_field(3)
    frame_time_95_micro_s: int = betterproto.uint32_field(4)
    frame_time_avg_micro_s: int = betterproto.uint32_field(5)
    frame_idle_time_95_micro_s: int = betterproto.uint32_field(6)
    frame_idle_time_avg_micro_s: int = betterproto.uint32_field(7)
    frame_time_80_micro_s: int = betterproto.uint32_field(8)
    frame_time_99_micro_s: int = betterproto.uint32_field(9)
    perf_samples: "CMsgServerSignoutData_ServerPerfStatsMatchPerfSamples" = (
        betterproto.message_field(10)
    )


@dataclass
class CMsgServerSignoutData_ServerPerfStatsFrameCounts(betterproto.Message):
    num_frames: int = betterproto.uint32_field(1)
    longest_run: int = betterproto.uint32_field(2)
    num_runs: int = betterproto.uint32_field(3)


@dataclass
class CMsgServerSignoutData_ServerPerfStatsPerfSample(betterproto.Message):
    game_time_s: int = betterproto.uint32_field(1)
    avg_frame: float = betterproto.float_field(2)
    avg_idle: float = betterproto.float_field(3)
    total_frames: int = betterproto.uint32_field(4)
    performant_frames: "CMsgServerSignoutData_ServerPerfStatsFrameCounts" = (
        betterproto.message_field(5)
    )
    long_frames: "CMsgServerSignoutData_ServerPerfStatsFrameCounts" = (
        betterproto.message_field(6)
    )
    low_idle_frames: "CMsgServerSignoutData_ServerPerfStatsFrameCounts" = (
        betterproto.message_field(7)
    )
    memory_bytes: int = betterproto.uint64_field(8)
    peak_memory_bytes: int = betterproto.uint64_field(9)


@dataclass
class CMsgServerSignoutData_ServerPerfStatsMatchPerfSamples(betterproto.Message):
    long_frame_threshold: float = betterproto.float_field(1)
    low_idle_threshold: float = betterproto.float_field(2)
    samples: List[
        "CMsgServerSignoutData_ServerPerfStatsPerfSample"
    ] = betterproto.message_field(3)


@dataclass
class CMsgServerToGCUpdateMatchInfo(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    kills_team_0: int = betterproto.uint32_field(3)
    kills_team_1: int = betterproto.uint32_field(4)
    net_worth_team_0: int = betterproto.uint32_field(5)
    net_worth_team_1: int = betterproto.uint32_field(6)
    spectators: int = betterproto.uint32_field(7)
    open_spectator_slots: int = betterproto.uint32_field(8)
    objectives_mask_team0: int = betterproto.uint64_field(9)
    objectives_mask_team1: int = betterproto.uint64_field(10)


@dataclass
class CMsgServerToGCMatchSignoutPermission(betterproto.Message):
    signout_start: int = betterproto.uint32_field(1)
    permission_request: int = betterproto.uint32_field(2)
    match_id: int = betterproto.uint64_field(3)
    match_mode: "ECitadelMatchMode" = betterproto.enum_field(4)


@dataclass
class CMsgServerToGCMatchSignoutPermissionResponse(betterproto.Message):
    can_sign_out: bool = betterproto.bool_field(1)
    retry_time_s: int = betterproto.uint32_field(2)
    requested_data: List["EGCServerSignoutData"] = betterproto.enum_field(3)


@dataclass
class CMsgServerSignoutData_Disconnections(betterproto.Message):
    disconnections: List[
        "CMsgServerSignoutData_DisconnectionsCMsgMatchDisconnection"
    ] = betterproto.message_field(1)


@dataclass
class CMsgServerSignoutData_DisconnectionsCMsgMatchDisconnection(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    disconnect_time: int = betterproto.uint32_field(2)
    connection_state: int = betterproto.uint32_field(3)
    reason_code: int = betterproto.uint32_field(4)
    reconnect_delay: int = betterproto.uint32_field(5)
    match_disconnect_time: int = betterproto.uint32_field(6)
    match_reconnect_delay: int = betterproto.uint32_field(7)


@dataclass
class CMsgServerSignoutData_DetailedStats(betterproto.Message):
    player_stats: List[
        "CMsgServerSignoutData_DetailedStatsPlayer"
    ] = betterproto.message_field(1)
    objectives: List[
        "CMsgServerSignoutData_DetailedStatsObjective"
    ] = betterproto.message_field(2)
    mid_boss: List[
        "CMsgServerSignoutData_DetailedStatsMidBoss"
    ] = betterproto.message_field(3)


@dataclass
class CMsgServerSignoutData_DetailedStatsPosition(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
    z: float = betterproto.float_field(3)


@dataclass
class CMsgServerSignoutData_DetailedStatsTimeSample(betterproto.Message):
    match_time_s: int = betterproto.uint32_field(1)
    stats: "CMsgServerSignoutData_DetailedStatsTimeSampleStats" = (
        betterproto.message_field(2)
    )
    gold_stats: "CMsgServerSignoutData_DetailedStatsTimeSampleGoldStats" = (
        betterproto.message_field(4)
    )


@dataclass
class CMsgServerSignoutData_DetailedStatsTimeSampleStats(betterproto.Message):
    net_worth: int = betterproto.uint32_field(1)
    kills: int = betterproto.uint32_field(2)
    deaths: int = betterproto.uint32_field(3)
    assists: int = betterproto.uint32_field(4)
    possible_creeps: int = betterproto.uint32_field(5)
    creep_kills: int = betterproto.uint32_field(6)
    neutral_kills: int = betterproto.uint32_field(7)
    creep_damage: int = betterproto.uint32_field(8)
    neutral_damage: int = betterproto.uint32_field(9)
    boss_damage: int = betterproto.uint32_field(10)
    player_damage: int = betterproto.uint32_field(11)
    denies: int = betterproto.uint32_field(12)
    player_healing: int = betterproto.uint32_field(13)
    ability_points: int = betterproto.uint32_field(14)
    self_healing: int = betterproto.uint32_field(15)
    player_damage_taken: int = betterproto.uint32_field(16)
    max_health: int = betterproto.uint32_field(17)
    weapon_power: int = betterproto.uint32_field(18)
    tech_power: int = betterproto.uint32_field(19)
    shots_hit: int = betterproto.uint32_field(20)
    shots_missed: int = betterproto.uint32_field(21)
    damage_absorbed: int = betterproto.uint32_field(22)
    absorption_provided: int = betterproto.uint32_field(23)
    heal_prevented: int = betterproto.uint32_field(26)
    heal_lost: int = betterproto.uint32_field(27)


@dataclass
class CMsgServerSignoutData_DetailedStatsTimeSampleGoldStats(betterproto.Message):
    player: int = betterproto.uint32_field(1)
    player_orb: int = betterproto.uint32_field(2)
    lane_creep_orb: int = betterproto.uint32_field(3)
    neutral_creep_orb: int = betterproto.uint32_field(4)
    boss: int = betterproto.uint32_field(5)
    boss_orb: int = betterproto.uint32_field(6)
    treasure: int = betterproto.uint32_field(7)
    denied: int = betterproto.uint32_field(8)
    death_loss: int = betterproto.uint32_field(9)
    lane_creep: int = betterproto.uint32_field(10)
    neutral_creep: int = betterproto.uint32_field(11)


@dataclass
class CMsgServerSignoutData_DetailedStatsObjective(betterproto.Message):
    destroyed_time_s: int = betterproto.uint32_field(2)
    creep_damage: int = betterproto.uint32_field(4)
    creep_damage_mitigated: int = betterproto.uint32_field(5)
    player_damage: int = betterproto.uint32_field(6)
    player_damage_mitigated: int = betterproto.uint32_field(7)
    first_damage_time_s: int = betterproto.uint32_field(8)
    team_objective_id: "ECitadelTeamObjective" = betterproto.enum_field(9)
    team: "ECitadelLobbyTeam" = betterproto.enum_field(10)


@dataclass
class CMsgServerSignoutData_DetailedStatsMidBoss(betterproto.Message):
    team_killed: "ECitadelLobbyTeam" = betterproto.enum_field(1)
    team_claimed: "ECitadelLobbyTeam" = betterproto.enum_field(2)
    destroyed_time_s: int = betterproto.uint32_field(3)


@dataclass
class CMsgServerSignoutData_DetailedStatsPlayer(betterproto.Message):
    player_slot: int = betterproto.uint32_field(1)
    time_samples: List[
        "CMsgServerSignoutData_DetailedStatsTimeSample"
    ] = betterproto.message_field(3)


@dataclass
class CMsgServerSignoutData_PerfData(betterproto.Message):
    average_frame_time: List[float] = betterproto.float_field(1)
    max_frame_time: List[float] = betterproto.float_field(2)
    server_average_frame_time: float = betterproto.float_field(3)
    server_max_frame_time: float = betterproto.float_field(4)
    average_compute_time: List[float] = betterproto.float_field(5)
    max_compute_time: List[float] = betterproto.float_field(6)
    average_client_tick_time: List[float] = betterproto.float_field(7)
    max_client_tick_time: List[float] = betterproto.float_field(8)
    average_client_simulate_time: List[float] = betterproto.float_field(9)
    max_client_simulate_time: List[float] = betterproto.float_field(10)
    average_output_time: List[float] = betterproto.float_field(11)
    max_output_time: List[float] = betterproto.float_field(12)
    average_wait_for_rendering_to_complete_time: List[float] = betterproto.float_field(
        13
    )
    max_wait_for_rendering_to_complete_time: List[float] = betterproto.float_field(14)
    average_swap_time: List[float] = betterproto.float_field(15)
    max_swap_time: List[float] = betterproto.float_field(16)
    average_frame_update_time: List[float] = betterproto.float_field(17)
    max_frame_update_time: List[float] = betterproto.float_field(18)
    average_idle_time: List[float] = betterproto.float_field(19)
    max_idle_time: List[float] = betterproto.float_field(20)
    average_input_processing_time: List[float] = betterproto.float_field(21)
    max_input_processing_time: List[float] = betterproto.float_field(22)


@dataclass
class CMsgServerSignoutData_BookRewards(betterproto.Message):
    account_rewards: List[
        "CMsgServerSignoutData_BookRewardsAccountRewards"
    ] = betterproto.message_field(1)


@dataclass
class CMsgServerSignoutData_BookRewardsBookReward(betterproto.Message):
    book_id: int = betterproto.uint32_field(1)
    xp_reward: int = betterproto.uint32_field(2)


@dataclass
class CMsgServerSignoutData_BookRewardsAccountRewards(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    book_reward: "CMsgServerSignoutData_BookRewardsBookReward" = (
        betterproto.message_field(2)
    )


@dataclass
class CMsgServerSignoutData_AccountStatChanges(betterproto.Message):
    account_stats: List[
        "CMsgServerSignoutData_AccountStatChangesAccountStats"
    ] = betterproto.message_field(1)


@dataclass
class CMsgServerSignoutData_AccountStatChangesStat(betterproto.Message):
    hero_id: int = betterproto.uint32_field(1)
    stat_id: int = betterproto.uint32_field(2)
    value: int = betterproto.uint32_field(3)
    medal: "ECitadelAccountStatMedal" = betterproto.enum_field(4)


@dataclass
class CMsgServerSignoutData_AccountStatChangesAccountStats(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    stats: List[
        "CMsgServerSignoutData_AccountStatChangesStat"
    ] = betterproto.message_field(2)


@dataclass
class CMsgServerSignoutData_PlayerChat(betterproto.Message):
    chat_lines: List[
        "CMsgServerSignoutData_PlayerChatChatLine"
    ] = betterproto.message_field(1)


@dataclass
class CMsgServerSignoutData_PlayerChatChatLine(betterproto.Message):
    player_slot: int = betterproto.uint32_field(1)
    game_time: float = betterproto.float_field(2)
    team_only: bool = betterproto.bool_field(3)
    chat_line: str = betterproto.string_field(4)


@dataclass
class CMsgServerSignoutData_PenalizedPlayers(betterproto.Message):
    penalized_players: List[
        "CMsgServerSignoutData_PenalizedPlayersPenalty"
    ] = betterproto.message_field(1)


@dataclass
class CMsgServerSignoutData_PenalizedPlayersPenalty(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    reason: "CMsgServerSignoutData_PenalizedPlayersEPenaltyReason" = (
        betterproto.enum_field(2)
    )
    match_time_s: int = betterproto.uint32_field(3)
    time_stamp: int = betterproto.uint32_field(4)


@dataclass
class CMsgMatchData(betterproto.Message):
    match_duration_s: int = betterproto.uint32_field(1)
    end_reason: "CMsgMatchDataEEndReason" = betterproto.enum_field(2)
    winning_team: "ECitadelLobbyTeam" = betterproto.enum_field(3)
    players: List["CMsgMatchDataPlayerInfo"] = betterproto.message_field(4)
    objectives_mask_legacy: int = betterproto.uint32_field(5)
    server_version: int = betterproto.uint32_field(6)
    game_mode: "ECitadelGameMode" = betterproto.enum_field(7)
    match_mode: "ECitadelMatchMode" = betterproto.enum_field(8)
    objectives_mask_team0: int = betterproto.uint64_field(9)
    objectives_mask_team1: int = betterproto.uint64_field(10)
    match_end_time: int = betterproto.uint32_field(11)
    stomp_score: float = betterproto.float_field(12)
    safe_to_abandon: bool = betterproto.bool_field(13)
    team_abandon: bool = betterproto.bool_field(14)
    new_player_pool: bool = betterproto.bool_field(15)
    low_pri_pool: bool = betterproto.bool_field(16)


@dataclass
class CMsgMatchDataPlayerItem(betterproto.Message):
    item_id: int = betterproto.uint32_field(1)
    game_time_s: int = betterproto.uint32_field(2)
    upgrade_id: int = betterproto.uint32_field(3)
    sold_time_s: int = betterproto.uint32_field(4)
    flags: int = betterproto.uint32_field(5)
    imbued_ability_id: int = betterproto.uint32_field(6)


@dataclass
class CMsgMatchDataPlayerInfo(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    team: "ECitadelLobbyTeam" = betterproto.enum_field(2)
    player_slot: int = betterproto.uint32_field(3)
    player_mmr: int = betterproto.uint32_field(5)
    player_uncertainty: int = betterproto.uint32_field(6)
    hero_id: int = betterproto.uint32_field(7)
    kills: int = betterproto.uint32_field(8)
    deaths: int = betterproto.uint32_field(9)
    net_worth: int = betterproto.uint32_field(10)
    assists: int = betterproto.uint32_field(11)
    hero_mmr: int = betterproto.uint32_field(12)
    items: List["CMsgMatchDataPlayerItem"] = betterproto.message_field(13)
    gpm_10min: int = betterproto.uint32_field(14)
    gpm_15min: int = betterproto.uint32_field(15)
    gpm_20min: int = betterproto.uint32_field(16)
    gpm_25min: int = betterproto.uint32_field(17)
    gpm_30min: int = betterproto.uint32_field(18)
    gpm_35min: int = betterproto.uint32_field(19)
    gpm_end: int = betterproto.uint32_field(20)
    last_hits: int = betterproto.uint32_field(21)
    denies: int = betterproto.uint32_field(22)
    ability_points: int = betterproto.uint32_field(23)
    level: int = betterproto.uint32_field(24)
    assigned_lane: int = betterproto.uint32_field(25)
    party_index: int = betterproto.uint32_field(26)
    platform: "EGCPlatform" = betterproto.enum_field(27)
    ability_damage: int = betterproto.uint32_field(28)
    bullet_damage: int = betterproto.uint32_field(29)
    hero_bullets_hit: int = betterproto.uint32_field(30)
    hero_bullets_hit_crit: int = betterproto.uint32_field(31)
    player_healing: int = betterproto.uint32_field(32)
    hero_bullets_fired: int = betterproto.uint32_field(33)
    hero_incoming_bullets_fired: int = betterproto.uint32_field(34)
    hero_incoming_bullets_hit: int = betterproto.uint32_field(35)
    hero_incoming_bullets_crit: int = betterproto.uint32_field(36)
    time_dead_s: int = betterproto.uint32_field(37)
    player_bullet_damage: int = betterproto.uint32_field(38)
    player_ability_damage: int = betterproto.uint32_field(39)
    player_melee_damage: int = betterproto.uint32_field(40)
    abandon_match_time_s: int = betterproto.uint32_field(41)
    abandon_time_stamp: int = betterproto.uint32_field(42)
    trooper_kill_excluded: int = betterproto.uint32_field(43)
    hero_bullets_lucky_shots: int = betterproto.uint32_field(44)


@dataclass
class CMsgServerToGCMatchSignout(betterproto.Message):
    additional_data: List["CExtraMsgBlock"] = betterproto.message_field(1)
    signout_attempt: int = betterproto.uint32_field(2)
    lobby_id: int = betterproto.uint64_field(3)
    match_id: int = betterproto.uint64_field(4)
    cluster_id: int = betterproto.uint32_field(9)
    match_data: "CMsgMatchData" = betterproto.message_field(10)


@dataclass
class CMsgServerToGCMatchSignoutResponse(betterproto.Message):
    result: "CMsgServerToGCMatchSignoutResponseESignoutResult" = betterproto.enum_field(
        1
    )


@dataclass
class CMsgServerWelcomeCitadel(betterproto.Message):
    pass


@dataclass
class CMsgServerToGCIdlePing(betterproto.Message):
    server_version: int = betterproto.uint32_field(1)


@dataclass
class CMsgGCToServerRequestPing(betterproto.Message):
    pass


@dataclass
class CMsgGCToServerAllocateForMatch(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)


@dataclass
class CMsgGCToServerAllocateForMatchResponse(betterproto.Message):
    success: bool = betterproto.bool_field(1)


@dataclass
class CMsgServerToGCEnterMatchmaking(betterproto.Message):
    server_version: int = betterproto.uint32_field(1)
    search_key: str = betterproto.string_field(2)
    region_id: int = betterproto.uint32_field(3)
    cluster_id: int = betterproto.uint32_field(4)
    server_public_ip: int = betterproto.uint32_field(5)
    server_private_ip: int = betterproto.uint32_field(6)
    server_port: int = betterproto.uint32_field(7)
    sdr_address: bytes = betterproto.bytes_field(9)


@dataclass
class CMsgGCToServerCancelAllocateForMatch(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)


@dataclass
class CMsgServerToGCUpdateLobbyServerState(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    server_state: "ELobbyServerState" = betterproto.enum_field(2)
    safe_to_abandon: bool = betterproto.bool_field(3)


@dataclass
class CMsgServerToGCAbandonMatch(betterproto.Message):
    server_steam_id: float = betterproto.fixed64_field(1)
    lobby_id: float = betterproto.fixed64_field(2)
    cluster_id: int = betterproto.uint32_field(3)
    reason_code: "CMsgServerToGCAbandonMatchEReason" = betterproto.enum_field(4)
    additional_data: int = betterproto.uint64_field(5)
    match_id: int = betterproto.uint64_field(6)
    players: List["CMsgServerToGCAbandonMatchPlayer"] = betterproto.message_field(8)
    public_ip_address: float = betterproto.fixed32_field(9)
    port: int = betterproto.uint32_field(10)
    server_version: int = betterproto.uint32_field(11)
    pid: int = betterproto.uint32_field(12)
    instance_id: int = betterproto.uint32_field(13)
    private_ip_address: int = betterproto.uint32_field(14)
    match_mode: "ECitadelMatchMode" = betterproto.enum_field(15)
    game_mode: "ECitadelGameMode" = betterproto.enum_field(16)
    was_server_shutdown: bool = betterproto.bool_field(17)


@dataclass
class CMsgServerToGCAbandonMatchPlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    additional_data: int = betterproto.uint64_field(2)
    hero_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgServerToGCAbandonMatchResponse(betterproto.Message):
    pass


@dataclass
class CMsgServerToGCTestConnection(betterproto.Message):
    pass


@dataclass
class CMsgServerToGCTestConnectionResponse(betterproto.Message):
    state: int = betterproto.uint32_field(1)
    lobby_id: int = betterproto.uint64_field(2)


@dataclass
class CMsgGCToServerSetServerConVar(betterproto.Message):
    convar_name: str = betterproto.string_field(1)
    convar_value: str = betterproto.string_field(2)


@dataclass
class CMsgGCToServerSetServerConVarResponse(betterproto.Message):
    success: bool = betterproto.bool_field(1)


@dataclass
class CMsgGCToServerAddSpectator(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    account_id: int = betterproto.uint32_field(2)
    account_to_spectate: int = betterproto.uint32_field(3)


@dataclass
class CMsgGCToServerAddSpectatorResponse(betterproto.Message):
    result: "CMsgGCToServerAddSpectatorResponseEResponse" = betterproto.enum_field(1)
    requesting_account_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgServerToGCReportCheater(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    match_id: int = betterproto.uint64_field(2)
    lobby_id: float = betterproto.fixed64_field(3)
    reason: str = betterproto.string_field(4)


@dataclass
class CMsgServerToGCReportCheaterResponse(betterproto.Message):
    success: bool = betterproto.bool_field(1)
