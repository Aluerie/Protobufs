# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_scenariomessages.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CScenario_Position(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)


@dataclass
class CScenarioGame_RoshanSpawner(betterproto.Message):
    kill_count: int = betterproto.int32_field(1)
    state: int = betterproto.int32_field(2)
    cooldown: float = betterproto.float_field(3)
    killer_team: int = betterproto.int32_field(4)


@dataclass
class CScenarioEnt_Courier(betterproto.Message):
    team_number: int = betterproto.int32_field(1)
    owner_player_id: int = betterproto.int32_field(2)
    cooldown: float = betterproto.float_field(3)


@dataclass
class CScenarioEnt_NPC(betterproto.Message):
    position: "CScenario_Position" = betterproto.message_field(1)
    unit_name: str = betterproto.string_field(2)
    team_number: int = betterproto.int32_field(3)
    health_frac: float = betterproto.float_field(4)
    owning_camp: str = betterproto.string_field(10)
    owning_camp_position: "CScenario_Position" = betterproto.message_field(11)
    invade_goal: str = betterproto.string_field(20)


@dataclass
class CScenarioEnt_SpiritBear(betterproto.Message):
    owner_id: int = betterproto.int32_field(1)
    team_id: int = betterproto.int32_field(2)


@dataclass
class CScenarioEnt_DroppedItem(betterproto.Message):
    position: "CScenario_Position" = betterproto.message_field(1)


@dataclass
class CMsgDotaScenario(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    game: "CMsgDotaScenarioGame" = betterproto.message_field(2)
    teams: List["CMsgDotaScenarioTeam"] = betterproto.message_field(3)
    heroes: List["CMsgDotaScenarioHero"] = betterproto.message_field(4)
    stock: List["CMsgDotaScenarioStock"] = betterproto.message_field(5)
    buildings: List["CMsgDotaScenarioBuilding"] = betterproto.message_field(6)
    entities: List["CMsgDotaScenarioEntity"] = betterproto.message_field(7)
    items: List["CMsgDotaScenarioItem"] = betterproto.message_field(8)
    modifiers: List["CMsgDotaScenarioModifier"] = betterproto.message_field(9)


@dataclass
class CMsgDotaScenarioEntityRef(betterproto.Message):
    player_id: int = betterproto.int32_field(1)
    neutral_stash_id: int = betterproto.int32_field(2)
    entity_idx: int = betterproto.int32_field(3)
    roshan: bool = betterproto.bool_field(4)
    ability_name: str = betterproto.string_field(10)


@dataclass
class CMsgDotaScenarioGame(betterproto.Message):
    match_id: int = betterproto.uint64_field(1)
    game_mode: int = betterproto.int32_field(2)
    clock_time: float = betterproto.float_field(3)
    internal_time: float = betterproto.float_field(4)
    roshan: "CScenarioGame_RoshanSpawner" = betterproto.message_field(5)


@dataclass
class CMsgDotaScenarioTeamNeutralItem(betterproto.Message):
    name: str = betterproto.string_field(1)
    consumed: bool = betterproto.bool_field(2)
    tier: int = betterproto.int32_field(3)


@dataclass
class CMsgDotaScenarioTeam(betterproto.Message):
    team_number: int = betterproto.int32_field(1)
    neutral_items: List["CMsgDotaScenarioTeamNeutralItem"] = betterproto.message_field(
        2
    )
    hero_kills: int = betterproto.int32_field(3)
    tower_kills: int = betterproto.int32_field(4)
    barracks_kills: int = betterproto.int32_field(5)
    glyph_cooldown: float = betterproto.float_field(6)
    radar_cooldown: float = betterproto.float_field(7)


@dataclass
class CMsgDotaScenarioHeroHeroInt(betterproto.Message):
    player_id: int = betterproto.int32_field(1)
    value: int = betterproto.int32_field(2)


@dataclass
class CMsgDotaScenarioHeroHeroFloat(betterproto.Message):
    player_id: int = betterproto.int32_field(1)
    value: float = betterproto.float_field(2)


@dataclass
class CMsgDotaScenarioDamageStatsByType(betterproto.Message):
    damage_type: int = betterproto.int32_field(1)
    received_pre_reduction: int = betterproto.int32_field(2)
    received_post_reduction: int = betterproto.int32_field(3)
    outgoing_pre_reduction: int = betterproto.int32_field(4)
    outgoing_post_reduction: int = betterproto.int32_field(5)


@dataclass
class CMsgDotaScenarioHeroAbility(betterproto.Message):
    name: str = betterproto.string_field(1)
    level: int = betterproto.int32_field(2)


@dataclass
class CMsgDotaScenarioHero(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    player_id: int = betterproto.int32_field(2)
    team_id: int = betterproto.int32_field(3)
    hero: str = betterproto.string_field(4)
    total_xp: int = betterproto.int32_field(5)
    bkb_charges_used: int = betterproto.int32_field(6)
    aeon_charges_used: int = betterproto.int32_field(7)
    reliable_gold: int = betterproto.int32_field(8)
    unreliable_gold: int = betterproto.int32_field(9)
    total_earned_gold: int = betterproto.int32_field(10)
    shared_gold: int = betterproto.int32_field(11)
    hero_kill_gold: int = betterproto.int32_field(12)
    creep_kill_gold: int = betterproto.int32_field(13)
    neutral_kill_gold: int = betterproto.int32_field(14)
    courier_gold: int = betterproto.int32_field(15)
    bounty_gold: int = betterproto.int32_field(16)
    roshan_gold: int = betterproto.int32_field(17)
    building_gold: int = betterproto.int32_field(18)
    other_gold: int = betterproto.int32_field(19)
    income_gold: int = betterproto.int32_field(26)
    ward_kill_gold: int = betterproto.int32_field(27)
    ability_gold: int = betterproto.int32_field(28)
    denies: int = betterproto.int32_field(29)
    last_hits: int = betterproto.int32_field(30)
    last_hit_streak: int = betterproto.int32_field(31)
    last_hit_multikill: int = betterproto.int32_field(32)
    nearby_creep_death_count: int = betterproto.int32_field(33)
    claimed_deny_count: int = betterproto.int32_field(34)
    claimed_miss_count: int = betterproto.int32_field(35)
    miss_count: int = betterproto.int32_field(36)
    buyback_cooldown_time: float = betterproto.float_field(40)
    buyback_gold_limit_time: float = betterproto.float_field(41)
    stun_duration: float = betterproto.float_field(44)
    healing: float = betterproto.float_field(45)
    tower_kills: int = betterproto.int32_field(46)
    roshan_kills: int = betterproto.int32_field(47)
    observer_wards_placed: int = betterproto.int32_field(48)
    sentry_wards_placed: int = betterproto.int32_field(49)
    creeps_stacked: int = betterproto.int32_field(50)
    camps_stacked: int = betterproto.int32_field(51)
    rune_pickups: int = betterproto.int32_field(52)
    gold_spent_on_support: int = betterproto.int32_field(53)
    hero_damage: int = betterproto.int32_field(54)
    wards_purchased: int = betterproto.int32_field(55)
    wards_destroyed: int = betterproto.int32_field(56)
    gold_spent_on_consumables: int = betterproto.int32_field(58)
    gold_spent_on_items: int = betterproto.int32_field(59)
    gold_spent_on_buybacks: int = betterproto.int32_field(60)
    gold_lost_to_death: int = betterproto.int32_field(61)
    kills: int = betterproto.int32_field(62)
    assists: int = betterproto.int32_field(63)
    deaths: int = betterproto.int32_field(64)
    kill_streak: int = betterproto.int32_field(65)
    respawn_seconds: int = betterproto.int32_field(68)
    last_buyback_time: int = betterproto.int32_field(69)
    first_blood_claimed: bool = betterproto.bool_field(71)
    first_blood_given: bool = betterproto.bool_field(72)
    bounty_runes: int = betterproto.int32_field(73)
    outposts_captured: int = betterproto.int32_field(74)
    position: "CScenario_Position" = betterproto.message_field(75)
    enemy_kills: List["CMsgDotaScenarioHeroHeroInt"] = betterproto.message_field(150)
    damage_stats: List["CMsgDotaScenarioDamageStatsByType"] = betterproto.message_field(
        151
    )
    abilities: List["CMsgDotaScenarioHeroAbility"] = betterproto.message_field(152)


@dataclass
class CMsgDotaScenarioStock(betterproto.Message):
    name: str = betterproto.string_field(1)
    team_number: int = betterproto.int32_field(2)
    player_id: int = betterproto.int32_field(3)
    current_stock: int = betterproto.int32_field(4)
    cooldown: float = betterproto.float_field(5)
    bonus_stock: int = betterproto.int32_field(6)


@dataclass
class CMsgDotaScenarioBuilding(betterproto.Message):
    entity_name: str = betterproto.string_field(1)
    entity_class: str = betterproto.string_field(2)
    team_id: int = betterproto.int32_field(3)
    is_destroyed: bool = betterproto.bool_field(4)
    health_frac: float = betterproto.float_field(5)


@dataclass
class CMsgDotaScenarioEntity(betterproto.Message):
    courier: "CScenarioEnt_Courier" = betterproto.message_field(1)
    npc: "CScenarioEnt_NPC" = betterproto.message_field(2)
    spirit_bear: "CScenarioEnt_SpiritBear" = betterproto.message_field(3)
    dropped_item: "CScenarioEnt_DroppedItem" = betterproto.message_field(4)


@dataclass
class CMsgDotaScenarioItem(betterproto.Message):
    name: str = betterproto.string_field(1)
    location: "CMsgDotaScenarioEntityRef" = betterproto.message_field(2)
    owner_id: int = betterproto.int32_field(3)
    item_slot: int = betterproto.int32_field(4)
    neutral_drop_team: int = betterproto.int32_field(5)
    charges: int = betterproto.int32_field(6)
    secondary_charges: int = betterproto.int32_field(7)
    lifetime: float = betterproto.float_field(8)
    stored_rune_type: int = betterproto.int32_field(9)


@dataclass
class CMsgDotaScenarioModifier(betterproto.Message):
    name: str = betterproto.string_field(1)
    parent: "CMsgDotaScenarioEntityRef" = betterproto.message_field(2)
    caster: "CMsgDotaScenarioEntityRef" = betterproto.message_field(3)
    ability: "CMsgDotaScenarioEntityRef" = betterproto.message_field(4)
    duration: float = betterproto.float_field(5)
    lifetime_remaining: float = betterproto.float_field(6)
    stack_count: int = betterproto.int32_field(7)
    create_even_if_existing: bool = betterproto.bool_field(8)
    create_without_caster: bool = betterproto.bool_field(9)
    create_without_ability: bool = betterproto.bool_field(10)
    moonshard_consumed_bonus: int = betterproto.int32_field(100)
    moonshard_consumed_bonus_night_vision: int = betterproto.int32_field(101)
    wardtruesight_range: int = betterproto.int32_field(110)
    ultimate_scepter_consumed_alchemist_bonus_all_stats: int = betterproto.int32_field(
        120
    )
    ultimate_scepter_consumed_alchemist_bonus_health: int = betterproto.int32_field(121)
    ultimate_scepter_consumed_alchemist_bonus_mana: int = betterproto.int32_field(122)
