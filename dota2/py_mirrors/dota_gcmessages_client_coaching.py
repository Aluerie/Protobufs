# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_client_coaching.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class ECoachTeammateRating(betterproto.Enum):
    k_ECoachTeammateRating_None = 0
    k_ECoachTeammateRating_Positive = 1
    k_ECoachTeammateRating_Negative = 2
    k_ECoachTeammateRating_Abusive = 3


class EPrivateCoachingSessionState(betterproto.Enum):
    k_ePrivateCoachingSessionState_Invalid = 0
    k_ePrivateCoachingSessionState_SearchingForCoach = 1
    k_ePrivateCoachingSessionState_CoachAssigned = 2
    k_ePrivateCoachingSessionState_Finished = 3
    k_ePrivateCoachingSessionState_Expired = 4
    k_ePrivateCoachingSessionState_Abandoned = 5


class EPrivateCoachingSessionMemberFlag(betterproto.Enum):
    k_EPrivateCoachingSessionMemberFlag_Requester = 1
    k_EPrivateCoachingSessionMemberFlag_Coach = 2
    k_EPrivateCoachingSessionMemberFlag_LeftSession = 4


class EPlayerCoachMatchFlag(betterproto.Enum):
    k_EPlayerCoachMatchFlag_EligibleForRewards = 1
    k_EPlayerCoachMatchFlag_PrivateCoach = 2


class CMsgClientToGCRequestPlayerCoachMatchesResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3


class CMsgClientToGCRequestPlayerCoachMatchResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3


class CMsgClientToGCSubmitCoachTeammateRatingResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eInvalidInput = 4
    k_eAlreadySubmitted = 5
    k_eVotingFinished = 6
    k_ePlayerNotInMatch = 7
    k_eCoachNotInMatch = 8
    k_ePlayerNotOnCoachTeam = 9
    k_ePlayerInSamePartyAsCoach = 10
    k_eMatchNotEligible = 11


class CMsgClientToGCRequestPrivateCoachingSessionResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eAlreadyInSession = 5
    k_eBehaviorScoreTooLow = 6
    k_eInvalidLobbyType = 7
    k_eLowPriorityPlayer = 8
    k_eLowPriorityLobby = 9
    k_eLowPriorityParty = 10
    k_eTextChatBan = 11
    k_eVoiceChatBan = 12
    k_eMatchBan = 13


class CMsgClientToGCAcceptPrivateCoachingSessionResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eUnknownSession = 5
    k_eAlreadyHasCoach = 6
    k_eAlreadyHasSession = 7
    k_eInvalidUser = 8
    k_eAlreadyFinished = 9
    k_eInvalidLobbyType = 10
    k_eAlreadyInLobby = 11
    k_eLobbyIsLan = 12
    k_eLobbyIsLeague = 13
    k_eInvalidLobbyState = 14
    k_eRequesterIsNotPlayer = 15
    k_eTooManyCoaches = 16
    k_eCoachWasPlayer = 17
    k_eCoachBehaviorScoreTooLow = 18
    k_eCoachRankNotCalibrated = 19
    k_eCoachRankNotEligible = 20
    k_eCoachRankTooLow = 21


class CMsgClientToGCLeavePrivateCoachingSessionResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eNoSession = 5
    k_eAlreadyLeft = 6


class CMsgClientToGCGetCurrentPrivateCoachingSessionResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4


class CMsgClientToGCSubmitPrivateCoachingSessionRatingResponseEResponse(
    betterproto.Enum
):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eUnknownSession = 5
    k_eNotMember = 6
    k_eAlreadySubmitted = 7
    k_eSessionActive = 8
    k_eSessionTooShort = 9
    k_eNoCoach = 10
    k_eInvalidRating = 11


class CMsgClientToGCGetAvailablePrivateCoachingSessionsResponseEResponse(
    betterproto.Enum
):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4


class CMsgClientToGCGetAvailablePrivateCoachingSessionsSummaryResponseEResponse(
    betterproto.Enum
):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4


class CMsgClientToGCJoinPrivateCoachingSessionLobbyResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eNoSession = 5
    k_eSessionFinished = 6
    k_eAlreadyLeft = 7
    k_eNotACoach = 8
    k_eNoLobby = 9
    k_eCoachInThisLobby = 10
    k_eCoachInALobby = 11
    k_eLobbyIsLan = 12
    k_eLobbyIsLeague = 13
    k_eInvalidLobbyType = 14
    k_eInvalidLobbyState = 15
    k_eRequesterIsNotPlayer = 16
    k_eTooManyCoaches = 17
    k_eCoachWasPlayer = 18
    k_eJoinFailed = 19


class CMsgClientToGCCoachFriendResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eCoachNotSubscriber = 5
    k_eLobbyNotFound = 6
    k_eFriendsOnBothSides = 7
    k_eNotFriends = 8
    k_eCoachInThisLobby = 9
    k_eCoachInALobby = 10
    k_eLobbyIsLan = 11
    k_eInvalidLobbyType = 12
    k_eInvalidLobbyState = 13
    k_eFriendIsNotAPlayer = 14
    k_eTooManyCoaches = 15
    k_eCoachSwitchedTeams = 16
    k_eLobbyIsLeague = 17
    k_eCoachWasPlayer = 18
    k_eRequestRejected = 19


class CMsgClientToGCRespondToCoachFriendRequestResponseEResponse(betterproto.Enum):
    k_eInternalError = 0
    k_eSuccess = 1
    k_eTooBusy = 2
    k_eDisabled = 3
    k_eTimeout = 4
    k_eLobbyNotFound = 5
    k_eInvalidLobbyState = 6
    k_eCoachNotInLobby = 7
    k_ePlayerInvalidTeam = 8
    k_eCoachInvalidTeam = 9
    k_eNoRequest = 10
    k_eInvalidResponse = 11
    k_eAlreadyResponded = 12


@dataclass
class CMsgPlayerCoachMatch(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)
    match_outcome: "EMatchOutcome" = betterproto.enum_field(2)
    coached_team: int = betterproto.uint32_field(3)
    start_time: float = betterproto.fixed32_field(4)
    duration: int = betterproto.uint32_field(5)
    teammate_ratings: List["ECoachTeammateRating"] = betterproto.enum_field(6)
    coach_flags: int = betterproto.uint32_field(7)


@dataclass
class CMsgPrivateCoachingSessionMember(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    member_flags: int = betterproto.uint32_field(2)
    member_session_rating: "ECoachTeammateRating" = betterproto.enum_field(3)


@dataclass
class CMsgPrivateCoachingSession(betterproto.Message):
    private_coaching_session_id: int = betterproto.uint64_field(1)
    requested_timestamp: float = betterproto.fixed32_field(2)
    requested_language: int = betterproto.uint32_field(3)
    coaching_session_state: "EPrivateCoachingSessionState" = betterproto.enum_field(4)
    session_members: List[
        "CMsgPrivateCoachingSessionMember"
    ] = betterproto.message_field(5)
    current_lobby_id: int = betterproto.uint64_field(6)
    current_server_steam_id: int = betterproto.uint64_field(7)
    accepted_timestamp: float = betterproto.fixed32_field(8)
    completed_timestamp: float = betterproto.fixed32_field(9)


@dataclass
class CMsgPrivateCoachingSessionStatus(betterproto.Message):
    requester_competitive_rank_tier: int = betterproto.uint32_field(1)
    requester_games_played: int = betterproto.uint32_field(2)


@dataclass
class CMsgAvailablePrivateCoachingSession(betterproto.Message):
    coaching_session: "CMsgPrivateCoachingSession" = betterproto.message_field(1)
    coaching_session_status: "CMsgPrivateCoachingSessionStatus" = (
        betterproto.message_field(2)
    )


@dataclass
class CMsgAvailablePrivateCoachingSessionList(betterproto.Message):
    available_coaching_sessions: List[
        "CMsgAvailablePrivateCoachingSession"
    ] = betterproto.message_field(1)


@dataclass
class CMsgAvailablePrivateCoachingSessionSummary(betterproto.Message):
    coaching_session_count: int = betterproto.uint32_field(1)


@dataclass
class CMsgClientToGCRequestPlayerCoachMatches(betterproto.Message):
    pass


@dataclass
class CMsgClientToGCRequestPlayerCoachMatchesResponse(betterproto.Message):
    result: "CMsgClientToGCRequestPlayerCoachMatchesResponseEResponse" = (
        betterproto.enum_field(1)
    )
    coach_matches: List["CMsgPlayerCoachMatch"] = betterproto.message_field(2)


@dataclass
class CMsgClientToGCRequestPlayerCoachMatch(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)


@dataclass
class CMsgClientToGCRequestPlayerCoachMatchResponse(betterproto.Message):
    result: "CMsgClientToGCRequestPlayerCoachMatchResponseEResponse" = (
        betterproto.enum_field(1)
    )
    coach_match: "CMsgPlayerCoachMatch" = betterproto.message_field(2)


@dataclass
class CMsgClientToGCSubmitCoachTeammateRating(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)
    coach_account_id: int = betterproto.uint32_field(2)
    rating: "ECoachTeammateRating" = betterproto.enum_field(3)
    reason: str = betterproto.string_field(4)


@dataclass
class CMsgClientToGCSubmitCoachTeammateRatingResponse(betterproto.Message):
    result: "CMsgClientToGCSubmitCoachTeammateRatingResponseEResponse" = (
        betterproto.enum_field(1)
    )


@dataclass
class CMsgGCToClientCoachTeammateRatingsChanged(betterproto.Message):
    coach_match: "CMsgPlayerCoachMatch" = betterproto.message_field(1)


@dataclass
class CMsgClientToGCRequestPrivateCoachingSession(betterproto.Message):
    language: int = betterproto.uint32_field(1)


@dataclass
class CMsgClientToGCRequestPrivateCoachingSessionResponse(betterproto.Message):
    result: "CMsgClientToGCRequestPrivateCoachingSessionResponseEResponse" = (
        betterproto.enum_field(1)
    )
    coaching_session: "CMsgPrivateCoachingSession" = betterproto.message_field(2)


@dataclass
class CMsgClientToGCAcceptPrivateCoachingSession(betterproto.Message):
    coaching_session_id: int = betterproto.uint64_field(1)


@dataclass
class CMsgClientToGCAcceptPrivateCoachingSessionResponse(betterproto.Message):
    result: "CMsgClientToGCAcceptPrivateCoachingSessionResponseEResponse" = (
        betterproto.enum_field(1)
    )
    coaching_session: "CMsgPrivateCoachingSession" = betterproto.message_field(2)


@dataclass
class CMsgClientToGCLeavePrivateCoachingSession(betterproto.Message):
    pass


@dataclass
class CMsgClientToGCLeavePrivateCoachingSessionResponse(betterproto.Message):
    result: "CMsgClientToGCLeavePrivateCoachingSessionResponseEResponse" = (
        betterproto.enum_field(1)
    )


@dataclass
class CMsgClientToGCGetCurrentPrivateCoachingSession(betterproto.Message):
    pass


@dataclass
class CMsgClientToGCGetCurrentPrivateCoachingSessionResponse(betterproto.Message):
    result: "CMsgClientToGCGetCurrentPrivateCoachingSessionResponseEResponse" = (
        betterproto.enum_field(1)
    )
    current_session: "CMsgPrivateCoachingSession" = betterproto.message_field(2)


@dataclass
class CMsgGCToClientPrivateCoachingSessionUpdated(betterproto.Message):
    coaching_session: "CMsgPrivateCoachingSession" = betterproto.message_field(1)


@dataclass
class CMsgClientToGCSubmitPrivateCoachingSessionRating(betterproto.Message):
    coaching_session_id: int = betterproto.uint64_field(1)
    session_rating: "ECoachTeammateRating" = betterproto.enum_field(2)


@dataclass
class CMsgClientToGCSubmitPrivateCoachingSessionRatingResponse(betterproto.Message):
    result: "CMsgClientToGCSubmitPrivateCoachingSessionRatingResponseEResponse" = (
        betterproto.enum_field(1)
    )


@dataclass
class CMsgClientToGCGetAvailablePrivateCoachingSessions(betterproto.Message):
    language: int = betterproto.uint32_field(1)


@dataclass
class CMsgClientToGCGetAvailablePrivateCoachingSessionsResponse(betterproto.Message):
    result: "CMsgClientToGCGetAvailablePrivateCoachingSessionsResponseEResponse" = (
        betterproto.enum_field(1)
    )
    available_sessions_list: "CMsgAvailablePrivateCoachingSessionList" = (
        betterproto.message_field(2)
    )


@dataclass
class CMsgClientToGCGetAvailablePrivateCoachingSessionsSummary(betterproto.Message):
    pass


@dataclass
class CMsgClientToGCGetAvailablePrivateCoachingSessionsSummaryResponse(
    betterproto.Message
):
    result: "CMsgClientToGCGetAvailablePrivateCoachingSessionsSummaryResponseEResponse" = betterproto.enum_field(
        1
    )
    coaching_session_summary: "CMsgAvailablePrivateCoachingSessionSummary" = (
        betterproto.message_field(2)
    )


@dataclass
class CMsgClientToGCJoinPrivateCoachingSessionLobby(betterproto.Message):
    pass


@dataclass
class CMsgClientToGCJoinPrivateCoachingSessionLobbyResponse(betterproto.Message):
    result: "CMsgClientToGCJoinPrivateCoachingSessionLobbyResponseEResponse" = (
        betterproto.enum_field(1)
    )


@dataclass
class CMsgClientToGCCoachFriend(betterproto.Message):
    target_account_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgClientToGCCoachFriendResponse(betterproto.Message):
    result: "CMsgClientToGCCoachFriendResponseEResponse" = betterproto.enum_field(1)


@dataclass
class CMsgClientToGCRespondToCoachFriendRequest(betterproto.Message):
    coach_account_id: int = betterproto.uint32_field(1)
    response: "ELobbyMemberCoachRequestState" = betterproto.enum_field(2)


@dataclass
class CMsgClientToGCRespondToCoachFriendRequestResponse(betterproto.Message):
    result: "CMsgClientToGCRespondToCoachFriendRequestResponseEResponse" = (
        betterproto.enum_field(1)
    )
