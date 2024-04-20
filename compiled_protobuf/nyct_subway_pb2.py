# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nyct-subway.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import compiled_protobuf.gtfs_realtime_pb2 as gtfs__realtime__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11nyct-subway.proto\x12\x10transit_realtime\x1a\x13gtfs-realtime.proto\"b\n\x15TripReplacementPeriod\x12\x10\n\x08route_id\x18\x01 \x01(\t\x12\x37\n\x12replacement_period\x18\x02 \x01(\x0b\x32\x1b.transit_realtime.TimeRange\"w\n\x0eNyctFeedHeader\x12\x1b\n\x13nyct_subway_version\x18\x01 \x02(\t\x12H\n\x17trip_replacement_period\x18\x02 \x03(\x0b\x32\'.transit_realtime.TripReplacementPeriod\"\xb5\x01\n\x12NyctTripDescriptor\x12\x10\n\x08train_id\x18\x01 \x01(\t\x12\x13\n\x0bis_assigned\x18\x02 \x01(\x08\x12\x41\n\tdirection\x18\x03 \x01(\x0e\x32..transit_realtime.NyctTripDescriptor.Direction\"5\n\tDirection\x12\t\n\x05NORTH\x10\x01\x12\x08\n\x04\x45\x41ST\x10\x02\x12\t\n\x05SOUTH\x10\x03\x12\x08\n\x04WEST\x10\x04\"C\n\x12NyctStopTimeUpdate\x12\x17\n\x0fscheduled_track\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63tual_track\x18\x02 \x01(\t:Y\n\x10nyct_feed_header\x12\x1c.transit_realtime.FeedHeader\x18\xe9\x07 \x01(\x0b\x32 .transit_realtime.NyctFeedHeader:e\n\x14nyct_trip_descriptor\x12 .transit_realtime.TripDescriptor\x18\xe9\x07 \x01(\x0b\x32$.transit_realtime.NyctTripDescriptor:q\n\x15nyct_stop_time_update\x12+.transit_realtime.TripUpdate.StopTimeUpdate\x18\xe9\x07 \x01(\x0b\x32$.transit_realtime.NyctStopTimeUpdateB\x1d\n\x1b\x63om.google.transit.realtime')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nyct_subway_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.google.transit.realtime'
  _globals['_TRIPREPLACEMENTPERIOD']._serialized_start=60
  _globals['_TRIPREPLACEMENTPERIOD']._serialized_end=158
  _globals['_NYCTFEEDHEADER']._serialized_start=160
  _globals['_NYCTFEEDHEADER']._serialized_end=279
  _globals['_NYCTTRIPDESCRIPTOR']._serialized_start=282
  _globals['_NYCTTRIPDESCRIPTOR']._serialized_end=463
  _globals['_NYCTTRIPDESCRIPTOR_DIRECTION']._serialized_start=410
  _globals['_NYCTTRIPDESCRIPTOR_DIRECTION']._serialized_end=463
  _globals['_NYCTSTOPTIMEUPDATE']._serialized_start=465
  _globals['_NYCTSTOPTIMEUPDATE']._serialized_end=532
# @@protoc_insertion_point(module_scope)