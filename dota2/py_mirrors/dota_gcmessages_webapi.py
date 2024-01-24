# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_webapi.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class ETeamFanContentStatus(betterproto.Enum):
    TEAM_FAN_CONTENT_STATUS_INVALID = 0
    TEAM_FAN_CONTENT_STATUS_PENDING = 1
    TEAM_FAN_CONTENT_STATUS_EVALUATED = 2


class ETeamFanContentAssetType(betterproto.Enum):
    k_eFanContentAssetType_LogoPNG = 1
    k_eFanContentAssetType_LogoSVG = 2
    k_eFanContentAssetType_Logo3D = 3
    k_eFanContentAssetType_Players = 4
    k_eFanContentAssetType_Sprays = 5
    k_eFanContentAssetType_Wallpapers = 6
    k_eFanContentAssetType_Emoticons = 7
    k_eFanContentAssetType_VoiceLines = 8
    k_eFanContentAssetType_Localization = 9


class ETeamFanContentAssetStatus(betterproto.Enum):
    k_eFanContentAssetStatus_None = 0
    k_eFanContentAssetStatus_Approved = 1
    k_eFanContentAssetStatus_Rejected = 2


class CMsgArcanaVotesVotingState(betterproto.Enum):
    FINISHED = 0
    IN_PROGRESS = 1
    IN_FUTURE = 2


class CMsgDOTADPCFeedEFeedElementType(betterproto.Enum):
    FEED_SERIES_RESULT = 1
    FEED_MATCH_POPULAR = 2
    FEED_TEAM_UPCOMING_MATCH = 3
    FEED_TEAM_LEAGUE_RESULT = 4
    FEED_TEAM_ADD_PLAYER = 5
    FEED_TEAM_REMOVE_PLAYER = 6
    FEED_TEAM_DISBAND = 7
    FEED_LEAGUE_UPCOMING = 8
    FEED_LEAGUE_CONCLUDED = 9
    FEED_DPC_STANDINGS = 10
    FEED_ALERT_PREDICTIONS = 11
    FEED_ALERT_FANTASY = 12
    FEED_LEAGUE_LIVE_MATCH = 13
    FEED_LEAGUE_INPROGRESS_SERIES = 14


class CMsgTeamFanContentAssetStatusResponseEResult(betterproto.Enum):
    k_eSuccess = 0
    k_eInternalError = 1


class CMsgDPCEventELeagueEvent(betterproto.Enum):
    EVENT_INVALID = 0
    SPRING_2021_LEAGUE = 1
    SPRING_2021_MAJOR = 2
    INTERNATIONAL_2021_QUALIFIERS = 3
    INTERNATIONAL_2021 = 4
    WINTER_2021_LEAGUE = 5
    WINTER_2021_LEAGUE_FINALS = 6
    SPRING_2022_LEAGUE = 7
    SPRING_2022_MAJOR = 8
    SUMMER_2022_LEAGUE = 9
    SUMMER_2022_MAJOR = 10
    INTERNATIONAL_2022 = 11
    CHINA_REGIONAL_FINALS = 12
    INTERNATIONAL_2022_REGIONAL_QUALIFIERS = 13
    INTERNATIONAL_2022_LAST_CHANCE_QUALIFIERS = 14
    WINTER_2023_LEAGUE = 15
    WINTER_2023_MAJOR = 16
    SPRING_2023_LEAGUE = 17
    SPRING_2023_MAJOR = 18
    SUMMER_2023_LEAGUE = 19
    SUMMER_2023_MAJOR = 20
    INTERNATIONAL_2023 = 21


class CMsgDPCEventELeagueEventPhase(betterproto.Enum):
    PHASE_INVALID = 0
    WILD_CARD = 1
    GROUP_STAGE = 2
    GROUP_A = 3
    GROUP_B = 4
    OVERALL = 5
    PLAYOFF = 6
    RESULTS = 7
    DPC_POINT_STANDINGS = 8
    GROUP_C = 9
    GROUP_D = 10
    PLACEMENT = 11


class CMsgDPCEventELeagueEventType(betterproto.Enum):
    UNKNOWN = 0
    LEAGUE = 1
    MAJOR = 2
    INTERNATIONAL_QUALIFIERS = 3
    INTERNATIONAL = 4
    LEAGUE_FINALS = 5


class CMsgDPCEventETour(betterproto.Enum):
    TOUR_NONE = 0
    TOUR_1 = 1
    TOUR_2 = 2
    TOUR_3 = 3


@dataclass
class CMsgArcanaVotes(betterproto.Message):
    matches: List["CMsgArcanaVotesMatch"] = betterproto.message_field(1)
    round_time_remaining: int = betterproto.uint32_field(2)
    round_number: int = betterproto.uint32_field(3)
    voting_state: int = betterproto.uint32_field(4)
    is_current_round_calibrating: bool = betterproto.bool_field(5)
    closest_active_match_id: int = betterproto.uint32_field(6)
    event_id: int = betterproto.uint32_field(7)
    voting_start_time: int = betterproto.uint32_field(8)


@dataclass
class CMsgArcanaVotesMatch(betterproto.Message):
    match_id: int = betterproto.uint32_field(1)
    hero_id_0: int = betterproto.uint32_field(2)
    hero_id_1: int = betterproto.uint32_field(3)
    hero_seeding_0: int = betterproto.uint32_field(4)
    hero_seeding_1: int = betterproto.uint32_field(5)
    vote_count_0: int = betterproto.uint32_field(6)
    vote_count_1: int = betterproto.uint32_field(7)
    voting_state: int = betterproto.uint32_field(8)
    round_number: int = betterproto.uint32_field(9)
    is_votes_hidden: bool = betterproto.bool_field(10)
    calibration_time_remaining: int = betterproto.uint32_field(11)


@dataclass
class CMsgDOTADPCFeed(betterproto.Message):
    elements: List["CMsgDOTADPCFeedElement"] = betterproto.message_field(1)


@dataclass
class CMsgDOTADPCFeedElement(betterproto.Message):
    type: "CMsgDOTADPCFeedEFeedElementType" = betterproto.enum_field(1)
    timestamp: int = betterproto.uint32_field(2)
    series_id: int = betterproto.uint32_field(3)
    match_id: int = betterproto.uint64_field(4)
    team_id: int = betterproto.uint32_field(5)
    account_id: int = betterproto.uint32_field(6)
    league_id: int = betterproto.uint32_field(7)
    node_id: int = betterproto.uint32_field(8)
    server_steam_id: int = betterproto.uint64_field(13)
    data_1: int = betterproto.uint32_field(9)
    data_2: int = betterproto.uint32_field(10)
    data_3: int = betterproto.uint32_field(11)
    data_4: int = betterproto.uint32_field(12)


@dataclass
class CMsgDOTADPCUserInfo(betterproto.Message):
    is_plus_subscriber: bool = betterproto.bool_field(1)


@dataclass
class CMsgDraftTrivia(betterproto.Message):
    has_valid_match: bool = betterproto.bool_field(1)
    match_hero_info: "CMsgDraftTriviaDraftTriviaMatchInfo" = betterproto.message_field(
        2
    )
    match_rank_tier: int = betterproto.uint32_field(3)
    end_time: int = betterproto.uint32_field(4)
    event_id: int = betterproto.uint32_field(5)
    current_match_voted_radiant: bool = betterproto.bool_field(6)
    previous_result: "CMsgDraftTriviaPreviousResult" = betterproto.message_field(7)
    current_streak: int = betterproto.uint32_field(8)


@dataclass
class CMsgDraftTriviaDraftTriviaHeroInfo(betterproto.Message):
    hero_id: int = betterproto.uint32_field(1)
    role: int = betterproto.uint32_field(2)


@dataclass
class CMsgDraftTriviaDraftTriviaMatchInfo(betterproto.Message):
    radiant_heroes: List[
        "CMsgDraftTriviaDraftTriviaHeroInfo"
    ] = betterproto.message_field(1)
    dire_heroes: List["CMsgDraftTriviaDraftTriviaHeroInfo"] = betterproto.message_field(
        2
    )


@dataclass
class CMsgDraftTriviaPreviousResult(betterproto.Message):
    voted_correctly: bool = betterproto.bool_field(1)
    voted_radiant: bool = betterproto.bool_field(2)
    match_hero_info: "CMsgDraftTriviaDraftTriviaMatchInfo" = betterproto.message_field(
        3
    )
    match_rank_tier: int = betterproto.uint32_field(4)
    end_time: int = betterproto.uint32_field(5)
    match_id: int = betterproto.uint64_field(6)


@dataclass
class CMsgTeamFanContentAssetStatus(betterproto.Message):
    asset_type: "ETeamFanContentAssetType" = betterproto.enum_field(1)
    asset_index: int = betterproto.uint32_field(2)
    asset_status: "ETeamFanContentAssetStatus" = betterproto.enum_field(3)
    crc: int = betterproto.uint32_field(4)


@dataclass
class CMsgTeamFanContentAssetStatusResponse(betterproto.Message):
    result: "CMsgTeamFanContentAssetStatusResponseEResult" = betterproto.enum_field(1)


@dataclass
class CMsgTeamFanContentStatus(betterproto.Message):
    team_status_list: List[
        "CMsgTeamFanContentStatusTeamStatus"
    ] = betterproto.message_field(1)


@dataclass
class CMsgTeamFanContentStatusTeamStatus(betterproto.Message):
    name: str = betterproto.string_field(1)
    team_id: int = betterproto.uint32_field(2)
    logo_url: str = betterproto.string_field(3)
    status: "ETeamFanContentStatus" = betterproto.enum_field(4)
    timestamp: int = betterproto.uint32_field(5)
    ugc_logo: int = betterproto.uint64_field(7)
    workshop_account_id: int = betterproto.uint32_field(8)
    abbreviation: str = betterproto.string_field(9)
    voiceline_count: int = betterproto.uint32_field(10)
    spray_count: int = betterproto.uint32_field(11)
    emoticon_count: int = betterproto.uint32_field(12)
    wallpaper_count: int = betterproto.uint32_field(13)
    comment: str = betterproto.string_field(14)
    comment_timestamp: int = betterproto.uint32_field(15)
    asset_status: List["CMsgTeamFanContentAssetStatus"] = betterproto.message_field(16)
    email_timestamp: int = betterproto.uint32_field(17)
    email_tier: int = betterproto.uint32_field(18)
    languages: str = betterproto.string_field(19)


@dataclass
class CMsgTeamFanContentAutographStatus(betterproto.Message):
    team_autographs: List[
        "CMsgTeamFanContentAutographStatusTeamStatus"
    ] = betterproto.message_field(1)


@dataclass
class CMsgTeamFanContentAutographStatusAutographStatus(betterproto.Message):
    pro_name: str = betterproto.string_field(1)
    account_id: int = betterproto.uint32_field(2)
    timestamp: int = betterproto.uint32_field(3)
    file: str = betterproto.string_field(4)


@dataclass
class CMsgTeamFanContentAutographStatusTeamStatus(betterproto.Message):
    name: str = betterproto.string_field(1)
    team_id: int = betterproto.uint32_field(2)
    autographs: List[
        "CMsgTeamFanContentAutographStatusAutographStatus"
    ] = betterproto.message_field(3)
    workshop_account_id: int = betterproto.uint32_field(4)


@dataclass
class CMsgDPCEvent(betterproto.Message):
    event: "CMsgDPCEventELeagueEvent" = betterproto.enum_field(1)
    event_type: "CMsgDPCEventELeagueEventType" = betterproto.enum_field(2)
    leagues: List["CMsgDPCEventLeague"] = betterproto.message_field(3)
    registration_period: int = betterproto.uint32_field(4)
    is_event_upcoming: bool = betterproto.bool_field(5)
    is_event_completed: bool = betterproto.bool_field(6)
    event_name: str = betterproto.string_field(7)
    multicast_league_id: int = betterproto.uint32_field(8)
    multicast_streams: List[int] = betterproto.uint32_field(9)
    tour: "CMsgDPCEventETour" = betterproto.enum_field(10)
    timestamp_drop_lock: int = betterproto.uint32_field(12)
    timestamp_add_lock: int = betterproto.uint32_field(13)
    timestamp_content_deadline: int = betterproto.uint32_field(14)
    is_fantasy_enabled: bool = betterproto.bool_field(15)
    timestamp_content_review_deadline: int = betterproto.uint32_field(16)


@dataclass
class CMsgDPCEventPhaseInfo(betterproto.Message):
    phase: "CMsgDPCEventELeagueEventPhase" = betterproto.enum_field(1)
    node_group_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgDPCEventLeague(betterproto.Message):
    region: "ELeagueRegion" = betterproto.enum_field(1)
    division: "ELeagueDivision" = betterproto.enum_field(2)
    league_id: int = betterproto.uint32_field(3)
    phases: List["CMsgDPCEventPhaseInfo"] = betterproto.message_field(4)


@dataclass
class CMsgDPCEventList(betterproto.Message):
    events: List["CMsgDPCEvent"] = betterproto.message_field(1)


@dataclass
class CMsgDOTAFantasyCardLineup(betterproto.Message):
    periods: List["CMsgDOTAFantasyCardLineupPeriod"] = betterproto.message_field(1)


@dataclass
class CMsgDOTAFantasyCardLineupCardBonus(betterproto.Message):
    bonus_stat: int = betterproto.uint32_field(1)
    bonus_value: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTAFantasyCardLineupCard(betterproto.Message):
    player_account_id: int = betterproto.uint32_field(1)
    player_name: str = betterproto.string_field(2)
    team_id: int = betterproto.uint32_field(3)
    team_name: str = betterproto.string_field(4)
    role: int = betterproto.uint32_field(5)
    bonuses: List["CMsgDOTAFantasyCardLineupCardBonus"] = betterproto.message_field(6)
    score: float = betterproto.float_field(7)
    finalized: bool = betterproto.bool_field(8)
    item_id: int = betterproto.uint64_field(9)


@dataclass
class CMsgDOTAFantasyCardLineupLeague(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    cards: List["CMsgDOTAFantasyCardLineupCard"] = betterproto.message_field(2)
    score: float = betterproto.float_field(3)


@dataclass
class CMsgDOTAFantasyCardLineupPeriod(betterproto.Message):
    fantasy_period: int = betterproto.uint32_field(1)
    timestamp_start: int = betterproto.uint32_field(2)
    timestamp_end: int = betterproto.uint32_field(3)
    leagues: List["CMsgDOTAFantasyCardLineupLeague"] = betterproto.message_field(4)


@dataclass
class CMsgDOTAFantasyCardList(betterproto.Message):
    cards: List["CMsgDOTAFantasyCardListCard"] = betterproto.message_field(1)


@dataclass
class CMsgDOTAFantasyCardListCardBonus(betterproto.Message):
    bonus_stat: int = betterproto.uint32_field(1)
    bonus_value: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTAFantasyCardListCard(betterproto.Message):
    player_account_id: int = betterproto.uint32_field(1)
    player_name: str = betterproto.string_field(2)
    team_id: int = betterproto.uint32_field(3)
    team_name: str = betterproto.string_field(4)
    role: int = betterproto.uint32_field(5)
    bonuses: List["CMsgDOTAFantasyCardListCardBonus"] = betterproto.message_field(6)
    item_id: int = betterproto.uint64_field(8)


@dataclass
class CMsgChatToxicityToxicPlayerMatchesReport(betterproto.Message):
    rows: List[
        "CMsgChatToxicityToxicPlayerMatchesReportIndividualRow"
    ] = betterproto.message_field(1)


@dataclass
class CMsgChatToxicityToxicPlayerMatchesReportIndividualRow(betterproto.Message):
    player_account_id: int = betterproto.uint32_field(1)
    num_matches_seen: int = betterproto.uint32_field(2)
    num_messages: int = betterproto.uint32_field(3)
    num_messages_toxic: int = betterproto.uint32_field(4)
    first_match_seen: int = betterproto.uint64_field(5)
    last_match_seen: int = betterproto.uint64_field(6)


@dataclass
class CMsgChatToxicityReport(betterproto.Message):
    num_matches_seen: int = betterproto.uint32_field(1)
    num_messages: int = betterproto.uint32_field(2)
    num_messages_ml_thinks_toxic: int = betterproto.uint32_field(4)
    status: str = betterproto.string_field(5)
    result: int = betterproto.uint32_field(6)
    message: str = betterproto.string_field(7)


@dataclass
class CMsgGetTeamAuditInformation(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)
    team_name: str = betterproto.string_field(2)
    actions: List["CMsgGetTeamAuditInformationAction"] = betterproto.message_field(3)
    last_updated: int = betterproto.uint32_field(4)


@dataclass
class CMsgGetTeamAuditInformationAction(betterproto.Message):
    registration_period: int = betterproto.uint32_field(1)
    account_id: int = betterproto.uint32_field(2)
    action: int = betterproto.uint32_field(3)
    timestamp: int = betterproto.uint32_field(4)
    player_name: str = betterproto.string_field(5)
    player_real_name: str = betterproto.string_field(6)


@dataclass
class CMsgDOTADPCMatch(betterproto.Message):
    match: "CMsgDOTAMatch" = betterproto.message_field(1)
    metadata: "CDOTAMatchMetadata" = betterproto.message_field(2)
