# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_steamlearn.steamworkssdk.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib


class ESteamLearnDataType(betterproto.Enum):
    STEAMLEARN_DATATYPE_INVALID = 0
    STEAMLEARN_DATATYPE_INT32 = 1
    STEAMLEARN_DATATYPE_FLOAT32 = 2
    STEAMLEARN_DATATYPE_BOOL = 3
    STEAMLEARN_DATATYPE_STRING = 4
    STEAMLEARN_DATATYPE_OBJECT = 5


class ESteammLearnRegisterDataSourceResult(betterproto.Enum):
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR = 0
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_SUCCESS_CREATED = 1
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_SUCCESS_FOUND = 2
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_GENERIC = 3
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_NAME = 4
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_VERSION = 5
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_DATA_CHANGED = 6
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_DATA_INVALID = 7
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_FORBIDDEN = 8
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_TIMESTAMP = 9
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_DISABLED = 10


class ESteamLearnCacheDataResult(betterproto.Enum):
    STEAMLEARN_CACHE_DATA_ERROR = 0
    STEAMLEARN_CACHE_DATA_SUCCESS = 1
    STEAMLEARN_CACHE_DATA_ERROR_UNKNOWN_DATA_SOURCE = 2
    STEAMLEARN_CACHE_DATA_ERROR_UNCACHED_DATA_SOURCE = 3
    STEAMLEARN_CACHE_DATA_ERROR_INVALID_KEYS = 4
    STEAMLEARN_CACHE_DATA_ERROR_FORBIDDEN = 5
    STEAMLEARN_CACHE_DATA_ERROR_INVALID_TIMESTAMP = 6
    STEAMLEARN_CACHE_DATA_DISABLED = 7


class ESteamLearnSnapshotProjectResult(betterproto.Enum):
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR = 0
    STEAMLEARN_SNAPSHOT_PROJECT_SUCCESS_STORED = 1
    STEAMLEARN_SNAPSHOT_PROJECT_SUCCESS_QUEUED = 2
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_PROJECT_ID = 3
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_UNKNOWN_DATA_SOURCE = 4
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_DATA_SOURCE_KEY = 5
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_MISSING_CACHE_DURATION = 6
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_NO_PUBLISHED_CONFIG = 7
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_FORBIDDEN = 8
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_TIMESTAMP = 9
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INTERNAL_DATA_SOURCE_ERROR = 10
    STEAMLEARN_SNAPSHOT_PROJECT_DISABLED = 11
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_PUBLISHED_VERSION = 12


class ESteamLearnGetHMACKeysResult(betterproto.Enum):
    STEAMLEARN_GET_HMAC_KEYS_SUCCESS = 0


class ESteamLearnInferenceResult(betterproto.Enum):
    STEAMLEARN_INFERENCE_ERROR = 0
    STEAMLEARN_INFERENCE_SUCCESS = 1
    STEAMLEARN_INFERENCE_ERROR_INVALID_PROJECT_ID = 2
    STEAMLEARN_INFERENCE_ERROR_MISSING_CACHED_SCHEMA_DATA = 3
    STEAMLEARN_INFERENCE_ERROR_NO_PUBLISHED_CONFIG = 4
    STEAMLEARN_INFERENCE_ERROR_FORBIDDEN = 5
    STEAMLEARN_INFERENCE_ERROR_INVALID_TIMESTAMP = 6
    STEAMLEARN_INFERENCE_ERROR_INVALID_PUBLISHED_VERSION = 7
    STEAMLEARN_INFERENCE_ERROR_NO_FETCH_ID_FOUND = 8
    STEAMLEARN_INFERENCE_ERROR_TOO_BUSY = 9


class ESteamLearnInferenceMetadataResult(betterproto.Enum):
    STEAMLEARN_INFERENCE_METADATA_ERROR = 0
    STEAMLEARN_INFERENCE_METADATA_SUCCESS = 1
    STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_PROJECT_ID = 2
    STEAMLEARN_INFERENCE_METADATA_ERROR_NO_PUBLISHED_CONFIG = 3
    STEAMLEARN_INFERENCE_METADATA_ERROR_FORBIDDEN = 4
    STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_TIMESTAMP = 5
    STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_PUBLISHED_VERSION = 6
    STEAMLEARN_INFERENCE_METADATA_ERROR_NO_FETCH_ID_FOUND = 7


@dataclass
class CMsgSteamLearnDataSourceDescObject(betterproto.Message):
    elements: List["CMsgSteamLearnDataSourceDescElement"] = betterproto.message_field(1)


@dataclass
class CMsgSteamLearnDataSourceDescElement(betterproto.Message):
    name: str = betterproto.string_field(1)
    data_type: "ESteamLearnDataType" = betterproto.enum_field(2)
    object: "CMsgSteamLearnDataSourceDescObject" = betterproto.message_field(3)
    count: int = betterproto.uint32_field(4)


@dataclass
class CMsgSteamLearnDataSource(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    version: int = betterproto.uint32_field(3)
    source_description: str = betterproto.string_field(4)
    structure: "CMsgSteamLearnDataSourceDescObject" = betterproto.message_field(5)
    structure_crc: int = betterproto.uint32_field(6)
    cache_duration_seconds: int = betterproto.uint32_field(7)


@dataclass
class CMsgSteamLearnDataObject(betterproto.Message):
    elements: List["CMsgSteamLearnDataElement"] = betterproto.message_field(1)


@dataclass
class CMsgSteamLearnDataElement(betterproto.Message):
    name: str = betterproto.string_field(1)
    data_int32s: List[int] = betterproto.int32_field(20)
    data_floats: List[float] = betterproto.float_field(21)
    data_bools: List[bool] = betterproto.bool_field(22)
    data_strings: List[str] = betterproto.string_field(23)
    data_objects: List["CMsgSteamLearnDataObject"] = betterproto.message_field(24)


@dataclass
class CMsgSteamLearnData(betterproto.Message):
    data_source_id: int = betterproto.uint32_field(1)
    keys: List[int] = betterproto.uint64_field(2)
    data_object: "CMsgSteamLearnDataObject" = betterproto.message_field(3)


@dataclass
class CMsgSteamLearnDataList(betterproto.Message):
    data: List["CMsgSteamLearnData"] = betterproto.message_field(1)


@dataclass
class CMsgSteamLearn_AccessData(betterproto.Message):
    publisher_id: int = betterproto.uint32_field(1)
    timestamp: int = betterproto.uint32_field(2)
    random_value: int = betterproto.uint64_field(3)


@dataclass
class CMsgSteamLearn_RegisterDataSource_Request(betterproto.Message):
    access_token: str = betterproto.string_field(1)
    access_data: "CMsgSteamLearn_AccessData" = betterproto.message_field(2)
    data_source: "CMsgSteamLearnDataSource" = betterproto.message_field(3)


@dataclass
class CMsgSteamLearn_RegisterDataSource_Response(betterproto.Message):
    result: "ESteammLearnRegisterDataSourceResult" = betterproto.enum_field(1)
    data_source: "CMsgSteamLearnDataSource" = betterproto.message_field(2)


@dataclass
class CMsgSteamLearn_CacheData_Request(betterproto.Message):
    access_token: str = betterproto.string_field(1)
    access_data: "CMsgSteamLearn_AccessData" = betterproto.message_field(2)
    data: "CMsgSteamLearnData" = betterproto.message_field(3)


@dataclass
class CMsgSteamLearn_CacheData_Response(betterproto.Message):
    cache_data_result: "ESteamLearnCacheDataResult" = betterproto.enum_field(1)


@dataclass
class CMsgSteamLearn_SnapshotProject_Request(betterproto.Message):
    access_token: str = betterproto.string_field(1)
    access_data: "CMsgSteamLearn_AccessData" = betterproto.message_field(2)
    project_id: int = betterproto.uint32_field(3)
    published_version: int = betterproto.uint32_field(7)
    keys: List[int] = betterproto.uint64_field(4)
    data: List["CMsgSteamLearnData"] = betterproto.message_field(5)
    pending_data_limit_seconds: int = betterproto.uint32_field(6)


@dataclass
class CMsgSteamLearn_SnapshotProject_Response(betterproto.Message):
    snapshot_result: "ESteamLearnSnapshotProjectResult" = betterproto.enum_field(1)


@dataclass
class CMsgSteamLearn_BatchOperation_Request(betterproto.Message):
    cache_data_requests: List[
        "CMsgSteamLearn_CacheData_Request"
    ] = betterproto.message_field(1)
    snapshot_requests: List[
        "CMsgSteamLearn_SnapshotProject_Request"
    ] = betterproto.message_field(2)


@dataclass
class CMsgSteamLearn_BatchOperation_Response(betterproto.Message):
    cache_data_responses: List[
        "CMsgSteamLearn_CacheData_Response"
    ] = betterproto.message_field(1)
    snapshot_responses: List[
        "CMsgSteamLearn_SnapshotProject_Response"
    ] = betterproto.message_field(2)


@dataclass
class CMsgSteamLearnHMACKeys(betterproto.Message):
    register_data_source_key: str = betterproto.string_field(1)
    cache_data_keys: List[
        "CMsgSteamLearnHMACKeysCacheDataKeys"
    ] = betterproto.message_field(2)
    snapshot_project_keys: List[
        "CMsgSteamLearnHMACKeysSnapshotProjectKeys"
    ] = betterproto.message_field(3)


@dataclass
class CMsgSteamLearnHMACKeysCacheDataKeys(betterproto.Message):
    data_source_id: int = betterproto.uint32_field(1)
    version: int = betterproto.uint32_field(3)
    key: str = betterproto.string_field(2)


@dataclass
class CMsgSteamLearnHMACKeysSnapshotProjectKeys(betterproto.Message):
    project_id: int = betterproto.uint32_field(1)
    published_version: int = betterproto.uint32_field(3)
    key: str = betterproto.string_field(2)


@dataclass
class CMsgSteamLearn_GetHMACKeys_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass
class CMsgSteamLearn_GetHMACKeys_Response(betterproto.Message):
    result: "ESteamLearnGetHMACKeysResult" = betterproto.enum_field(1)
    keys: "CMsgSteamLearnHMACKeys" = betterproto.message_field(2)


@dataclass
class CMsgSteamLearn_Inference_Request(betterproto.Message):
    access_token: str = betterproto.string_field(1)
    access_data: "CMsgSteamLearn_AccessData" = betterproto.message_field(2)
    project_id: int = betterproto.uint32_field(3)
    published_version: int = betterproto.uint32_field(4)
    override_train_id: int = betterproto.uint32_field(5)
    data: "CMsgSteamLearnDataList" = betterproto.message_field(6)
    additional_data: List[float] = betterproto.float_field(7)


@dataclass
class CMsgSteamLearn_InferenceMetadata_Request(betterproto.Message):
    access_token: str = betterproto.string_field(1)
    access_data: "CMsgSteamLearn_AccessData" = betterproto.message_field(2)
    project_id: int = betterproto.uint32_field(3)
    published_version: int = betterproto.uint32_field(4)
    override_train_id: int = betterproto.uint32_field(5)


@dataclass
class CMsgSteamLearn_InferenceMetadataBackend_Request(betterproto.Message):
    project_id: int = betterproto.uint32_field(1)
    fetch_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgSteamLearn_InferenceMetadata_Response(betterproto.Message):
    inference_metadata_result: "ESteamLearnInferenceMetadataResult" = (
        betterproto.enum_field(1)
    )
    row_range: "CMsgSteamLearn_InferenceMetadata_ResponseRowRange" = (
        betterproto.message_field(2)
    )
    ranges: List[
        "CMsgSteamLearn_InferenceMetadata_ResponseRange"
    ] = betterproto.message_field(3)
    std_devs: List[
        "CMsgSteamLearn_InferenceMetadata_ResponseStdDev"
    ] = betterproto.message_field(4)
    compact_tables: List[
        "CMsgSteamLearn_InferenceMetadata_ResponseCompactTable"
    ] = betterproto.message_field(5)
    kmeans: List[
        "CMsgSteamLearn_InferenceMetadata_ResponseKMeans"
    ] = betterproto.message_field(6)
    snapshot_histogram: "CMsgSteamLearn_InferenceMetadata_ResponseSnapshotHistogram" = (
        betterproto.message_field(7)
    )


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseRowRange(betterproto.Message):
    min_row: int = betterproto.uint64_field(1)
    max_row: int = betterproto.uint64_field(2)


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseRange(betterproto.Message):
    data_element_path: str = betterproto.string_field(1)
    min_value: float = betterproto.float_field(2)
    max_value: float = betterproto.float_field(3)


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseStdDev(betterproto.Message):
    data_element_path: str = betterproto.string_field(1)
    mean: float = betterproto.float_field(2)
    std_dev: float = betterproto.float_field(3)


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseCompactTable(betterproto.Message):
    name: str = betterproto.string_field(1)
    map_values: List[
        "CMsgSteamLearn_InferenceMetadata_ResponseCompactTableMapValuesEntry"
    ] = betterproto.message_field(2)
    map_mappings: List[
        "CMsgSteamLearn_InferenceMetadata_ResponseCompactTableMapMappingsEntry"
    ] = betterproto.message_field(3)


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseCompactTableEntry(betterproto.Message):
    value: int = betterproto.uint32_field(1)
    mapping: int = betterproto.uint32_field(2)
    count: int = betterproto.uint64_field(3)


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseCompactTableMapValuesEntry(
    betterproto.Message
):
    key: int = betterproto.uint32_field(1)
    value: "CMsgSteamLearn_InferenceMetadata_ResponseCompactTableEntry" = (
        betterproto.message_field(2)
    )


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseCompactTableMapMappingsEntry(
    betterproto.Message
):
    key: int = betterproto.uint32_field(1)
    value: "CMsgSteamLearn_InferenceMetadata_ResponseCompactTableEntry" = (
        betterproto.message_field(2)
    )


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseKMeans(betterproto.Message):
    name: str = betterproto.string_field(1)
    clusters: List[
        "CMsgSteamLearn_InferenceMetadata_ResponseKMeansCluster"
    ] = betterproto.message_field(2)


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseKMeansCluster(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
    radius: float = betterproto.float_field(3)
    radius_75pct: float = betterproto.float_field(4)
    radius_50pct: float = betterproto.float_field(5)
    radius_25pct: float = betterproto.float_field(6)


@dataclass
class CMsgSteamLearn_InferenceMetadata_ResponseSnapshotHistogram(betterproto.Message):
    min_value: float = betterproto.float_field(1)
    max_value: float = betterproto.float_field(2)
    num_buckets: int = betterproto.uint32_field(3)
    bucket_counts: List[int] = betterproto.uint32_field(4)


@dataclass
class CMsgSteamLearn_InferenceBackend_Response(betterproto.Message):
    outputs: List[
        "CMsgSteamLearn_InferenceBackend_ResponseOutput"
    ] = betterproto.message_field(1)


@dataclass
class CMsgSteamLearn_InferenceBackend_ResponseBinaryCrossEntropyOutput(
    betterproto.Message
):
    value: float = betterproto.float_field(1)


@dataclass
class CMsgSteamLearn_InferenceBackend_ResponseMutliBinaryCrossEntropyOutput(
    betterproto.Message
):
    weight: List[float] = betterproto.float_field(1)
    value: List[float] = betterproto.float_field(2)


@dataclass
class CMsgSteamLearn_InferenceBackend_ResponseCategoricalCrossEntropyOutput(
    betterproto.Message
):
    weight: List[float] = betterproto.float_field(1)
    value: List[float] = betterproto.float_field(2)


@dataclass
class CMsgSteamLearn_InferenceBackend_ResponseOutput(betterproto.Message):
    binary_crossentropy: "CMsgSteamLearn_InferenceBackend_ResponseBinaryCrossEntropyOutput" = betterproto.message_field(
        1, group="ResponseType"
    )
    categorical_crossentropy: "CMsgSteamLearn_InferenceBackend_ResponseCategoricalCrossEntropyOutput" = betterproto.message_field(
        2, group="ResponseType"
    )
    multi_binary_crossentropy: "CMsgSteamLearn_InferenceBackend_ResponseMutliBinaryCrossEntropyOutput" = betterproto.message_field(
        3, group="ResponseType"
    )


@dataclass
class CMsgSteamLearn_Inference_Response(betterproto.Message):
    inference_result: "ESteamLearnInferenceResult" = betterproto.enum_field(1)
    backend_response: "CMsgSteamLearn_InferenceBackend_Response" = (
        betterproto.message_field(2)
    )


class SteamLearnStub(betterproto.ServiceStub):
    async def register_data_source(
        self,
        *,
        access_token: str = "",
        access_data: Optional["CMsgSteamLearn_AccessData"] = None,
        data_source: Optional["CMsgSteamLearnDataSource"] = None,
    ) -> CMsgSteamLearn_RegisterDataSource_Response:
        request = CMsgSteamLearn_RegisterDataSource_Request()
        request.access_token = access_token
        if access_data is not None:
            request.access_data = access_data
        if data_source is not None:
            request.data_source = data_source

        return await self._unary_unary(
            "/.SteamLearn/RegisterDataSource",
            request,
            CMsgSteamLearn_RegisterDataSource_Response,
        )

    async def cache_data(
        self,
        *,
        access_token: str = "",
        access_data: Optional["CMsgSteamLearn_AccessData"] = None,
        data: Optional["CMsgSteamLearnData"] = None,
    ) -> CMsgSteamLearn_CacheData_Response:
        request = CMsgSteamLearn_CacheData_Request()
        request.access_token = access_token
        if access_data is not None:
            request.access_data = access_data
        if data is not None:
            request.data = data

        return await self._unary_unary(
            "/.SteamLearn/CacheData",
            request,
            CMsgSteamLearn_CacheData_Response,
        )

    async def snapshot_project(
        self,
        *,
        access_token: str = "",
        access_data: Optional["CMsgSteamLearn_AccessData"] = None,
        project_id: int = 0,
        published_version: int = 0,
        keys: List[int] = [],
        data: List["CMsgSteamLearnData"] = [],
        pending_data_limit_seconds: int = 0,
    ) -> CMsgSteamLearn_SnapshotProject_Response:
        request = CMsgSteamLearn_SnapshotProject_Request()
        request.access_token = access_token
        if access_data is not None:
            request.access_data = access_data
        request.project_id = project_id
        request.published_version = published_version
        request.keys = keys
        if data is not None:
            request.data = data
        request.pending_data_limit_seconds = pending_data_limit_seconds

        return await self._unary_unary(
            "/.SteamLearn/SnapshotProject",
            request,
            CMsgSteamLearn_SnapshotProject_Response,
        )

    async def batch_operation(
        self,
        *,
        cache_data_requests: List["CMsgSteamLearn_CacheData_Request"] = [],
        snapshot_requests: List["CMsgSteamLearn_SnapshotProject_Request"] = [],
    ) -> CMsgSteamLearn_BatchOperation_Response:
        request = CMsgSteamLearn_BatchOperation_Request()
        if cache_data_requests is not None:
            request.cache_data_requests = cache_data_requests
        if snapshot_requests is not None:
            request.snapshot_requests = snapshot_requests

        return await self._unary_unary(
            "/.SteamLearn/BatchOperation",
            request,
            CMsgSteamLearn_BatchOperation_Response,
        )

    async def get_h_m_a_c_keys(
        self, *, appid: int = 0
    ) -> CMsgSteamLearn_GetHMACKeys_Response:
        request = CMsgSteamLearn_GetHMACKeys_Request()
        request.appid = appid

        return await self._unary_unary(
            "/.SteamLearn/GetHMACKeys",
            request,
            CMsgSteamLearn_GetHMACKeys_Response,
        )

    async def inference(
        self,
        *,
        access_token: str = "",
        access_data: Optional["CMsgSteamLearn_AccessData"] = None,
        project_id: int = 0,
        published_version: int = 0,
        override_train_id: int = 0,
        data: Optional["CMsgSteamLearnDataList"] = None,
        additional_data: List[float] = [],
    ) -> CMsgSteamLearn_Inference_Response:
        request = CMsgSteamLearn_Inference_Request()
        request.access_token = access_token
        if access_data is not None:
            request.access_data = access_data
        request.project_id = project_id
        request.published_version = published_version
        request.override_train_id = override_train_id
        if data is not None:
            request.data = data
        request.additional_data = additional_data

        return await self._unary_unary(
            "/.SteamLearn/Inference",
            request,
            CMsgSteamLearn_Inference_Response,
        )

    async def inference_metadata(
        self,
        *,
        access_token: str = "",
        access_data: Optional["CMsgSteamLearn_AccessData"] = None,
        project_id: int = 0,
        published_version: int = 0,
        override_train_id: int = 0,
    ) -> CMsgSteamLearn_InferenceMetadata_Response:
        request = CMsgSteamLearn_InferenceMetadata_Request()
        request.access_token = access_token
        if access_data is not None:
            request.access_data = access_data
        request.project_id = project_id
        request.published_version = published_version
        request.override_train_id = override_train_id

        return await self._unary_unary(
            "/.SteamLearn/InferenceMetadata",
            request,
            CMsgSteamLearn_InferenceMetadata_Response,
        )
