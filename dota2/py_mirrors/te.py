# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: te.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class ETEProtobufIds(betterproto.Enum):
    TE_EffectDispatchId = 400
    TE_ArmorRicochetId = 401
    TE_BeamEntPointId = 402
    TE_BeamEntsId = 403
    TE_BeamPointsId = 404
    TE_BeamRingId = 405
    TE_BSPDecalId = 407
    TE_BubblesId = 408
    TE_BubbleTrailId = 409
    TE_DecalId = 410
    TE_WorldDecalId = 411
    TE_EnergySplashId = 412
    TE_FizzId = 413
    TE_ShatterSurfaceId = 414
    TE_GlowSpriteId = 415
    TE_ImpactId = 416
    TE_MuzzleFlashId = 417
    TE_BloodStreamId = 418
    TE_ExplosionId = 419
    TE_DustId = 420
    TE_LargeFunnelId = 421
    TE_SparksId = 422
    TE_PhysicsPropId = 423
    TE_PlayerDecalId = 424
    TE_ProjectedDecalId = 425
    TE_SmokeId = 426


@dataclass
class CMsgTEArmorRicochet(betterproto.Message):
    pos: "CMsgVector" = betterproto.message_field(1)
    dir: "CMsgVector" = betterproto.message_field(2)


@dataclass
class CMsgTEBaseBeam(betterproto.Message):
    modelindex: float = betterproto.fixed64_field(1)
    haloindex: float = betterproto.fixed64_field(2)
    startframe: int = betterproto.uint32_field(3)
    framerate: int = betterproto.uint32_field(4)
    life: float = betterproto.float_field(5)
    width: float = betterproto.float_field(6)
    endwidth: float = betterproto.float_field(7)
    fadelength: int = betterproto.uint32_field(8)
    amplitude: float = betterproto.float_field(9)
    color: float = betterproto.fixed32_field(10)
    speed: int = betterproto.uint32_field(11)
    flags: int = betterproto.uint32_field(12)


@dataclass
class CMsgTEBeamEntPoint(betterproto.Message):
    base: "CMsgTEBaseBeam" = betterproto.message_field(1)
    startentity: int = betterproto.uint32_field(2)
    endentity: int = betterproto.uint32_field(3)
    start: "CMsgVector" = betterproto.message_field(4)
    end: "CMsgVector" = betterproto.message_field(5)


@dataclass
class CMsgTEBeamEnts(betterproto.Message):
    base: "CMsgTEBaseBeam" = betterproto.message_field(1)
    startentity: int = betterproto.uint32_field(2)
    endentity: int = betterproto.uint32_field(3)


@dataclass
class CMsgTEBeamPoints(betterproto.Message):
    base: "CMsgTEBaseBeam" = betterproto.message_field(1)
    start: "CMsgVector" = betterproto.message_field(2)
    end: "CMsgVector" = betterproto.message_field(3)


@dataclass
class CMsgTEBeamRing(betterproto.Message):
    base: "CMsgTEBaseBeam" = betterproto.message_field(1)
    startentity: int = betterproto.uint32_field(2)
    endentity: int = betterproto.uint32_field(3)


@dataclass
class CMsgTEBSPDecal(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    normal: "CMsgVector" = betterproto.message_field(2)
    saxis: "CMsgVector" = betterproto.message_field(3)
    entity: int = betterproto.int32_field(4)
    index: int = betterproto.uint32_field(5)


@dataclass
class CMsgTEBubbles(betterproto.Message):
    mins: "CMsgVector" = betterproto.message_field(1)
    maxs: "CMsgVector" = betterproto.message_field(2)
    height: float = betterproto.float_field(3)
    count: int = betterproto.uint32_field(4)
    speed: float = betterproto.float_field(5)


@dataclass
class CMsgTEBubbleTrail(betterproto.Message):
    mins: "CMsgVector" = betterproto.message_field(1)
    maxs: "CMsgVector" = betterproto.message_field(2)
    waterz: float = betterproto.float_field(3)
    count: int = betterproto.uint32_field(4)
    speed: float = betterproto.float_field(5)


@dataclass
class CMsgTEDecal(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    start: "CMsgVector" = betterproto.message_field(2)
    entity: int = betterproto.int32_field(3)
    hitbox: int = betterproto.uint32_field(4)
    index: int = betterproto.uint32_field(5)


@dataclass
class CMsgEffectData(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    start: "CMsgVector" = betterproto.message_field(2)
    normal: "CMsgVector" = betterproto.message_field(3)
    angles: "CMsgQAngle" = betterproto.message_field(4)
    entity: float = betterproto.fixed32_field(5)
    otherentity: float = betterproto.fixed32_field(6)
    scale: float = betterproto.float_field(7)
    magnitude: float = betterproto.float_field(8)
    radius: float = betterproto.float_field(9)
    surfaceprop: float = betterproto.fixed32_field(10)
    effectindex: float = betterproto.fixed64_field(11)
    damagetype: int = betterproto.uint32_field(12)
    material: int = betterproto.uint32_field(13)
    hitbox: int = betterproto.uint32_field(14)
    color: int = betterproto.uint32_field(15)
    flags: int = betterproto.uint32_field(16)
    attachmentindex: int = betterproto.int32_field(17)
    effectname: int = betterproto.uint32_field(18)
    attachmentname: int = betterproto.uint32_field(19)


@dataclass
class CMsgTEEffectDispatch(betterproto.Message):
    effectdata: "CMsgEffectData" = betterproto.message_field(1)


@dataclass
class CMsgTEEnergySplash(betterproto.Message):
    pos: "CMsgVector" = betterproto.message_field(1)
    dir: "CMsgVector" = betterproto.message_field(2)
    explosive: bool = betterproto.bool_field(3)


@dataclass
class CMsgTEFizz(betterproto.Message):
    entity: int = betterproto.int32_field(1)
    density: int = betterproto.uint32_field(2)
    current: int = betterproto.int32_field(3)


@dataclass
class CMsgTEShatterSurface(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    angles: "CMsgQAngle" = betterproto.message_field(2)
    force: "CMsgVector" = betterproto.message_field(3)
    forcepos: "CMsgVector" = betterproto.message_field(4)
    width: float = betterproto.float_field(5)
    height: float = betterproto.float_field(6)
    shardsize: float = betterproto.float_field(7)
    surfacetype: int = betterproto.uint32_field(8)
    frontcolor: float = betterproto.fixed32_field(9)
    backcolor: float = betterproto.fixed32_field(10)


@dataclass
class CMsgTEGlowSprite(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    scale: float = betterproto.float_field(2)
    life: float = betterproto.float_field(3)
    brightness: int = betterproto.uint32_field(4)


@dataclass
class CMsgTEImpact(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    normal: "CMsgVector" = betterproto.message_field(2)
    type: int = betterproto.uint32_field(3)


@dataclass
class CMsgTEMuzzleFlash(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    angles: "CMsgQAngle" = betterproto.message_field(2)
    scale: float = betterproto.float_field(3)
    type: int = betterproto.uint32_field(4)


@dataclass
class CMsgTEBloodStream(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    direction: "CMsgVector" = betterproto.message_field(2)
    color: float = betterproto.fixed32_field(3)
    amount: int = betterproto.uint32_field(4)


@dataclass
class CMsgTEExplosion(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    framerate: int = betterproto.uint32_field(2)
    flags: int = betterproto.uint32_field(3)
    normal: "CMsgVector" = betterproto.message_field(4)
    materialtype: int = betterproto.uint32_field(5)
    radius: int = betterproto.uint32_field(6)
    magnitude: int = betterproto.uint32_field(7)
    scale: float = betterproto.float_field(8)
    affect_ragdolls: bool = betterproto.bool_field(9)
    effect_name: str = betterproto.string_field(10)
    explosion_type: int = betterproto.uint32_field(11)
    create_debris: bool = betterproto.bool_field(12)
    debris_origin: "CMsgVector" = betterproto.message_field(13)
    debris_surfaceprop: float = betterproto.fixed32_field(14)


@dataclass
class CMsgTEDust(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    size: float = betterproto.float_field(2)
    speed: float = betterproto.float_field(3)
    direction: "CMsgVector" = betterproto.message_field(4)


@dataclass
class CMsgTELargeFunnel(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    reversed: int = betterproto.uint32_field(2)


@dataclass
class CMsgTESparks(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    magnitude: int = betterproto.uint32_field(2)
    length: int = betterproto.uint32_field(3)
    direction: "CMsgVector" = betterproto.message_field(4)


@dataclass
class CMsgTEPhysicsProp(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    velocity: "CMsgVector" = betterproto.message_field(2)
    angles: "CMsgQAngle" = betterproto.message_field(3)
    skin: float = betterproto.fixed32_field(4)
    flags: int = betterproto.uint32_field(5)
    effects: int = betterproto.uint32_field(6)
    color: float = betterproto.fixed32_field(7)
    modelindex: float = betterproto.fixed64_field(8)
    unused_breakmodelsnottomake: int = betterproto.uint32_field(9)
    scale: float = betterproto.float_field(10)
    dmgpos: "CMsgVector" = betterproto.message_field(11)
    dmgdir: "CMsgVector" = betterproto.message_field(12)
    dmgtype: int = betterproto.int32_field(13)


@dataclass
class CMsgTEPlayerDecal(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    player: int = betterproto.int32_field(2)
    entity: int = betterproto.int32_field(3)


@dataclass
class CMsgTEProjectedDecal(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    angles: "CMsgQAngle" = betterproto.message_field(2)
    index: int = betterproto.uint32_field(3)
    distance: float = betterproto.float_field(4)


@dataclass
class CMsgTESmoke(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    scale: float = betterproto.float_field(2)


@dataclass
class CMsgTEWorldDecal(betterproto.Message):
    origin: "CMsgVector" = betterproto.message_field(1)
    normal: "CMsgVector" = betterproto.message_field(2)
    index: int = betterproto.uint32_field(3)
