# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_client_bingo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class EBingoAuditAction(betterproto.Enum):
    k_eBingoAuditAction_Invalid = 0
    k_eBingoAuditAction_DevModifyTokens = 1
    k_eBingoAuditAction_DevClearInventory = 2
    k_eBingoAuditAction_DevRerollCard = 3
    k_eBingoAuditAction_ShuffleCard = 4
    k_eBingoAuditAction_RerollSquare = 5
    k_eBingoAuditAction_UpgradeSquare = 6
    k_eBingoAuditAction_ClaimRow = 7
    k_eBingoAuditAction_EventActionTokenGrant = 8
    k_eBingoAuditAction_SupportGrantTokens = 9
    k_eBingoAuditAction_SupportStatThresholdFixup = 10


class CMsgClientToGCBingoGetUserDataResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4


class CMsgClientToGCBingoGetStatsDataResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4


class CMsgClientToGCBingoClaimRowResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eInvalidRow = 5
    k_eExpiredCard = 6


class CMsgClientToGCBingoShuffleCardResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eExpiredCard = 6
    k_eNotAllowed = 7
    k_eInsufficientTokens = 8


class CMsgClientToGCBingoModifySquareEModifyAction(betterproto.Enum):
    k_eRerollStat = 0
    k_eUpgrade = 1


class CMsgClientToGCBingoModifySquareResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eExpiredCard = 6
    k_eNotAllowed = 7
    k_eInsufficientTokens = 8
    k_eCantUpgrade = 9
    k_eCantReroll = 10
    k_eInvalidSquare = 11


class CMsgClientToGCBingoDevRerollCardResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eExpiredCard = 6
    k_eNotAllowed = 7


class CMsgClientToGCBingoDevAddTokensResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eExpiredCard = 6
    k_eNotAllowed = 7


class CMsgClientToGCBingoDevClearInventoryResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eExpiredCard = 6
    k_eNotAllowed = 7


@dataclass
class CMsgBingoSquare(betterproto.Message):
    stat_id: int = betterproto.uint32_field(1)
    stat_threshold: int = betterproto.int32_field(2)
    upgrade_level: int = betterproto.uint32_field(3)


@dataclass
class CMsgBingoTokens(betterproto.Message):
    token_count: int = betterproto.uint32_field(1)


@dataclass
class CMsgBingoCard(betterproto.Message):
    squares: List["CMsgBingoSquare"] = betterproto.message_field(1)


@dataclass
class CMsgBingoUserData(betterproto.Message):
    bingo_cards: List["CMsgBingoUserDataBingoCardsEntry"] = betterproto.message_field(1)
    bingo_tokens: List["CMsgBingoUserDataBingoTokensEntry"] = betterproto.message_field(
        2
    )


@dataclass
class CMsgBingoUserDataBingoCardsEntry(betterproto.Message):
    key: int = betterproto.uint32_field(1)
    value: "CMsgBingoCard" = betterproto.message_field(2)


@dataclass
class CMsgBingoUserDataBingoTokensEntry(betterproto.Message):
    key: int = betterproto.uint32_field(1)
    value: "CMsgBingoTokens" = betterproto.message_field(2)


@dataclass
class CMsgClientToGCBingoGetUserData(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgClientToGCBingoGetUserDataResponse(betterproto.Message):
    response: "CMsgClientToGCBingoGetUserDataResponseEResponse" = (
        betterproto.enum_field(1)
    )
    user_data: "CMsgBingoUserData" = betterproto.message_field(2)


@dataclass
class CMsgBingoIndividualStatData(betterproto.Message):
    stat_id: int = betterproto.uint32_field(1)
    stat_value: int = betterproto.int32_field(2)


@dataclass
class CMsgBingoStatsData(betterproto.Message):
    stats_data: List["CMsgBingoIndividualStatData"] = betterproto.message_field(1)


@dataclass
class CMsgClientToGCBingoGetStatsData(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    league_phase: int = betterproto.uint32_field(2)


@dataclass
class CMsgClientToGCBingoGetStatsDataResponse(betterproto.Message):
    response: "CMsgClientToGCBingoGetStatsDataResponseEResponse" = (
        betterproto.enum_field(1)
    )
    stats_data: "CMsgBingoStatsData" = betterproto.message_field(2)


@dataclass
class CMsgGCToClientBingoUserDataUpdated(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    user_data: "CMsgBingoUserData" = betterproto.message_field(2)


@dataclass
class CMsgClientToGCBingoClaimRow(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    league_phase: int = betterproto.uint32_field(2)
    row_index: int = betterproto.uint32_field(3)


@dataclass
class CMsgClientToGCBingoClaimRowResponse(betterproto.Message):
    response: "CMsgClientToGCBingoClaimRowResponseEResponse" = betterproto.enum_field(1)


@dataclass
class CMsgClientToGCBingoShuffleCard(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    league_phase: int = betterproto.uint32_field(2)


@dataclass
class CMsgClientToGCBingoShuffleCardResponse(betterproto.Message):
    response: "CMsgClientToGCBingoShuffleCardResponseEResponse" = (
        betterproto.enum_field(1)
    )


@dataclass
class CMsgClientToGCBingoModifySquare(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    league_phase: int = betterproto.uint32_field(2)
    square_index: int = betterproto.uint32_field(3)
    action: "CMsgClientToGCBingoModifySquareEModifyAction" = betterproto.enum_field(4)


@dataclass
class CMsgClientToGCBingoModifySquareResponse(betterproto.Message):
    response: "CMsgClientToGCBingoModifySquareResponseEResponse" = (
        betterproto.enum_field(1)
    )


@dataclass
class CMsgClientToGCBingoDevRerollCard(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    league_phase: int = betterproto.uint32_field(2)


@dataclass
class CMsgClientToGCBingoDevRerollCardResponse(betterproto.Message):
    response: "CMsgClientToGCBingoDevRerollCardResponseEResponse" = (
        betterproto.enum_field(1)
    )


@dataclass
class CMsgClientToGCBingoDevAddTokens(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    league_phase: int = betterproto.uint32_field(2)
    token_count: int = betterproto.int32_field(3)


@dataclass
class CMsgClientToGCBingoDevAddTokensResponse(betterproto.Message):
    response: "CMsgClientToGCBingoDevAddTokensResponseEResponse" = (
        betterproto.enum_field(1)
    )


@dataclass
class CMsgClientToGCBingoDevClearInventory(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgClientToGCBingoDevClearInventoryResponse(betterproto.Message):
    response: "CMsgClientToGCBingoDevClearInventoryResponseEResponse" = (
        betterproto.enum_field(1)
    )
