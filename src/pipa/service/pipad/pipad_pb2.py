# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pipad.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 27, 2, "", "pipad.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0bpipad.proto\x12\x04pipa"\xb3\r\n\rDeployRequest\x12\x10\n\x08workload\x18\x01 \x01(\t\x12\x14\n\x0ctransactions\x18\x02 \x01(\x04\x12\x12\n\nthroughput\x18\x03 \x01(\x01\x12\x14\n\x0cused_threads\x18\x04 \x03(\r\x12\x10\n\x08run_time\x18\x05 \x01(\x01\x12\x0e\n\x06\x63ycles\x18\x06 \x01(\x04\x12\x14\n\x0cinstructions\x18\x07 \x01(\x04\x12\x19\n\x11\x63ycles_per_second\x18\x08 \x01(\x01\x12\x1f\n\x17instructions_per_second\x18\t \x01(\x01\x12\x0b\n\x03\x43PI\x18\n \x01(\x01\x12\x1b\n\x13\x63ycles_per_requests\x18\x0b \x01(\x01\x12\x13\n\x0bpath_length\x18\x0c \x01(\x01\x12\x19\n\x11\x63pu_frequency_mhz\x18\r \x01(\x01\x12\x14\n\x07\x63pu_usr\x18\x0e \x01(\x01H\x00\x88\x01\x01\x12\x15\n\x08\x63pu_nice\x18\x0f \x01(\x01H\x01\x88\x01\x01\x12\x14\n\x07\x63pu_sys\x18\x10 \x01(\x01H\x02\x88\x01\x01\x12\x17\n\ncpu_iowait\x18\x11 \x01(\x01H\x03\x88\x01\x01\x12\x16\n\tcpu_steal\x18\x12 \x01(\x01H\x04\x88\x01\x01\x12\x14\n\x07\x63pu_irq\x18\x13 \x01(\x01H\x05\x88\x01\x01\x12\x15\n\x08\x63pu_soft\x18\x14 \x01(\x01H\x06\x88\x01\x01\x12\x16\n\tcpu_guest\x18\x15 \x01(\x01H\x07\x88\x01\x01\x12\x16\n\tcpu_gnice\x18\x16 \x01(\x01H\x08\x88\x01\x01\x12\x15\n\x08\x63pu_idle\x18\x17 \x01(\x01H\t\x88\x01\x01\x12\x15\n\x08\x63pu_util\x18\x18 \x01(\x01H\n\x88\x01\x01\x12\x16\n\tkbmemfree\x18\x19 \x01(\x04H\x0b\x88\x01\x01\x12\x14\n\x07kbavail\x18\x1a \x01(\x04H\x0c\x88\x01\x01\x12\x16\n\tkbmemused\x18\x1b \x01(\x04H\r\x88\x01\x01\x12\x1c\n\x0fpercent_memused\x18\x1c \x01(\x01H\x0e\x88\x01\x01\x12\x16\n\tkbbuffers\x18\x1d \x01(\x04H\x0f\x88\x01\x01\x12\x15\n\x08kbcached\x18\x1e \x01(\x04H\x10\x88\x01\x01\x12\x15\n\x08kbcommit\x18\x1f \x01(\x04H\x11\x88\x01\x01\x12\x1b\n\x0epercent_commit\x18  \x01(\x01H\x12\x88\x01\x01\x12\x15\n\x08kbactive\x18! \x01(\x04H\x13\x88\x01\x01\x12\x14\n\x07kbinact\x18" \x01(\x04H\x14\x88\x01\x01\x12\x14\n\x07kbdirty\x18# \x01(\x04H\x15\x88\x01\x01\x12\x15\n\x08kbanonpg\x18$ \x01(\x04H\x16\x88\x01\x01\x12\x13\n\x06kbslab\x18% \x01(\x04H\x17\x88\x01\x01\x12\x15\n\x08kbkstack\x18& \x01(\x04H\x18\x88\x01\x01\x12\x14\n\x07kbpgtbl\x18\' \x01(\x04H\x19\x88\x01\x01\x12\x15\n\x08kbvmused\x18( \x01(\x04H\x1a\x88\x01\x01\x12\x0b\n\x03\x64\x65v\x18) \x01(\t\x12\x10\n\x03tps\x18* \x01(\x01H\x1b\x88\x01\x01\x12\x12\n\x05rkB_s\x18+ \x01(\x01H\x1c\x88\x01\x01\x12\x12\n\x05wkB_s\x18, \x01(\x01H\x1d\x88\x01\x01\x12\x12\n\x05\x64kB_s\x18- \x01(\x01H\x1e\x88\x01\x01\x12\x14\n\x07\x61req_sz\x18. \x01(\x01H\x1f\x88\x01\x01\x12\x13\n\x06\x61qu_sz\x18/ \x01(\x01H \x88\x01\x01\x12\x17\n\ndisk_await\x18\x30 \x01(\x01H!\x88\x01\x01\x12\x1e\n\x11percent_disk_util\x18\x31 \x01(\x01H"\x88\x01\x01\x12\x15\n\rdata_location\x18\x32 \x01(\t\x12\x0f\n\x07hw_info\x18\x33 \x01(\t\x12\x0f\n\x07sw_info\x18\x34 \x01(\t\x12\x10\n\x08platform\x18\x35 \x01(\t\x12\x14\n\x07\x63omment\x18\x36 \x01(\tH#\x88\x01\x01\x12\x10\n\x08username\x18\x37 \x01(\tB\n\n\x08_cpu_usrB\x0b\n\t_cpu_niceB\n\n\x08_cpu_sysB\r\n\x0b_cpu_iowaitB\x0c\n\n_cpu_stealB\n\n\x08_cpu_irqB\x0b\n\t_cpu_softB\x0c\n\n_cpu_guestB\x0c\n\n_cpu_gniceB\x0b\n\t_cpu_idleB\x0b\n\t_cpu_utilB\x0c\n\n_kbmemfreeB\n\n\x08_kbavailB\x0c\n\n_kbmemusedB\x12\n\x10_percent_memusedB\x0c\n\n_kbbuffersB\x0b\n\t_kbcachedB\x0b\n\t_kbcommitB\x11\n\x0f_percent_commitB\x0b\n\t_kbactiveB\n\n\x08_kbinactB\n\n\x08_kbdirtyB\x0b\n\t_kbanonpgB\t\n\x07_kbslabB\x0b\n\t_kbkstackB\n\n\x08_kbpgtblB\x0b\n\t_kbvmusedB\x06\n\x04_tpsB\x08\n\x06_rkB_sB\x08\n\x06_wkB_sB\x08\n\x06_dkB_sB\n\n\x08_areq_szB\t\n\x07_aqu_szB\r\n\x0b_disk_awaitB\x14\n\x12_percent_disk_utilB\n\n\x08_comment"y\n\nDeployResp\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x17\n\x0fupload_datetime\x18\x05 \x01(\t\x12\x13\n\x0bstatus_code\x18\x06 \x01(\r"n\n\x18\x44ownloadFullTableRequest\x12\x15\n\rpipad_ip_addr\x18\x01 \x01(\t\x12\x12\n\npipad_port\x18\x02 \x01(\r\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x13\n\x0b\x66ile_option\x18\x04 \x01(\t"-\n\x15\x44ownloadFullTableResp\x12\x14\n\x0c\x66ile_content\x18\x01 \x01(\x0c\x32\x8f\x02\n\x05PIPAD\x12\x31\n\x06\x44\x65ploy\x12\x13.pipa.DeployRequest\x1a\x10.pipa.DeployResp"\x00\x12>\n\x11\x44\x65ployStreamReply\x12\x13.pipa.DeployRequest\x1a\x10.pipa.DeployResp"\x00\x30\x01\x12?\n\x10\x44\x65ployBidiStream\x12\x13.pipa.DeployRequest\x1a\x10.pipa.DeployResp"\x00(\x01\x30\x01\x12R\n\x11\x44ownloadFullTable\x12\x1e.pipa.DownloadFullTableRequest\x1a\x1b.pipa.DownloadFullTableResp"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "pipad_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_DEPLOYREQUEST"]._serialized_start = 22
    _globals["_DEPLOYREQUEST"]._serialized_end = 1737
    _globals["_DEPLOYRESP"]._serialized_start = 1739
    _globals["_DEPLOYRESP"]._serialized_end = 1860
    _globals["_DOWNLOADFULLTABLEREQUEST"]._serialized_start = 1862
    _globals["_DOWNLOADFULLTABLEREQUEST"]._serialized_end = 1972
    _globals["_DOWNLOADFULLTABLERESP"]._serialized_start = 1974
    _globals["_DOWNLOADFULLTABLERESP"]._serialized_end = 2019
    _globals["_PIPAD"]._serialized_start = 2022
    _globals["_PIPAD"]._serialized_end = 2293
# @@protoc_insertion_point(module_scope)
