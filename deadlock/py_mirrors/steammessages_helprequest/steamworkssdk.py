# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_helprequest.steamworkssdk.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
import grpclib


@dataclass
class CHelpRequestLogs_UploadUserApplicationLog_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    log_type: str = betterproto.string_field(2)
    version_string: str = betterproto.string_field(3)
    log_contents: str = betterproto.string_field(4)


@dataclass
class CHelpRequestLogs_UploadUserApplicationLog_Response(betterproto.Message):
    id: int = betterproto.uint64_field(1)


class HelpRequestLogsStub(betterproto.ServiceStub):
    async def upload_user_application_log(
        self,
        *,
        appid: int = 0,
        log_type: str = "",
        version_string: str = "",
        log_contents: str = "",
    ) -> CHelpRequestLogs_UploadUserApplicationLog_Response:
        request = CHelpRequestLogs_UploadUserApplicationLog_Request()
        request.appid = appid
        request.log_type = log_type
        request.version_string = version_string
        request.log_contents = log_contents

        return await self._unary_unary(
            "/.HelpRequestLogs/UploadUserApplicationLog",
            request,
            CHelpRequestLogs_UploadUserApplicationLog_Response,
        )
