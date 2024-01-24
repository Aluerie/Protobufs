# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_player.steamworkssdk.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib


class ENotificationSetting(betterproto.Enum):
    k_ENotificationSettingNotifyUseDefault = 0
    k_ENotificationSettingAlways = 1
    k_ENotificationSettingNever = 2


@dataclass
class CPlayer_GetMutualFriendsForIncomingInvites_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_IncomingInviteMutualFriendList(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    mutual_friend_account_ids: List[int] = betterproto.uint32_field(2)


@dataclass
class CPlayer_GetMutualFriendsForIncomingInvites_Response(betterproto.Message):
    incoming_invite_mutual_friends_lists: List[
        "CPlayer_IncomingInviteMutualFriendList"
    ] = betterproto.message_field(1)


@dataclass
class CPlayer_GetFriendsGameplayInfo_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetFriendsGameplayInfo_Response(betterproto.Message):
    your_info: "CPlayer_GetFriendsGameplayInfo_ResponseOwnGameplayInfo" = (
        betterproto.message_field(1)
    )
    in_game: List[
        "CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"
    ] = betterproto.message_field(2)
    played_recently: List[
        "CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"
    ] = betterproto.message_field(3)
    played_ever: List[
        "CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"
    ] = betterproto.message_field(4)
    owns: List[
        "CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"
    ] = betterproto.message_field(5)
    in_wishlist: List[
        "CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"
    ] = betterproto.message_field(6)


@dataclass
class CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    minutes_played: int = betterproto.uint32_field(2)
    minutes_played_forever: int = betterproto.uint32_field(3)


@dataclass
class CPlayer_GetFriendsGameplayInfo_ResponseOwnGameplayInfo(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    minutes_played: int = betterproto.uint32_field(2)
    minutes_played_forever: int = betterproto.uint32_field(3)
    in_wishlist: bool = betterproto.bool_field(4)
    owned: bool = betterproto.bool_field(5)


@dataclass
class CPlayer_GetGameBadgeLevels_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetGameBadgeLevels_Response(betterproto.Message):
    player_level: int = betterproto.uint32_field(1)
    badges: List[
        "CPlayer_GetGameBadgeLevels_ResponseBadge"
    ] = betterproto.message_field(2)


@dataclass
class CPlayer_GetGameBadgeLevels_ResponseBadge(betterproto.Message):
    level: int = betterproto.int32_field(1)
    series: int = betterproto.int32_field(2)
    border_color: int = betterproto.uint32_field(3)


@dataclass
class CPlayer_GetLastPlayedTimes_Request(betterproto.Message):
    min_last_played: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetLastPlayedTimes_Response(betterproto.Message):
    games: List["CPlayer_GetLastPlayedTimes_ResponseGame"] = betterproto.message_field(
        1
    )


@dataclass
class CPlayer_GetLastPlayedTimes_ResponseGame(betterproto.Message):
    appid: int = betterproto.int32_field(1)
    last_playtime: int = betterproto.uint32_field(2)
    playtime_2weeks: int = betterproto.int32_field(3)
    playtime_forever: int = betterproto.int32_field(4)
    first_playtime: int = betterproto.uint32_field(5)


@dataclass
class CPlayer_AcceptSSA_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_AcceptSSA_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetNicknameList_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_GetNicknameList_Response(betterproto.Message):
    nicknames: List[
        "CPlayer_GetNicknameList_ResponsePlayerNickname"
    ] = betterproto.message_field(1)


@dataclass
class CPlayer_GetNicknameList_ResponsePlayerNickname(betterproto.Message):
    accountid: float = betterproto.fixed32_field(1)
    nickname: str = betterproto.string_field(2)


@dataclass
class CPlayer_GetPerFriendPreferences_Request(betterproto.Message):
    pass


@dataclass
class PerFriendPreferences(betterproto.Message):
    accountid: float = betterproto.fixed32_field(1)
    nickname: str = betterproto.string_field(2)
    notifications_showingame: "ENotificationSetting" = betterproto.enum_field(3)
    notifications_showonline: "ENotificationSetting" = betterproto.enum_field(4)
    notifications_showmessages: "ENotificationSetting" = betterproto.enum_field(5)
    sounds_showingame: "ENotificationSetting" = betterproto.enum_field(6)
    sounds_showonline: "ENotificationSetting" = betterproto.enum_field(7)
    sounds_showmessages: "ENotificationSetting" = betterproto.enum_field(8)
    notifications_sendmobile: "ENotificationSetting" = betterproto.enum_field(9)


@dataclass
class CPlayer_GetPerFriendPreferences_Response(betterproto.Message):
    preferences: List["PerFriendPreferences"] = betterproto.message_field(1)


@dataclass
class CPlayer_SetPerFriendPreferences_Request(betterproto.Message):
    preferences: "PerFriendPreferences" = betterproto.message_field(1)


@dataclass
class CPlayer_SetPerFriendPreferences_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_AddFriend_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CPlayer_AddFriend_Response(betterproto.Message):
    invite_sent: bool = betterproto.bool_field(1)
    friend_relationship: int = betterproto.uint32_field(2)


@dataclass
class CPlayer_RemoveFriend_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CPlayer_RemoveFriend_Response(betterproto.Message):
    friend_relationship: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_IgnoreFriend_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    unignore: bool = betterproto.bool_field(2)


@dataclass
class CPlayer_IgnoreFriend_Response(betterproto.Message):
    friend_relationship: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetCommunityPreferences_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_CommunityPreferences(betterproto.Message):
    hide_adult_content_violence: bool = betterproto.bool_field(1)
    hide_adult_content_sex: bool = betterproto.bool_field(2)
    parenthesize_nicknames: bool = betterproto.bool_field(4)
    timestamp_updated: int = betterproto.uint32_field(3)


@dataclass
class CPlayer_GetCommunityPreferences_Response(betterproto.Message):
    preferences: "CPlayer_CommunityPreferences" = betterproto.message_field(1)


@dataclass
class CPlayer_SetCommunityPreferences_Request(betterproto.Message):
    preferences: "CPlayer_CommunityPreferences" = betterproto.message_field(1)


@dataclass
class CPlayer_SetCommunityPreferences_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetNewSteamAnnouncementState_Request(betterproto.Message):
    language: int = betterproto.int32_field(1)


@dataclass
class CPlayer_GetNewSteamAnnouncementState_Response(betterproto.Message):
    state: int = betterproto.int32_field(1)
    announcement_headline: str = betterproto.string_field(2)
    announcement_url: str = betterproto.string_field(3)
    time_posted: int = betterproto.uint32_field(4)
    announcement_gid: int = betterproto.uint64_field(5)


@dataclass
class CPlayer_UpdateSteamAnnouncementLastRead_Request(betterproto.Message):
    announcement_gid: int = betterproto.uint64_field(1)
    time_posted: int = betterproto.uint32_field(2)


@dataclass
class CPlayer_UpdateSteamAnnouncementLastRead_Response(betterproto.Message):
    pass


class PlayerStub(betterproto.ServiceStub):
    async def get_mutual_friends_for_incoming_invites(
        self,
    ) -> CPlayer_GetMutualFriendsForIncomingInvites_Response:
        request = CPlayer_GetMutualFriendsForIncomingInvites_Request()

        return await self._unary_unary(
            "/.Player/GetMutualFriendsForIncomingInvites",
            request,
            CPlayer_GetMutualFriendsForIncomingInvites_Response,
        )

    async def get_friends_gameplay_info(
        self, *, appid: int = 0
    ) -> CPlayer_GetFriendsGameplayInfo_Response:
        request = CPlayer_GetFriendsGameplayInfo_Request()
        request.appid = appid

        return await self._unary_unary(
            "/.Player/GetFriendsGameplayInfo",
            request,
            CPlayer_GetFriendsGameplayInfo_Response,
        )

    async def get_game_badge_levels(
        self, *, appid: int = 0
    ) -> CPlayer_GetGameBadgeLevels_Response:
        request = CPlayer_GetGameBadgeLevels_Request()
        request.appid = appid

        return await self._unary_unary(
            "/.Player/GetGameBadgeLevels",
            request,
            CPlayer_GetGameBadgeLevels_Response,
        )

    async def client_get_last_played_times(
        self, *, min_last_played: int = 0
    ) -> CPlayer_GetLastPlayedTimes_Response:
        request = CPlayer_GetLastPlayedTimes_Request()
        request.min_last_played = min_last_played

        return await self._unary_unary(
            "/.Player/ClientGetLastPlayedTimes",
            request,
            CPlayer_GetLastPlayedTimes_Response,
        )

    async def accept_s_s_a(self) -> CPlayer_AcceptSSA_Response:
        request = CPlayer_AcceptSSA_Request()

        return await self._unary_unary(
            "/.Player/AcceptSSA",
            request,
            CPlayer_AcceptSSA_Response,
        )

    async def get_nickname_list(self) -> CPlayer_GetNicknameList_Response:
        request = CPlayer_GetNicknameList_Request()

        return await self._unary_unary(
            "/.Player/GetNicknameList",
            request,
            CPlayer_GetNicknameList_Response,
        )

    async def get_per_friend_preferences(
        self,
    ) -> CPlayer_GetPerFriendPreferences_Response:
        request = CPlayer_GetPerFriendPreferences_Request()

        return await self._unary_unary(
            "/.Player/GetPerFriendPreferences",
            request,
            CPlayer_GetPerFriendPreferences_Response,
        )

    async def set_per_friend_preferences(
        self, *, preferences: Optional["PerFriendPreferences"] = None
    ) -> CPlayer_SetPerFriendPreferences_Response:
        request = CPlayer_SetPerFriendPreferences_Request()
        if preferences is not None:
            request.preferences = preferences

        return await self._unary_unary(
            "/.Player/SetPerFriendPreferences",
            request,
            CPlayer_SetPerFriendPreferences_Response,
        )

    async def add_friend(self, *, steamid: float = 0) -> CPlayer_AddFriend_Response:
        request = CPlayer_AddFriend_Request()
        request.steamid = steamid

        return await self._unary_unary(
            "/.Player/AddFriend",
            request,
            CPlayer_AddFriend_Response,
        )

    async def remove_friend(
        self, *, steamid: float = 0
    ) -> CPlayer_RemoveFriend_Response:
        request = CPlayer_RemoveFriend_Request()
        request.steamid = steamid

        return await self._unary_unary(
            "/.Player/RemoveFriend",
            request,
            CPlayer_RemoveFriend_Response,
        )

    async def ignore_friend(
        self, *, steamid: float = 0, unignore: bool = False
    ) -> CPlayer_IgnoreFriend_Response:
        request = CPlayer_IgnoreFriend_Request()
        request.steamid = steamid
        request.unignore = unignore

        return await self._unary_unary(
            "/.Player/IgnoreFriend",
            request,
            CPlayer_IgnoreFriend_Response,
        )

    async def get_community_preferences(
        self,
    ) -> CPlayer_GetCommunityPreferences_Response:
        request = CPlayer_GetCommunityPreferences_Request()

        return await self._unary_unary(
            "/.Player/GetCommunityPreferences",
            request,
            CPlayer_GetCommunityPreferences_Response,
        )

    async def set_community_preferences(
        self, *, preferences: Optional["CPlayer_CommunityPreferences"] = None
    ) -> CPlayer_SetCommunityPreferences_Response:
        request = CPlayer_SetCommunityPreferences_Request()
        if preferences is not None:
            request.preferences = preferences

        return await self._unary_unary(
            "/.Player/SetCommunityPreferences",
            request,
            CPlayer_SetCommunityPreferences_Response,
        )

    async def get_new_steam_announcement_state(
        self, *, language: int = 0
    ) -> CPlayer_GetNewSteamAnnouncementState_Response:
        request = CPlayer_GetNewSteamAnnouncementState_Request()
        request.language = language

        return await self._unary_unary(
            "/.Player/GetNewSteamAnnouncementState",
            request,
            CPlayer_GetNewSteamAnnouncementState_Response,
        )

    async def update_steam_announcement_last_read(
        self, *, announcement_gid: int = 0, time_posted: int = 0
    ) -> CPlayer_UpdateSteamAnnouncementLastRead_Response:
        request = CPlayer_UpdateSteamAnnouncementLastRead_Request()
        request.announcement_gid = announcement_gid
        request.time_posted = time_posted

        return await self._unary_unary(
            "/.Player/UpdateSteamAnnouncementLastRead",
            request,
            CPlayer_UpdateSteamAnnouncementLastRead_Response,
        )
