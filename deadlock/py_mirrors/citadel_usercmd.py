# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: citadel_usercmd.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class CCitadelUserCmdPB(betterproto.Message):
    base: "CBaseUserCmdPB" = betterproto.message_field(1)
    vec_camera_position: "CMsgVector" = betterproto.message_field(2)
    ang_camera_angles: "CMsgQAngle" = betterproto.message_field(3)
    execute_ability_indices: int = betterproto.int32_field(4)
    in_shop: bool = betterproto.bool_field(5)
    camera_roaming_speed: float = betterproto.float_field(6)
    using_free_cursor: bool = betterproto.bool_field(8)
    enemy_hero_aimed_at: int = betterproto.int32_field(10)
