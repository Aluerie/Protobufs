# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_common_league.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class ELeagueNodeGroupType(betterproto.Enum):
    INVALID_GROUP_TYPE = 0
    ORGANIZATIONAL = 1
    ROUND_ROBIN = 2
    SWISS = 3
    BRACKET_SINGLE = 4
    BRACKET_DOUBLE_SEED_LOSER = 5
    BRACKET_DOUBLE_ALL_WINNER = 6
    SHOWMATCH = 7
    GSL = 8
    PLACEMENT = 9


class ELeagueNodeType(betterproto.Enum):
    INVALID_NODE_TYPE = 0
    BEST_OF_ONE = 1
    BEST_OF_THREE = 2
    BEST_OF_FIVE = 3
    BEST_OF_TWO = 4


@dataclass
class CMsgDOTALeagueNode(betterproto.Message):
    name: str = betterproto.string_field(1)
    node_id: int = betterproto.uint32_field(2)
    node_group_id: int = betterproto.uint32_field(3)
    winning_node_id: int = betterproto.uint32_field(4)
    losing_node_id: int = betterproto.uint32_field(5)
    incoming_node_id_1: int = betterproto.uint32_field(6)
    incoming_node_id_2: int = betterproto.uint32_field(7)
    node_type: "ELeagueNodeType" = betterproto.enum_field(8)
    scheduled_time: int = betterproto.uint32_field(9)
    actual_time: int = betterproto.uint32_field(19)
    series_id: int = betterproto.uint32_field(10)
    team_id_1: int = betterproto.uint32_field(11)
    team_id_2: int = betterproto.uint32_field(12)
    matches: List["CMsgDOTALeagueNodeMatchDetails"] = betterproto.message_field(13)
    team_1_wins: int = betterproto.uint32_field(14)
    team_2_wins: int = betterproto.uint32_field(15)
    has_started: bool = betterproto.bool_field(16)
    is_completed: bool = betterproto.bool_field(17)
    stream_ids: List[int] = betterproto.uint32_field(18)
    vods: List["CMsgDOTALeagueNodeVOD"] = betterproto.message_field(20)


@dataclass
class CMsgDOTALeagueNodeMatchDetails(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)
    winning_team_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTALeagueNodeVOD(betterproto.Message):
    series_game: int = betterproto.uint32_field(1)
    stream_id: int = betterproto.uint32_field(2)
    url: str = betterproto.string_field(3)


@dataclass
class CMsgDOTALeagueNodeGroup(betterproto.Message):
    name: str = betterproto.string_field(1)
    node_group_id: int = betterproto.uint32_field(2)
    parent_node_group_id: int = betterproto.uint32_field(3)
    incoming_node_group_ids: List[int] = betterproto.uint32_field(4)
    advancing_node_group_id: int = betterproto.uint32_field(5)
    advancing_team_count: int = betterproto.uint32_field(6)
    team_count: int = betterproto.uint32_field(7)
    node_group_type: "ELeagueNodeGroupType" = betterproto.enum_field(8)
    default_node_type: "ELeagueNodeType" = betterproto.enum_field(9)
    round: int = betterproto.uint32_field(10)
    max_rounds: int = betterproto.uint32_field(11)
    is_tiebreaker: bool = betterproto.bool_field(12)
    is_final_group: bool = betterproto.bool_field(13)
    is_completed: bool = betterproto.bool_field(14)
    phase: "ELeaguePhase" = betterproto.enum_field(18)
    region: "ELeagueRegion" = betterproto.enum_field(19)
    start_time: int = betterproto.uint32_field(20)
    end_time: int = betterproto.uint32_field(21)
    secondary_advancing_node_group_id: int = betterproto.uint32_field(22)
    secondary_advancing_team_count: int = betterproto.uint32_field(23)
    tertiary_advancing_node_group_id: int = betterproto.uint32_field(24)
    tertiary_advancing_team_count: int = betterproto.uint32_field(25)
    elimination_dpc_points: int = betterproto.uint32_field(26)
    team_standings: List[
        "CMsgDOTALeagueNodeGroupTeamStanding"
    ] = betterproto.message_field(15)
    nodes: List["CMsgDOTALeagueNode"] = betterproto.message_field(16)
    node_groups: List["CMsgDOTALeagueNodeGroup"] = betterproto.message_field(17)


@dataclass
class CMsgDOTALeagueNodeGroupTeamStanding(betterproto.Message):
    standing: int = betterproto.uint32_field(1)
    team_id: int = betterproto.uint32_field(2)
    team_name: str = betterproto.string_field(3)
    team_tag: str = betterproto.string_field(4)
    team_logo: int = betterproto.uint64_field(5)
    team_logo_url: str = betterproto.string_field(6)
    wins: int = betterproto.uint32_field(7)
    losses: int = betterproto.uint32_field(8)
    score: int = betterproto.int64_field(9)
    team_abbreviation: str = betterproto.string_field(10)
    score_tiebreak_group: int = betterproto.int64_field(11)
    score_tiebreak_below: int = betterproto.int64_field(12)
    score_tiebreak_random: int = betterproto.int64_field(13)
    is_pro: bool = betterproto.bool_field(14)


@dataclass
class CMsgDOTALeague(betterproto.Message):
    info: "CMsgDOTALeagueInfo" = betterproto.message_field(1)
    prize_pool: "CMsgDOTALeaguePrizePool" = betterproto.message_field(2)
    admins: List["CMsgDOTALeagueAdmin"] = betterproto.message_field(3)
    streams: List["CMsgDOTALeagueStream"] = betterproto.message_field(4)
    node_groups: List["CMsgDOTALeagueNodeGroup"] = betterproto.message_field(5)
    series_infos: List["CMsgDOTALeagueSeriesInfo"] = betterproto.message_field(6)
    registered_players: List["CMsgDOTALeaguePlayer"] = betterproto.message_field(7)


@dataclass
class CMsgDOTALeagueInfo(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    tier: "ELeagueTier" = betterproto.enum_field(3)
    region: "ELeagueRegion" = betterproto.enum_field(4)
    url: str = betterproto.string_field(5)
    description: str = betterproto.string_field(6)
    notes: str = betterproto.string_field(7)
    start_timestamp: int = betterproto.uint32_field(8)
    end_timestamp: int = betterproto.uint32_field(9)
    pro_circuit_points: int = betterproto.uint32_field(10)
    image_bits: int = betterproto.uint32_field(11)
    status: "ELeagueStatus" = betterproto.enum_field(12)
    most_recent_activity: int = betterproto.uint32_field(13)
    registration_period: int = betterproto.uint32_field(14)


@dataclass
class CMsgDOTALeagueAdmin(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    is_primary: bool = betterproto.bool_field(2)
    email_address: str = betterproto.string_field(3)


@dataclass
class CMsgDOTALeaguePrizePoolItem(betterproto.Message):
    item_def: int = betterproto.uint32_field(1)
    sales_stop_timestamp: int = betterproto.uint32_field(2)
    revenue_pct: int = betterproto.uint32_field(3)
    revenue_cents_per_sale: int = betterproto.uint32_field(4)


@dataclass
class CMsgDOTALeaguePrizePool(betterproto.Message):
    base_prize_pool: int = betterproto.uint32_field(1)
    total_prize_pool: int = betterproto.uint32_field(2)
    prize_split_pct_x100: List[int] = betterproto.uint32_field(3)
    prize_pool_items: List["CMsgDOTALeaguePrizePoolItem"] = betterproto.message_field(4)


@dataclass
class CMsgDOTALeagueStream(betterproto.Message):
    stream_id: int = betterproto.uint32_field(1)
    language: int = betterproto.uint32_field(2)
    name: str = betterproto.string_field(3)
    broadcast_provider: "ELeagueBroadcastProvider" = betterproto.enum_field(4)
    stream_url: str = betterproto.string_field(5)
    vod_url: str = betterproto.string_field(6)


@dataclass
class CMsgDOTALeagueSeriesInfo(betterproto.Message):
    series_id: int = betterproto.uint32_field(1)
    series_type: int = betterproto.uint32_field(2)
    start_time: int = betterproto.uint32_field(3)
    match_ids: List[int] = betterproto.uint64_field(4)
    team_id_1: int = betterproto.uint32_field(5)
    team_id_2: int = betterproto.uint32_field(6)


@dataclass
class CMsgDOTALeaguePlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    team_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgDOTALeagueList(betterproto.Message):
    leagues: List["CMsgDOTALeague"] = betterproto.message_field(1)


@dataclass
class CMsgDOTALeagueInfo(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    tier: "ELeagueTier" = betterproto.enum_field(3)
    region: "ELeagueRegion" = betterproto.enum_field(4)
    most_recent_activity: int = betterproto.uint32_field(5)
    total_prize_pool: int = betterproto.uint32_field(6)
    start_timestamp: int = betterproto.uint32_field(7)
    end_timestamp: int = betterproto.uint32_field(8)
    status: int = betterproto.uint32_field(9)


@dataclass
class CMsgDOTALeagueInfoList(betterproto.Message):
    infos: List["CMsgDOTALeagueInfo"] = betterproto.message_field(1)


@dataclass
class CMsgDOTALeagueLiveGames(betterproto.Message):
    games: List["CMsgDOTALeagueLiveGamesLiveGame"] = betterproto.message_field(1)


@dataclass
class CMsgDOTALeagueLiveGamesLiveGame(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    server_steam_id: int = betterproto.uint64_field(2)
    radiant_name: str = betterproto.string_field(3)
    radiant_logo: int = betterproto.uint64_field(4)
    radiant_team_id: int = betterproto.uint32_field(9)
    dire_name: str = betterproto.string_field(5)
    dire_logo: int = betterproto.uint64_field(6)
    dire_team_id: int = betterproto.uint32_field(10)
    time: int = betterproto.uint32_field(7)
    spectators: int = betterproto.uint32_field(8)
    league_node_id: int = betterproto.uint32_field(11)
    series_id: int = betterproto.uint32_field(12)
    match_id: int = betterproto.uint64_field(13)


@dataclass
class CMsgDOTALeagueMessages(betterproto.Message):
    messages: List["CMsgDOTALeagueMessagesMessage"] = betterproto.message_field(1)


@dataclass
class CMsgDOTALeagueMessagesMessage(betterproto.Message):
    author_account_id: int = betterproto.uint32_field(1)
    timestamp: int = betterproto.uint32_field(2)
    message: str = betterproto.string_field(3)


@dataclass
class CMsgDOTALeaguePrizePool(betterproto.Message):
    prize_pool: int = betterproto.uint32_field(1)
    increment_per_second: float = betterproto.float_field(2)


@dataclass
class CMsgDOTALeagueInfoListAdminsRequest(betterproto.Message):
    pass


@dataclass
class CMsgDOTALeagueAvailableLobbyNodesRequest(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgDOTALeagueAvailableLobbyNodes(betterproto.Message):
    node_infos: List[
        "CMsgDOTALeagueAvailableLobbyNodesNodeInfo"
    ] = betterproto.message_field(1)


@dataclass
class CMsgDOTALeagueAvailableLobbyNodesNodeInfo(betterproto.Message):
    node_id: int = betterproto.uint32_field(1)
    node_name: str = betterproto.string_field(2)
    node_group_name: str = betterproto.string_field(3)
    team_id_1: int = betterproto.uint32_field(4)
    team_id_2: int = betterproto.uint32_field(5)


@dataclass
class CMsgDOTALeagueNodeResults(betterproto.Message):
    node_results: List["CMsgDOTALeagueNodeResultsResult"] = betterproto.message_field(1)


@dataclass
class CMsgDOTALeagueNodeResultsResult(betterproto.Message):
    node_id: int = betterproto.uint32_field(1)
    winning_node_id: int = betterproto.uint32_field(2)
    losing_node_id: int = betterproto.uint32_field(3)
    incoming_node_id_1: int = betterproto.uint32_field(4)
    incoming_node_id_2: int = betterproto.uint32_field(5)
    team_id_1: int = betterproto.uint32_field(6)
    team_id_2: int = betterproto.uint32_field(7)
    team_1_name: str = betterproto.string_field(8)
    team_2_name: str = betterproto.string_field(9)
    team_1_wins: int = betterproto.uint32_field(10)
    team_2_wins: int = betterproto.uint32_field(11)
    winning_team_id: int = betterproto.uint32_field(12)
    losing_team_id: int = betterproto.uint32_field(13)
    has_started: bool = betterproto.bool_field(14)
    is_completed: bool = betterproto.bool_field(15)
    scheduled_time: int = betterproto.uint32_field(16)
    match_ids: List[int] = betterproto.uint64_field(17)


@dataclass
class CMsgDOTADPCLeagueResults(betterproto.Message):
    results: List["CMsgDOTADPCLeagueResultsResult"] = betterproto.message_field(1)
    points: List[int] = betterproto.uint32_field(2)
    dollars: List[int] = betterproto.uint32_field(3)


@dataclass
class CMsgDOTADPCLeagueResultsResult(betterproto.Message):
    standing: int = betterproto.uint32_field(1)
    team_id: int = betterproto.uint32_field(2)
    team_name: str = betterproto.string_field(3)
    team_logo: int = betterproto.uint64_field(4)
    team_logo_url: str = betterproto.string_field(5)
    points: int = betterproto.uint32_field(6)
    earnings: int = betterproto.uint32_field(7)
    timestamp: int = betterproto.uint32_field(8)
    phase: "ELeaguePhase" = betterproto.enum_field(9)
    team_abbreviation: str = betterproto.string_field(10)


@dataclass
class CMsgDOTADPCTeamResults(betterproto.Message):
    results: List["CMsgDOTADPCTeamResultsResult"] = betterproto.message_field(1)


@dataclass
class CMsgDOTADPCTeamResultsResult(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    standing: int = betterproto.uint32_field(2)
    points: int = betterproto.uint32_field(3)
    earnings: int = betterproto.uint32_field(4)
    timestamp: int = betterproto.uint32_field(5)


@dataclass
class CMsgDOTADPCSeasonResults(betterproto.Message):
    results: List["CMsgDOTADPCSeasonResultsTeamResult"] = betterproto.message_field(1)
    standings: List["CMsgDOTADPCSeasonResultsStanding"] = betterproto.message_field(2)
    major_wildcard_standings: List[
        "CMsgDOTADPCSeasonResultsStandingEntry"
    ] = betterproto.message_field(3)
    major_group_standings: List[
        "CMsgDOTADPCSeasonResultsStandingEntry"
    ] = betterproto.message_field(4)
    major_playoff_standings: List[
        "CMsgDOTADPCSeasonResultsStandingEntry"
    ] = betterproto.message_field(5)


@dataclass
class CMsgDOTADPCSeasonResultsTeamLeagueResult(betterproto.Message):
    timestamp: int = betterproto.uint32_field(1)
    league_id: int = betterproto.uint32_field(2)
    standing: int = betterproto.uint32_field(3)
    points: int = betterproto.uint32_field(4)
    earnings: int = betterproto.uint32_field(5)
    audit_action: int = betterproto.uint32_field(6)
    audit_data: int = betterproto.uint32_field(7)


@dataclass
class CMsgDOTADPCSeasonResultsTeamResult(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)
    team_name: str = betterproto.string_field(2)
    team_abbreviation: str = betterproto.string_field(8)
    team_logo: int = betterproto.uint64_field(3)
    team_logo_url: str = betterproto.string_field(4)
    total_points: int = betterproto.uint32_field(5)
    total_earnings: int = betterproto.uint32_field(6)
    league_results: List[
        "CMsgDOTADPCSeasonResultsTeamLeagueResult"
    ] = betterproto.message_field(7)


@dataclass
class CMsgDOTADPCSeasonResultsStandingEntry(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)
    wins: int = betterproto.uint32_field(2)
    losses: int = betterproto.uint32_field(3)
    team_url: str = betterproto.string_field(4)
    team_name: str = betterproto.string_field(5)
    team_abbreviation: str = betterproto.string_field(6)


@dataclass
class CMsgDOTADPCSeasonResultsStanding(betterproto.Message):
    region: "ELeagueRegion" = betterproto.enum_field(1)
    division: "ELeagueDivision" = betterproto.enum_field(2)
    entries: List["CMsgDOTADPCSeasonResultsStandingEntry"] = betterproto.message_field(
        3
    )


@dataclass
class CMsgDOTADPCSeasonSpoilerResults(betterproto.Message):
    time_last_updated: int = betterproto.uint32_field(1)
    saved_results: "CMsgDOTADPCSeasonResults" = betterproto.message_field(2)
