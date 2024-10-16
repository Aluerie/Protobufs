# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_gamenetworkingui.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CGameNetworkingUI_GlobalState(betterproto.Message):
    pass


@dataclass
class CGameNetworkingUI_ConnectionState(betterproto.Message):
    connection_key: str = betterproto.string_field(1)
    appid: int = betterproto.uint32_field(2)
    connection_id_local: float = betterproto.fixed32_field(3)
    identity_local: str = betterproto.string_field(4)
    identity_remote: str = betterproto.string_field(5)
    connection_state: int = betterproto.uint32_field(10)
    start_time: int = betterproto.uint32_field(12)
    close_time: int = betterproto.uint32_field(13)
    close_reason: int = betterproto.uint32_field(14)
    close_message: str = betterproto.string_field(15)
    status_loc_token: str = betterproto.string_field(16)
    transport_kind: int = betterproto.uint32_field(20)
    sdrpopid_local: str = betterproto.string_field(21)
    sdrpopid_remote: str = betterproto.string_field(22)
    address_remote: str = betterproto.string_field(23)
    p2p_routing: "CMsgSteamDatagramP2PRoutingSummary" = betterproto.message_field(24)
    ping_interior: int = betterproto.uint32_field(25)
    ping_remote_front: int = betterproto.uint32_field(26)
    ping_default_internet_route: int = betterproto.uint32_field(27)
    e2e_quality_local: "CMsgSteamDatagramConnectionQuality" = betterproto.message_field(
        30
    )
    e2e_quality_remote: "CMsgSteamDatagramConnectionQuality" = (
        betterproto.message_field(31)
    )
    e2e_quality_remote_instantaneous_time: int = betterproto.uint64_field(32)
    e2e_quality_remote_lifetime_time: int = betterproto.uint64_field(33)
    front_quality_local: "CMsgSteamDatagramConnectionQuality" = (
        betterproto.message_field(40)
    )
    front_quality_remote: "CMsgSteamDatagramConnectionQuality" = (
        betterproto.message_field(41)
    )
    front_quality_remote_instantaneous_time: int = betterproto.uint64_field(42)
    front_quality_remote_lifetime_time: int = betterproto.uint64_field(43)


@dataclass
class CGameNetworkingUI_Message(betterproto.Message):
    connection_state: List[
        "CGameNetworkingUI_ConnectionState"
    ] = betterproto.message_field(1)


@dataclass
class CGameNetworkingUI_ConnectionSummary(betterproto.Message):
    transport_kind: int = betterproto.uint32_field(1)
    connection_state: int = betterproto.uint32_field(8)
    sdrpop_local: str = betterproto.string_field(2)
    sdrpop_remote: str = betterproto.string_field(3)
    ping_ms: int = betterproto.uint32_field(4)
    packet_loss: float = betterproto.float_field(5)
    ping_default_internet_route: int = betterproto.uint32_field(6)
    ip_was_shared: bool = betterproto.bool_field(7)


@dataclass
class CGameNetworkingUI_AppSummary(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    ip_was_shared_with_friend: bool = betterproto.bool_field(10)
    ip_was_shared_with_nonfriend: bool = betterproto.bool_field(11)
    active_connections: int = betterproto.uint32_field(20)
    main_cxn: "CGameNetworkingUI_ConnectionSummary" = betterproto.message_field(30)
