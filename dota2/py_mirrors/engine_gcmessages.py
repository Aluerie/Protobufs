# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: engine_gcmessages.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class CEngineGotvSyncPacket(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)
    instance_id: int = betterproto.uint32_field(2)
    signupfragment: int = betterproto.uint32_field(3)
    currentfragment: int = betterproto.uint32_field(4)
    tickrate: float = betterproto.float_field(5)
    tick: int = betterproto.uint32_field(6)
    rtdelay: float = betterproto.float_field(8)
    rcvage: float = betterproto.float_field(9)
    keyframe_interval: float = betterproto.float_field(10)
    cdndelay: int = betterproto.uint32_field(11)
