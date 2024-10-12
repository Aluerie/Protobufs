# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: citadel_clientmessages.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class ECitadelClientMessages(betterproto.Enum):
    CITADEL_CM_MapPing = 1002
    CITADEL_CM_PerformanceStats = 1003
    CITADEL_CM_PingWheel = 1004
    CITADEL_CM_ChatMsg = 1005
    CITADEL_CM_PerfReport = 1006
    CITADEL_CM_QuickResponse = 1007
    CITADEL_CM_Pause = 1008
    CITADEL_CM_MapLine = 1009
    CITADEL_CM_AbilityPing = 1010
    CITADEL_CM_ExecuteMapUnitAbility = 1011
    CITADEL_CM_GetDamageStats = 1012
    CITADEL_CM_CheaterVote = 1013


@dataclass
class CCitadelClientMsg_Pause(betterproto.Message):
    pass


@dataclass
class CCitadelClientMsg_MapPing(betterproto.Message):
    ping_location: "CMsgVector" = betterproto.message_field(1)
    event_type: int = betterproto.int32_field(2)
    entity_index: int = betterproto.int32_field(3)
    is_aggressive_ping: bool = betterproto.bool_field(4)
    is_minimap_ping: bool = betterproto.bool_field(5)
    is_blind_ping: bool = betterproto.bool_field(6)


@dataclass
class CCitadelClientMsg_PingWheel(betterproto.Message):
    ping_wheel_option_id: int = betterproto.uint32_field(1)
    subnav_message_id: int = betterproto.uint32_field(2)
    ping_location: "CMsgVector" = betterproto.message_field(3)
    entity_index: int = betterproto.int32_field(4)


@dataclass
class CCitadelClientMsg_AbilityPing(betterproto.Message):
    entity_index: int = betterproto.int32_field(1)
    pinged_ability_id: int = betterproto.uint32_field(2)
    pinged_player_slot: int = betterproto.int32_field(3)


@dataclass
class CCitadelClientMsg_MapLine(betterproto.Message):
    mapline: "CMsgMapLine" = betterproto.message_field(1)


@dataclass
class CCitadelClientMsg_QuickResponse(betterproto.Message):
    ping_wheel_message_id: int = betterproto.uint32_field(1)
    responding_to_ping_message_id: int = betterproto.uint32_field(2)
    responding_to_player_slot: int = betterproto.int32_field(3)


@dataclass
class CCitadelClientMsg_PerformanceStats(betterproto.Message):
    current_game_time: float = betterproto.float_field(1)
    average_fps: float = betterproto.float_field(2)
    min_fps: float = betterproto.float_field(3)
    max_fps: float = betterproto.float_field(4)


@dataclass
class CCitadelClientMsg_ChatMsg(betterproto.Message):
    chat_text: str = betterproto.string_field(1)
    all_chat: bool = betterproto.bool_field(2)
    lane_color: "CMsgLaneColor" = betterproto.enum_field(3)


@dataclass
class CCitadelClientMsg_PerfReport(betterproto.Message):
    average_frame_time: float = betterproto.float_field(1)
    max_frame_time: float = betterproto.float_field(2)
    average_compute_time: float = betterproto.float_field(3)
    max_compute_time: float = betterproto.float_field(4)
    average_client_tick_time: float = betterproto.float_field(5)
    max_client_tick_time: float = betterproto.float_field(6)
    average_client_simulate_time: float = betterproto.float_field(7)
    max_client_simulate_time: float = betterproto.float_field(8)
    average_output_time: float = betterproto.float_field(9)
    max_output_time: float = betterproto.float_field(10)
    average_wait_for_rendering_to_complete_time: float = betterproto.float_field(11)
    max_wait_for_rendering_to_complete_time: float = betterproto.float_field(12)
    average_swap_time: float = betterproto.float_field(13)
    max_swap_time: float = betterproto.float_field(14)
    average_frame_update_time: float = betterproto.float_field(15)
    max_frame_update_time: float = betterproto.float_field(16)
    average_idle_time: float = betterproto.float_field(17)
    max_idle_time: float = betterproto.float_field(18)
    average_input_processing_time: float = betterproto.float_field(19)
    max_input_processing_time: float = betterproto.float_field(20)


@dataclass
class CCitadelClientMsg_GetDamageStats(betterproto.Message):
    lobby_player_slot: int = betterproto.uint32_field(1)
    ability_name: str = betterproto.string_field(2)


@dataclass
class CCitadelClientCachedPlayerStats(betterproto.Message):
    version: int = betterproto.uint32_field(1)
    stats: List["CCitadelClientCachedPlayerStatsStat"] = betterproto.message_field(2)


@dataclass
class CCitadelClientCachedPlayerStatsStat(betterproto.Message):
    stat_name: str = betterproto.string_field(1)
    all_time_total: int = betterproto.uint64_field(2)
    all_time_match_max: int = betterproto.uint32_field(3)
    all_time_life_max: int = betterproto.uint32_field(4)


@dataclass
class CCitadelClientMsg_ExecuteMapUnitAbility(betterproto.Message):
    ability_entity_index: int = betterproto.int32_field(1)
    target_entity_index: int = betterproto.int32_field(2)


@dataclass
class CCitadelClientMsg_CheaterVote(betterproto.Message):
    end_game_immediately: bool = betterproto.bool_field(1)
