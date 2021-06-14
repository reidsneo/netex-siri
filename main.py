import os
import sys
import time
import decimal

import simplejson as json
import pandas as panda
import zmq.green as zmq
from gevent import monkey
monkey.patch_all()
from engineio.async_drivers import gevent
import gevent

import gzip
import itertools
from collections import defaultdict
# import logging

from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from pathlib import Path
from lxml import etree

from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers.xml import XmlSerializer


from flask import Flask, make_response, current_app, render_template, request, abort
from flask_socketio import SocketIO, emit, disconnect
from spyne import Iterable, Integer, Unicode, rpc, Application, Service
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.interface.wsdl.wsdl11 import Wsdl11

from threading import Thread
import multiprocessing
from multiprocessing import Process, Manager, Queue
from gzip import GzipFile
from io import BytesIO
from io import StringIO
import numpy as np
intern = sys.intern

#helper for KV6 Data Pooling Parser
import kv6

#generated using netex-cen NETEX format https://github.com/NeTEx-CEN
from netex.models import *

#generated using netex-cen SIRI format https://github.com/NeTEx-CEN
from siri.models import Siri as sirimod_Siri, ServiceDelivery as sirimod_ServiceDelivery, VehicleMonitoringDelivery as sirimod_VehicleMonitoringDelivery, VehicleActivityStructure as sirimod_VehicleActivityStructure, MonitoredVehicleJourneyStructure as sirimod_MonitoredVehicleJourneyStructure, FramedVehicleJourneyRefStructure as sirimod_FramedVehicleJourneyRefStructure, LocationStructure as sirimod_LocationStructure, MonitoredCallStructure as sirimod_MonitoredCallStructure, OnwardCallsStructure as sirimod_OnwardCallsStructure, OnwardCallStructure as sirimod_OnwardCallStructure, StopTimetableDelivery as sirimod_StopTimetableDelivery, TimetabledStopVisitStructure as sirimod_TimetabledStopVisitStructure, TargetedVehicleJourney as sirimod_TargetedVehicleJourney, FramedVehicleJourneyRefStructure as sirimod_FramedVehicleJourneyRefStructure, TargetedCallStructure as sirimod_TargetedCallStructure

#generated using siri-cen SIRI format https://github.com/SIRI-CEN/SIRI
#this is new version of SIRI standard 2.1 which is constraint against SIRI older versin for NETEX-CEN
from siri.wsdl import ServiceDelivery, LineVersionStructure, DataObjectDelivery, DataObjectsRelStructure, ServiceFrame, LinesInFrameRelStructure, OrganisationsInFrameRelStructure, ResourceFrame, Operator

import threading
import uuid
import zipfile


thread_kv6 = None
thread_kv78turbo = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode='gevent')
tasks = {}

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

zmq_context = zmq.Context()
ids = []
here = Path(__file__).parent
parser = XmlParser(context=XmlContext(), config=ParserConfig(process_xinclude=False, fail_on_unknown_properties=False))
serializer = XmlSerializer(SerializerConfig(pretty_print=True, no_namespace_schema_location=None,xml_declaration=True, encoding="UTF-8",schema_location="siri/xsd/siri-bison-v900.xsd"))


# filename_new = str(here.joinpath("NeTEx_CXX_CXX_202102_new210110181901.xml"))
# filename_baseline = str(here.joinpath("NeTEx_CXX_2021-04-18_baseline_2021006_new.xml"))

#samples = list(map(str, here.joinpath("NeTEx/examples/functions").rglob("*.xml")))
# schema = here.joinpath("NeTEx/xsd/NeTEx_publication.xsd")
# validator = etree.XMLSchema(etree.parse(str(schema)))


def thread_upload_netex(f,task_name):
    filename = secure_filename(f.filename)
    if(".zip" in filename or "netex" in filename):
        foldername = task_name.replace(" ","-")
        if not os.path.exists("upload/"+foldername):
            os.makedirs("upload/"+foldername)
        f.save(os.path.join("upload/"+foldername+"/", filename))
        print(filename+" file uploaded successfully to "+foldername)
        print("extracting zip file")
        with zipfile.ZipFile(os.path.join("upload/"+foldername+"/", filename), 'r') as zip_ref:
            zip_ref.extractall(os.path.join("upload/"+foldername+"/"))
        print("done extract zip file")
        if not os.path.exists("database/"+foldername):
            print("creating database result path")
            os.makedirs("database/"+foldername)
    else:
        print("invalid file! "+filename)


def netex_import_new(filename_new,result_path=""):
    start = time.time()
    print("Processing XML File : "+filename_new)
    print("Processing using : parsing XML mode : NEW")

    data = {}
    RFDatasources = panda.DataFrame(data)
    RFResponsibilitySets = panda.DataFrame(data)
    RFTypesOfValue = panda.DataFrame(data)
    RFOperator = panda.DataFrame(data)
    RFAuthority = panda.DataFrame(data)

    SFRoutePoint = panda.DataFrame(data)
    SFLine = panda.DataFrame(data)
    SFTimingLinks = panda.DataFrame(data)
    SFDestinationDisplays = panda.DataFrame(data)
    SFScheduledStopPoints = panda.DataFrame(data)
    SFJourneyPatterns = panda.DataFrame(data)
    SFTimeDemandTypes = panda.DataFrame(data)
    SFNotices = panda.DataFrame(data)
    SFNoticesAssignments = panda.DataFrame(data)
    SFTimeTableFrame = panda.DataFrame(data)

    print("Chunking the XML file...")
    chunking_timestart = time.time()

    pd = parser.parse(filename_new, PublicationDelivery)
    
    chunking_time = time.time() - chunking_timestart
    mon, sec = divmod(chunking_time, 60)
    hr, mon = divmod(mon, 60)
    chunking_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    print("Chunking XML file done! in "+ chunking_elapsed)

    print("Data Sources parsing....")
    datasources_timestart = time.time()
    for data_source in pd.data_objects.composite_frame[0].frames.resource_frame[0].data_sources.data_source:
        RFDatasources = RFDatasources.append({
            'id':data_source.id,
            'modification':data_source.modification.value,
            'version':data_source.version,
            'name':data_source.name,
            'short_name':data_source.short_name.value,
            'description':data_source.description.value,
            'email':data_source.email
        }, ignore_index=True)
    datasources_time = time.time() - datasources_timestart
    mon, sec = divmod(datasources_time, 60)
    hr, mon = divmod(mon, 60)
    datasources_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    print("Data Sources parsing done! in "+ datasources_elapsed)
    RFDatasources.to_csv(result_path+'RFDatasources', index=False)
    print("Data Sources successfully dumped to database")

    # print("ResponsibilitySets parsing....")
    # responsibility_set_timestart = time.time()
    # for responsibility_set in pd.data_objects.composite_frame[0].frames.resource_frame[0].responsibility_sets.responsibility_set:
    #     RFResponsibilitySets = RFResponsibilitySets.append({
    #         'id':responsibility_set.id,
    #         'modification':responsibility_set.modification.value,
    #         'version':responsibility_set.version,
    #         'name':responsibility_set.name.value,
    #         'roles':responsibility_set.roles
    #     }, ignore_index=True)
    # responsibility_set_time = time.time() - responsibility_set_timestart
    # mon, sec = divmod(responsibility_set_time, 60)
    # hr, mon = divmod(mon, 60)
    # responsibility_set_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("ResponsibilitySets parsing done! in "+ responsibility_set_elapsed)
    # RFResponsibilitySets.to_csv('RFResponsibilitySets', index=False)
    # print("ResponsibilitySets successfully dumped to database")

    # print("TypesOfValue parsing....")
    # type_of_product_category_timestart = time.time()
    # for type_of_product_category in pd.data_objects.composite_frame[0].frames.resource_frame[0].types_of_value.type_of_product_category:
    #     RFTypesOfValue = RFTypesOfValue.append({
    #         'id':type_of_product_category.id,
    #         'modification':type_of_product_category.modification.value,
    #         'version':type_of_product_category.version,
    #         'name':type_of_product_category.name.value
    #     }, ignore_index=True)
    # type_of_product_category_time = time.time() - type_of_product_category_timestart
    # mon, sec = divmod(type_of_product_category_time, 60)
    # hr, mon = divmod(mon, 60)
    # type_of_product_category_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("TypesOfValue parsing done! in "+ type_of_product_category_elapsed)
    # RFTypesOfValue.to_csv('RFTypesOfValue', index=False)
    # print("TypesOfValue successfully dumped to database")


    # print("Operator parsing....")
    # operator_timestart = time.time()
    # for operator in pd.data_objects.composite_frame[0].frames.resource_frame[0].organisations.operator:
    #     RFOperator = RFOperator.append({'id':operator.id,'modification':operator.modification.value,'version':operator.version,'name':operator.name.value,'short_name':operator.short_name,'description':operator.description,'customer_service_contact_details':operator.customer_service_contact_details}, ignore_index=True)
    # operator_time = time.time() - operator_timestart
    # mon, sec = divmod(operator_time, 60)
    # hr, mon = divmod(mon, 60)
    # operator_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("Operator parsing done! in "+ operator_elapsed)
    # RFOperator.to_csv('RFOperator', index=False)
    # print("Operator successfully dumped to database")

    # print("Authority parsing....")
    # authority_timestart = time.time()
    # for authority in pd.data_objects.composite_frame[0].frames.resource_frame[0].organisations.authority:
    #     RFAuthority = RFAuthority.append({
    #         'id':authority.id,
    #         'name':authority.name.value,
    #         'short_name':authority.short_name
    #     }, ignore_index=True)
    # authority_time = time.time() - authority_timestart
    # mon, sec = divmod(authority_time, 60)
    # hr, mon = divmod(mon, 60)
    # authority_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("Authority parsing done! in "+ authority_elapsed)
    # RFAuthority.to_csv('RFAuthority', index=False)
    # print("Authority successfully dumped to database")

    # print("RoutePoint parsing....")
    # route_point_timestart = time.time()
    # for route_point in pd.data_objects.composite_frame[0].frames.service_frame[0].route_points.route_point:
    #     SFRoutePoint = SFRoutePoint.append({
    #         'id':route_point.id,
    #         'modification':route_point.modification.value,
    #         'version':route_point.version,
    #         'location':route_point.location.pos
    #     }, ignore_index=True)    
    # route_point_time = time.time() - route_point_timestart
    # mon, sec = divmod(route_point_time, 60)
    # hr, mon = divmod(mon, 60)
    # route_point_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("RoutePoint parsing done! in "+ route_point_elapsed)
    # SFRoutePoint.to_csv('SFRoutePoint', index=False)
    # print("RoutePoint successfully dumped to database")

    # print("Line parsing....")
    # line_timestart = time.time()
    # for line in pd.data_objects.composite_frame[0].frames.service_frame[0].lines.line:
    #     SFLine = SFLine.append({
    #         'id':line.id,
    #         'modification':line.modification.value,
    #         'version':line.version,
    #         'branding_ref':line.branding_ref,
    #         'name':line.name.value,
    #         'transport_mode':line.transport_mode.value,
    #         'transport_submode':line.transport_submode,
    #         'public_code':line.public_code,
    #         'private_code':line.private_code,
    #         'external_line_ref':line.external_line_ref,
    #         'authority_ref.version':line.authority_ref.version,
    #         'authority_ref.ref':line.authority_ref.ref,
    #         'monitored':line.monitored,
    #         'accessibility_assessment.id':line.accessibility_assessment.id,
    #         'accessibility_assessment.modification':line.accessibility_assessment.modification.value,
    #         'accessibility_assessment.version':line.accessibility_assessment.version,
    #         'accessibility_assessment.mobility_impaired_access':line.accessibility_assessment.mobility_impaired_access.value,
    #         'responsibility_set_ref':line.responsibility_set_ref
    #     }, ignore_index=True)
    # line_time = time.time() - line_timestart
    # mon, sec = divmod(line_time, 60)
    # hr, mon = divmod(mon, 60)
    # line_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("Line parsing done! in "+ line_elapsed)
    # SFLine.to_csv('SFLine', index=False)
    # print("Line successfully dumped to database")

    # print("TimingLinks parsing....")
    # timing_links_timestart = time.time()
    # for timing_link in pd.data_objects.composite_frame[0].frames.service_frame[0].timing_links.timing_link:
    #     SFTimingLinks = SFTimingLinks.append({
    #         'id':timing_link.id,
    #         'Distance':timing_link.distance,
    #         'FromPointRef.ref':timing_link.from_point_ref.ref,
    #         'FromPointRef.version':timing_link.from_point_ref.version,
    #         'ToPointRef.ref':timing_link.to_point_ref.ref,
    #         'ToPointRef.version':timing_link.to_point_ref.version
    #     }, ignore_index=True)
    # timing_links_time = time.time() - timing_links_timestart
    # mon, sec = divmod(timing_links_time, 60)
    # hr, mon = divmod(mon, 60)
    # timing_links_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("TimingLinks parsing done! in "+ timing_links_elapsed)
    # SFTimingLinks.to_csv('SFTimingLinks', index=False)
    # print("TimingLinks successfully dumped to database")

    # print("Destination Displays parsing....")
    # destination_displays_timestart = time.time()
    # for destination_display in pd.data_objects.composite_frame[0].frames.service_frame[0].destination_displays.destination_display:
    #     SFDestinationDisplays = SFDestinationDisplays.append({
    #         'id':destination_display.id,
    #         'modification':destination_display.modification.value,
    #         'version':destination_display.version,
    #         'name':destination_display.name.value,
    #         'side_text':destination_display.side_text,
    #         'front_text':destination_display.front_text,
    #         'private_code':destination_display.private_code,
    #         'presentation':destination_display.presentation,
    #         'vias':destination_display.vias,
    #         'variants':destination_display.variants
    #     }, ignore_index=True)
    # destination_displays_time = time.time() - destination_displays_timestart
    # mon, sec = divmod(destination_displays_time, 60)
    # hr, mon = divmod(mon, 60)
    # destination_displays_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("Destination Displays parsing done! in "+ destination_displays_elapsed)
    # SFDestinationDisplays.to_csv('SFDestinationDisplays', index=False)
    # print("Destination Displays successfully dumped to database")

    # print("ScheduledStopPoints parsing....")
    # scheduledstoppoints_timestart = time.time()
    # for scheduled_stop_point in pd.data_objects.composite_frame[0].frames.service_frame[0].scheduled_stop_points.scheduled_stop_point:
    #     SFScheduledStopPoints = SFScheduledStopPoints.append({
    #         'id':scheduled_stop_point.id,
    #         'modification':scheduled_stop_point.modification.value,
    #         'version':scheduled_stop_point.version,
    #         'name':scheduled_stop_point.name.value,
    #         'location':scheduled_stop_point.location,
    #         'projections':scheduled_stop_point.projections,
    #         'point_projection.id':scheduled_stop_point.projections.point_projection.id,
    #         'point_projection.modification':scheduled_stop_point.projections.point_projection.modification.value,
    #         'point_projection.version':scheduled_stop_point.projections.point_projection.version,
    #         'point_projection.project_to_point_ref.name_of_ref_class':scheduled_stop_point.projections.point_projection.project_to_point_ref.name_of_ref_class,
    #         'point_projection.project_to_point_ref.version':scheduled_stop_point.projections.point_projection.project_to_point_ref.version,
    #         'point_projection.project_to_point_ref.ref':scheduled_stop_point.projections.point_projection.project_to_point_ref.ref,
    #         'stop_areas':scheduled_stop_point.stop_areas,
    #         'tariff_zones':scheduled_stop_point.tariff_zones,
    #         'private_code':scheduled_stop_point.private_code,
    #         'for_alighting':scheduled_stop_point.for_alighting,
    #         'for_boarding':scheduled_stop_point.for_boarding
    #     }, ignore_index=True)
    # scheduledstoppoints_time = time.time() - scheduledstoppoints_timestart
    # mon, sec = divmod(scheduledstoppoints_time, 60)
    # hr, mon = divmod(mon, 60)
    # scheduledstoppoints_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("ScheduledStopPoints parsing done! in "+ scheduledstoppoints_elapsed)
    # SFScheduledStopPoints.to_csv('SFScheduledStopPoints', index=False)
    # print("ScheduledStopPoints successfully dumped to database")

    # print("JourneyPatterns parsing....")
    # journeypatterns_timestart = time.time()
    # for service_journey_pattern in pd.data_objects.composite_frame[0].frames.service_frame[0].journey_patterns.service_journey_pattern:
    #     SFJourneyPatterns = SFJourneyPatterns.append({
    #         'id':service_journey_pattern.id,
    #         'modification':service_journey_pattern.modification.value,
    #         'version':service_journey_pattern.version,
    #         'name':service_journey_pattern.name,
    #         'route_ref.ref':service_journey_pattern.route_ref.ref,
    #         'route_ref.version':service_journey_pattern.route_ref.version,
    #         'direction_type':service_journey_pattern.direction_type,
    #         'destination_display_ref.ref':service_journey_pattern.destination_display_ref.ref,
    #         'destination_display_ref.version':service_journey_pattern.destination_display_ref.version,
    #         #'points_in_sequence.stop_point':service_journey_pattern.points_in_sequence.stop_point_in_journey_pattern,
    #         #'points_in_sequence.timing_point':service_journey_pattern.points_in_sequence.timing_point_in_journey_pattern,            
    #         'points_in_sequence':service_journey_pattern.points_in_sequence
    #     }, ignore_index=True)
    # journeypatterns_time = time.time() - journeypatterns_timestart
    # mon, sec = divmod(journeypatterns_time, 60)
    # hr, mon = divmod(mon, 60)
    # journeypatterns_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("JourneyPatterns parsing done! in "+  journeypatterns_elapsed)
    # SFJourneyPatterns.to_csv('SFJourneyPatterns', index=False)
    # print("JourneyPatterns successfully dumped to database")

    # print("TimeDemandTypes parsing....")
    # timedemandtype_timestart = time.time()
    # for time_demand_type in pd.data_objects.composite_frame[0].frames.service_frame[0].time_demand_types.time_demand_type:
    #     SFTimeDemandTypes = SFTimeDemandTypes.append({
    #         'id':time_demand_type.id,
    #         'modification':time_demand_type.modification.value,
    #         'version':time_demand_type.version,
    #         'name':time_demand_type.name,
    #         'run_times':time_demand_type.run_times.journey_run_time
    #         }, ignore_index=True)
    # timedemandtype_time = time.time() - timedemandtype_timestart
    # mon, sec = divmod(timedemandtype_time, 60)
    # hr, mon = divmod(mon, 60)
    # timedemandtype_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("TimeDemandTypes parsing done! in "+  timedemandtype_elapsed)
    # SFTimeDemandTypes.to_csv('SFTimeDemandTypes', index=False)
    # print("TimeDemandTypes successfully dumped to database")

    # print("Notice parsing....")
    # notices_timestart = time.time()
    # for notice in pd.data_objects.composite_frame[0].frames.service_frame[0].notices.notice:
    #     SFNotices = SFNotices.append({
    #         'id':notice.id,
    #         'modification':notice.modification.value,
    #         'version':notice.version,
    #         'name':notice.name,
    #         'text':notice.text.value
    #         }, ignore_index=True)
    # notices_time = time.time() - notices_timestart
    # mon, sec = divmod(notices_time, 60)
    # hr, mon = divmod(mon, 60)
    # notices_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("Notice parsing done! in "+  notices_elapsed)
    # SFNotices.to_csv('SFNotices', index=False)
    # print("Notice successfully dumped to database")

    # print("Notice Assignments parsing....")
    # noticesassignments_timestart = time.time()
    # for notice_assignment in pd.data_objects.composite_frame[0].frames.service_frame[0].notice_assignments.notice_assignment:
    #     SFNoticesAssignments = SFNoticesAssignments.append({
    #         'id':notice_assignment.id,
    #         'modification':notice_assignment.modification.value,
    #         'version':notice_assignment.version,
    #         'notice_ref.ref':notice_assignment.notice_ref.ref,
    #         'notice_ref.version':notice_assignment.notice_ref.version,
    #         'noticed_object_ref.ref':notice_assignment.noticed_object_ref.ref,
    #         'noticed_object_ref.namerefclass':notice_assignment.noticed_object_ref.name_of_ref_class,
    #         'noticed_object_ref.version':notice_assignment.noticed_object_ref.version,
    #         'order':notice_assignment.order
    #     }, ignore_index=True)  
    # noticesassignments_time = time.time() - noticesassignments_timestart
    # mon, sec = divmod(noticesassignments_time, 60)
    # hr, mon = divmod(mon, 60)
    # noticesassignments_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("Notice Assignments parsing done! in "+  noticesassignments_elapsed)
    # SFNoticesAssignments.to_csv('SFNoticesAssignments', index=False)
    # print("Notice Assignments successfully dumped to database")

    # print("Timetables parsing....")
    # timetables_timestart = time.time()
    # for timetable_frame in pd.data_objects.composite_frame[0].frames.timetable_frame:
    #     SFTimeTableFrame = SFTimeTableFrame.append({
    #         'id':timetable_frame.id,
    #         'modification':timetable_frame.modification.value,
    #         'version':timetable_frame.version,
    #         'type_of_frame_ref':timetable_frame.type_of_frame_ref,
    #         'monitored':timetable_frame.monitored,
    #         'content_validity_conditions':timetable_frame.content_validity_conditions,
    #         'operator_view.ref':timetable_frame.operator_view.operator_ref.ref,
    #         'operator_view.version':timetable_frame.operator_view.operator_ref.version,
    #         'vehicle_journeys.service_journey':timetable_frame.vehicle_journeys.service_journey,
    #         'vehicle_journeys.deadrun':timetable_frame.vehicle_journeys.dead_run
    #         }, ignore_index=True)
    # timetables_time = time.time() - timetables_timestart
    # mon, sec = divmod(timetables_time, 60)
    # hr, mon = divmod(mon, 60)
    # timetables_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("Timetables parsing done! in "+  timetables_elapsed)
    # SFTimeTableFrame.to_csv('SFTimeTableFrame', index=False)
    # print("Timetables successfully dumped to database")



if( len(sys.argv) == 2 and sys.argv[1]=="new"):
    netex_import_new(filename_new)
elif( len(sys.argv) == 2 and sys.argv[1]=="baseline"):
    print("Processing XML File : "+filename_baseline)
    print("Processing using : parsing XML mode : BASELINE")
    data = {}
    RFDatasources = panda.DataFrame(data)
    RFResponsibilitySets = panda.DataFrame(data)
    RFTypesOfValue = panda.DataFrame(data)
    RFOperator = panda.DataFrame(data)
    RFAuthority = panda.DataFrame(data)

    SFRoutePoint = panda.DataFrame(data)
    SFLine = panda.DataFrame(data)
    SFTimingLinks = panda.DataFrame(data)
    SFDestinationDisplays = panda.DataFrame(data)
    SFScheduledStopPoints = panda.DataFrame(data)
    SFJourneyPatterns = panda.DataFrame(data)
    SFTimeDemandTypes = panda.DataFrame(data)
    SFNotices = panda.DataFrame(data)
    SFNoticesAssignments = panda.DataFrame(data)
    SFTimeTableFrame = panda.DataFrame(data)

    print("Chunking the XML file...")
    chunking_timestart = time.time()

    pd = parser.parse(filename_baseline, PublicationDelivery)
    
    chunking_time = time.time() - chunking_timestart
    mon, sec = divmod(chunking_time, 60)
    hr, mon = divmod(mon, 60)
    chunking_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    print("Chunking XML file done! in "+ chunking_elapsed)

    print("Baseline DataSources parsing....")
    datasources_timestart = time.time()
    for data_source in pd.data_objects.composite_frame[0].frames.resource_frame[0].data_sources.data_source:
        RFDatasources = RFDatasources.append({
            'id':data_source.id,
            'modification':data_source.modification.value,
            'version':data_source.version,
            'name':data_source.name.value,
            'short_name':data_source.short_name,
            'description':data_source.description.value,
            'email':data_source.email
        }, ignore_index=True)
    datasources_time = time.time() - datasources_timestart
    mon, sec = divmod(datasources_time, 60)
    hr, mon = divmod(mon, 60)
    datasources_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    print("Baseline DataSources parsing done! in "+ datasources_elapsed)
    RFDatasources.to_csv('RFDatasources_baseline', index=False)
    print("Baseline DataSources successfully dumped to database")

    print("Baseline ResponsibilitySets parsing....")
    responsibility_set_timestart = time.time()
    for responsibility_set in pd.data_objects.composite_frame[0].frames.resource_frame[0].responsibility_sets.responsibility_set:
        RFResponsibilitySets = RFResponsibilitySets.append({
            'id':responsibility_set.id,
            'modification':responsibility_set.modification.value,
            'version':responsibility_set.version,
            'name':responsibility_set.name.value,
            'roles':responsibility_set.roles.responsibility_role_assignment
        }, ignore_index=True)
    responsibility_set_time = time.time() - responsibility_set_timestart
    mon, sec = divmod(responsibility_set_time, 60)
    hr, mon = divmod(mon, 60)
    responsibility_set_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    print("Baseline ResponsibilitySets parsing done! in "+ responsibility_set_elapsed)
    RFResponsibilitySets.to_csv('RFResponsibilitySets_baseline', index=False)
    print("Baseline ResponsibilitySets successfully dumped to database")

    # print("Baseline ScheduledStopPoints parsing....")
    # for scheduled_stop_point in pd.data_objects.composite_frame[0].frames.service_frame[0].scheduled_stop_points.scheduled_stop_point:
    #     SFScheduledStopPoints = SFScheduledStopPoints.append({
    #         'id':scheduled_stop_point.id.replace("ScheduledStopPoint","SP").replace("CXX","cxx"),
    #         'modification':scheduled_stop_point.modification.value,
    #         'version':scheduled_stop_point.version,
    #         'name':scheduled_stop_point.name.value,
    #         'location':scheduled_stop_point.location.pos,
    #         'projections':scheduled_stop_point.projections,
    #         'point_projection.id':scheduled_stop_point.projections.point_projection.id,
    #         'point_projection.modification':scheduled_stop_point.projections.point_projection.modification.value,
    #         'point_projection.version':scheduled_stop_point.projections.point_projection.version,
    #         'point_projection.project_to_point_ref.name_of_ref_class':scheduled_stop_point.projections.point_projection.project_to_point_ref.name_of_ref_class,
    #         'point_projection.project_to_point_ref.version':scheduled_stop_point.projections.point_projection.project_to_point_ref.version,
    #         'point_projection.project_to_point_ref.ref':scheduled_stop_point.projections.point_projection.project_to_point_ref.ref,
    #         'stop_areas':scheduled_stop_point.stop_areas,
    #         'tariff_zones':scheduled_stop_point.tariff_zones,
    #         'private_code':scheduled_stop_point.private_code,
    #         'for_alighting':scheduled_stop_point.for_alighting,
    #         'for_boarding':scheduled_stop_point.for_boarding
    #     }, ignore_index=True)
    # scheduledstoppoints_end = time.time()
    # scheduledstoppoints_time = scheduledstoppoints_end - start
    # mon, sec = divmod(scheduledstoppoints_time, 60)
    # hr, mon = divmod(mon, 60)
    # scheduledstoppoints_elapsed = "%d:%02d:%02d" % (hr, mon, sec)
    # print("Baseline ScheduledStopPoints parsing done! in "+ scheduledstoppoints_elapsed)
    # SFScheduledStopPoints.to_csv('SFScheduledStopPoints_baseline', index=False)
    # print("Baseline ScheduledStopPoints successfully dumped to database")

else :
    start = time.time()
    print("Processing data using : load database")
    RFDatasources = panda.read_csv('RFDatasources')
    RFDatasources_baseline = panda.read_csv('RFDatasources_baseline')
    RFResponsibilitySets = panda.read_csv('RFResponsibilitySets')    
    RFResponsibilitySets_baseline = panda.read_csv('RFResponsibilitySets_baseline')
    RFTypesOfValue = panda.read_csv('RFTypesOfValue')
    RFOperator = panda.read_csv('RFOperator')
    RFAuthority = panda.read_csv('RFAuthority')

    SFRoutePoint = panda.read_csv('SFRoutePoint')
    SFLine = panda.read_csv('SFLine')
    SFTimingLinks = panda.read_csv('SFTimingLinks')
    SFDestinationDisplays = panda.read_csv('SFDestinationDisplays')
    SFScheduledStopPoints = panda.read_csv('SFScheduledStopPoints')
    SFScheduledStopPoints_baseline = panda.read_csv('SFScheduledStopPoints_baseline')
    SFJourneyPatterns = panda.read_csv('SFJourneyPatterns')
    SFTimeDemandTypes = panda.read_csv('SFTimeDemandTypes')
    SFNotices = panda.read_csv('SFNotices')
    SFNoticesAssignments = panda.read_csv('SFNoticesAssignments')
    SFTimeTableFrame = panda.read_csv('SFTimeTableFrame')
    print("Finish using : load database mode")
    
    
    
    print("Processing data of new + baseline")
    SFScheduledStopPoints_combine = panda.concat([SFScheduledStopPoints, SFScheduledStopPoints_baseline], axis=0)
    print("Processing data of new + baseline is done!")
    
    stoppoints_dicts = SFScheduledStopPoints_combine.to_dict("records")
    #deprecated StopPointsFlat=SFScheduledStopPoints_combine.set_index('id')[['name']].values.tolist()
    #deprecated StopPoint = dict(zip(SFScheduledStopPoints_combine['id'],StopPointsFlat))

    #print(stoppoints_dicts['cxx:SP:35220010'])
   # stoppoints_list = []
    # for stoppoints_dict in stoppoints_dicts:
    #     stoppoints_list.append(stoppoints_dict)
    # print(stoppoints_list)
    # newline_cols = ['id', 'name', 'short_name', 'modification', 'version']
    # newline = RFOperator; #.loc[SFLine['id']=="cxx:LN:N067" or SFLine['id']=="cxx:LN:N068"]
    # newline = newline[newline_cols]
    # line_dicts = newline.to_dict('records')
    # operator_list = []
    # for line_dict in line_dicts:
    #     operator_list.append(Operator(id=line_dict['name'],version=line_dict['version'],name=line_dict['name'],short_name=line_dict['short_name']))

    # sd = ServiceDelivery(
    #     response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #     data_object_delivery=[
    #         DataObjectDelivery(
    #             response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #             data_objects = DataObjectsRelStructure(
    #                 resource_frame = ResourceFrame(
    #                     organisations = OrganisationsInFrameRelStructure(
    #                         operator = operator_list
    #                     )
    #                 )
    #             )
    #         )
    #     ]
    # )
    # xml = serializer.render(sd, ns_map={"siri": "http://www.siri.org.uk/siri", None:"http://www.netex.org.uk/netex"})
    # print(xml)


    # vehicleinfo_dicts = transit_vehicleinfo.to_dict('records')
    # vehicleinfo_list = []
    # for vehicleinfo_dict in vehicleinfo_dicts:
    #     vehicleinfo_list.append(
    #         sirimod_VehicleActivityStructure(
    #             recorded_at_time = vehicleinfo_dict['timestamp'],
    #             valid_until_time = "",
    #             monitored_vehicle_journey = sirimod_MonitoredVehicleJourneyStructure(
    #                 line_ref = vehicleinfo_dict['lineplanningnumber'],
    #                 direction_ref = "S",
    #                 framed_vehicle_journey_ref = sirimod_FramedVehicleJourneyRefStructure(
    #                     data_frame_ref = vehicleinfo_dict['timestamp'],
    #                     dated_vehicle_journey_ref = "11514020",
    #                 ),
    #                 published_line_name = "Parchester - Rumrill - Carlson",
    #                 operator_ref = vehicleinfo_dict['dataownercode'],
    #                 origin_ref = "56780",
    #                 origin_name = "Richmond Pkwy Transit Center (Park & Ride)",
    #                 destination_ref = "57286",
    #                 destination_name = "El Cerrito Plaza BART",
    #                 monitored = True,
    #                 in_congestion = "",
    #                 vehicle_location = sirimod_LocationStructure(
    #                     longitude = vehicleinfo_dict['rd_x'],
    #                     latitude = vehicleinfo_dict['rd_y']
    #                 ),
    #                 bearing = "51.0000000000",
    #                 occupancy = "seatsAvailable",
    #                 vehicle_ref = "1201",
    #                 monitored_call = sirimod_MonitoredCallStructure(
    #                     stop_point_ref = strClean(vehicleinfo_dict['userstopcode']),
    #                     stop_point_name = getStopPoint(vehicleinfo_dict['userstopcode'],"name"),
    #                     vehicle_location_at_stop = "", #LocationStructure
    #                     vehicle_at_stop = "", #bool
    #                     aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                     expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                     aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                     expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                 ),
    #                 onward_calls = sirimod_OnwardCallsStructure(
    #                     onward_call = [
    #                         sirimod_OnwardCallStructure(
    #                             stop_point_ref = "54066",
    #                             stop_point_name = "Rumrill Blvd & 19th St",
    #                             aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                             expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                             aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                             expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                         ),
    #                         sirimod_OnwardCallStructure(
    #                             stop_point_ref = "55892",
    #                             stop_point_name = "Rumrill Blvd & 17th St",
    #                             aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                             expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                             aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                             expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                         ),
    #                     ]
    #                 )
    #             )
    #         )
    #     )

    vehicle_xml = sirimod_Siri(
        service_delivery= sirimod_ServiceDelivery(
            response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            status = True,
            stop_timetable_delivery = sirimod_StopTimetableDelivery(
                response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                subscription_ref = "511SFBay",
                timetabled_stop_visit = [
                    sirimod_TimetabledStopVisitStructure(
                        recorded_at_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        monitoring_ref = "57788", #userstopcode
                        targeted_vehicle_journey = sirimod_TargetedVehicleJourney(
                            line_ref = "800",
                            direction_ref = "E",
                            framed_vehicle_journey_ref = sirimod_FramedVehicleJourneyRefStructure(
                                data_frame_ref = datetime.now().strftime('%Y-%m-%d'),
                                dated_vehicle_journey_ref = "10367020"
                            ),
                            published_line_name = "800",
                            operator_ref = "AC",
                            origin_ref = "51418",
                            origin_name = "24th St & Mission St",
                            destination_ref = "51673",
                            destination_name = "Richmond BART",
                            vehicle_journey_name = "RICHMOND BART ALLNIGHTER VIA DWNTWN OAKLAND",
                            targeted_call = sirimod_TargetedCallStructure(
                                visit_number = "1",
                                aimed_arrival_time =  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            )
                        )
                    )
                ]
            )
        )
    )
    nonsiri_serializer = XmlSerializer(SerializerConfig(pretty_print=True))
    xml = nonsiri_serializer.render(vehicle_xml, ns_map={None:"http://www.siri.org.uk/siri"})

end = time.time()
totaltime = end - start
mon, sec = divmod(totaltime, 60)
hr, mon = divmod(mon, 60)
elapsed = "%d:%02d:%02d" % (hr, mon, sec)
print("Processing XML File : Finished in " + elapsed)

def getStopPoint(stop_id,field):
    if(str(stop_id).find("nan") == -1):
        stop_id = "cxx:SP:"+str(stop_id).replace(".0","")
        return next(item for item in stoppoints_dicts if item["id"] == stop_id)[field]
    else:
        return "Delayed"


def strClean(string):
    return str(string).replace(".0","")

def merge(shared_key, *iterables):
    result = defaultdict(dict)
    for dictionary in itertools.chain.from_iterable(iterables):
        result[dictionary[shared_key]].update(dictionary)
    for dictionary in result.values():
        dictionary.pop(shared_key)
    return result

@socketio.event
def worker_kv6():
    socket = zmq_context.socket(zmq.SUB)
    socket.connect('tcp://pubsub.besteffort.ndovloket.nl:7658')
    socket.setsockopt_string(zmq.SUBSCRIBE, "/CXX/KV6posinfo")
    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)
    gevent.sleep()
    received = 0
    kv6_merge = panda.DataFrame({})
    kv6_old = panda.DataFrame({})
    kv6_new = panda.DataFrame({})
    print("Running KV6 Poller...")
    while True:
        message = socket.recv()
        try:
            received += 1
            #print("kv6 data counter : "+ str(received))
            message = gzip.decompress(message)
            # print("================================================START===================================")
            #print(kv6.asList(message))
            kv6_list = kv6.asList(message)
            kv6_new = panda.DataFrame(kv6_list)
            try:
                kv6_new['vehiclenumber'] = kv6_new['vehiclenumber'].astype(str)
                if (received == 2):
                    #print("|-only executed once!")
                    kv6_merge = kv6_new
                    kv6_merge.drop(index=kv6_merge[kv6_merge['vehiclenumber'] == 'nan'].index, inplace=True)
                    kv6_merge.sort_values('timestamp', ascending=False).sort_index()      
                    kv6_merge['vehiclenumber'] = kv6_merge['vehiclenumber'].astype(str).replace('\.0*$','', regex=True)
                    kv6_old = kv6_new
                else :
                    kv6_old['vehiclenumber'] = kv6_old['vehiclenumber'].astype(str)
                    kv6_merge = kv6_old.set_index('vehiclenumber').combine_first(kv6_new.set_index('vehiclenumber')).reset_index()
                    kv6_merge.drop(index=kv6_merge[kv6_merge['vehiclenumber'] == 'nan'].index, inplace=True)
                    kv6_merge.drop_duplicates(subset=['vehiclenumber'], keep='last', inplace=True)
                    kv6_merge.sort_values('timestamp', ascending=False).sort_index()
                    kv6_merge['vehiclenumber'] = kv6_merge['vehiclenumber'].astype(str).replace('\.0*$','', regex=True)
                    kv6_old = kv6_merge
                #print("   |-old contains : " +str(len(kv6_old.to_dict('records'))))
                #print("   |-total contains : " +str(len(kv6_merge.to_dict('records'))))
                kv6_merge['vehiclenumber'] = kv6_merge['vehiclenumber'].astype(str)
                kv6_merge.drop(index=kv6_merge[kv6_merge['vehiclenumber'] == 'nan'].index, inplace=True)
                kv6_merge.drop_duplicates(subset=['vehiclenumber'], keep='last', inplace=True)
                kv6_merge.sort_values('timestamp', ascending=False).sort_index()
                kv6_merge['vehiclenumber'] = kv6_merge['vehiclenumber'].astype(str).str.replace('\.0*$','', regex=True)
                socketio.emit('kv6_status', {'data': str(len(kv6_merge.to_dict('records')))}, broadcast=True)
                socketio.emit('kv6_data', {'records': json.dumps(json.loads(kv6_merge.to_json(orient = "records"))) }, broadcast=True)
                export_csv = panda.DataFrame({})
                export_csv = kv6_merge.reindex(columns=['vehiclenumber','messagetype','journeynumber','lineplanningnumber','userstopcode','blockcode','distancesincelastuserstop','numberofcoaches','operatingday','passagesequencenumber','punctuality','reinforcementnumber','source','wheelchairaccessible','dataownercode','rd_x','rd_y','timestamp'])
                export_csv.to_csv('KV6_VehiclePosInfo', index=False)
            except:
                kv6_new.to_csv('KV6_VehiclePosInfo_error', index=False)
                print("Error occured, but skipped")
                pass
        except OSError: pass
        message = str(message,'utf-8-sig')
        gevent.sleep()

def storecurrect(newrow): 	    
    newrow['ExpectedArrivalTime'] = totimestamp(newrow['OperationDate'], newrow['ExpectedArrivalTime'], newrow)
    newrow['ExpectedDepartureTime'] = totimestamp(newrow['OperationDate'], newrow['ExpectedDepartureTime'], newrow)
    newrow['TargetArrivalTime'] = totimestamp(newrow['OperationDate'], newrow['TargetArrivalTime'], newrow)
    newrow['TargetDepartureTime'] = totimestamp(newrow['OperationDate'], newrow['TargetDepartureTime'], newrow)
    date,time = newrow['LastUpdateTimeStamp'].split('T')
    newrow['LastUpdateTimeStamp'] = totimestamp(date,time[:-6],None)

    id = '_'.join([newrow['DataOwnerCode'], str(newrow['LocalServiceLevelCode']), newrow['LinePlanningNumber'], str(newrow['JourneyNumber']), str(newrow['FortifyOrderNumber'])])
    if id in journey_store and int(newrow['UserStopOrderNumber']) in journey_store[id]['Stops']:
        row = journey_store[id]['Stops'][int(newrow['UserStopOrderNumber'])]
        if row['TripStopStatus'] == 'LINESTOPCANCEL':
            newrow['TripStopStatus'] = 'LINESTOPCANCEL'
            setDelayIncrease(row,newrow)
        
        if newrow['WheelChairAccessible'] == 'UNKNOWN':
            newrow['WheelChairAccessible'] = row['WheelChairAccessible'] # Because of agencies not implementing the accessiblity tag in KV6, we're better off ignoring UKNOWNS unfortunately
            row.update(newrow)
        else:
            row = newrow
            line_id = row['DataOwnerCode'] + '_' + row['LinePlanningNumber'] + '_' + str(row['LineDirection'])
            linemeta_id = row['DataOwnerCode'] + '_' + row['LinePlanningNumber']
            destinationmeta_id = row['DataOwnerCode'] + '_' + row['DestinationCode']
            pass_id = '_'.join([row['UserStopCode'], str(row['UserStopOrderNumber'])])

            for x in ['JourneyPatternCode', 'JourneyNumber', 'FortifyOrderNumber', 'UserStopOrderNumber', 'NumberOfCoaches', 'LocalServiceLevelCode', 'LineDirection']:
                try:
                    if x in row and row[x] is not None and row[x] != 'UNKNOWN':
                        row[x] = int(row[x])
                    else:
                        del(row[x])
                except:
                    pass
            row['IsTimingStop'] = (row['IsTimingStop'] == '1')

            if row['TimingPointCode'] not in tpc_store:
                    tpc_store[row['TimingPointCode']] = {'Passes' : {id: row}, 'GeneralMessages' : {}}
            else:
                    tpc_store[row['TimingPointCode']]['Passes'][id] = row

            if row['TimingPointCode'] in tpc_meta:
                stopareacode = tpc_meta[row['TimingPointCode']]['StopAreaCode']
                if stopareacode != None:
                    if stopareacode not in stopareacode_store:
                            stopareacode_store[stopareacode] = [row['TimingPointCode']]
                    elif row['TimingPointCode'] not in stopareacode_store[stopareacode]:
                            stopareacode_store[stopareacode].append(row['TimingPointCode'])
    
            if line_id not in line_store:
                line_store[line_id] = {'Network': {}, 'Actuals': {}, 'Line' : {}}
                line_store[line_id]['Line'] = {'DataOwnerCode' : row['DataOwnerCode'], 'LineDirection' : row['LineDirection'], 'LinePlanningNumber' : row['LinePlanningNumber'], 'DestinationCode' : row['DestinationCode']}
            if row['JourneyPatternCode'] not in line_store[line_id]['Network']:
                line_store[line_id]['Network'][row['JourneyPatternCode']] = {}
            if row['UserStopOrderNumber'] not in line_store[line_id]['Network'][row['JourneyPatternCode']]:
                line_store[line_id]['Network'][row['JourneyPatternCode']][row['UserStopOrderNumber']] = {
                    'TimingPointCode': row['TimingPointCode'],
                    'IsTimingStop': row['IsTimingStop'],
                    'UserStopOrderNumber':row['UserStopOrderNumber']
                    }
            if id not in journey_store:
                journey_store[id] = {'Stops' : {row['UserStopOrderNumber']: row}}
                if row['WheelChairAccessible'] != 'UNKNOWN':
                    line_store[line_id]['Line']['LineWheelchairAccessible'] = row['WheelChairAccessible']
            else:
                journey_store[id]['Stops'][row['UserStopOrderNumber']] = row

            if row['TripStopStatus'] in set(['ARRIVED', 'PASSED']): # , 'DRIVING']): Driving alleen nemen als kleinste waarde uit lijn, gegeven dat er geen ARRIVED/PASSED is
                for key in journey_store[id]['Stops'].keys(): #delete previous stops from journey
                    if key < int(row['UserStopOrderNumber']) - 1:
                        del(journey_store[id]['Stops'][key])
                        
                    if row['JourneyStopType'] == 'LAST': #delete journey
                        if id in line_store[line_id]['Actuals']:
                            del(line_store[line_id]['Actuals'][id])
                        else:
                            line_store[line_id]['Actuals'][id] = row
            elif row['TripStopStatus'] == 'DRIVING':   #replace a passed stop with the next stop
                previousStopOrder = int(row['UserStopOrderNumber']) - 1
                if previousStopOrder in journey_store[id]['Stops'] and journey_store[id]['Stops'][previousStopOrder]['TripStopStatus'] == 'PASSED':
                    line_store[line_id]['Actuals'][id] = row
            elif row['TripStopStatus'] == 'PLANNED' and row['TimingPointDataOwnerCode'] == 'ALGEMEEN' and id not in line_store[line_id]['Actuals'] and int(row['UserStopOrderNumber']) == 1: #add planned journeys
                line_store[line_id]['Actuals'][id] = row
            elif (row['TripStopStatus'] == 'UNKNOWN' or row['TripStopStatus'] == 'CANCEL') and id in line_store[line_id]['Actuals']: #Delete canceled or non live journeys
                del(line_store[line_id]['Actuals'][id])

def totimestamp(operationdate, timestamp, row):
    hours, minutes, seconds = timestamp.split(':')   
    years, months, days = operationdate.split('-')
    if hours == 0 and minutes == 0 and seconds == 0:
        return int(0)
    hours = int(hours)
    if hours >= 48:
        print(row)
    if hours >= 24:
        deltadays  = hours / 24
        hours = hours % 24
        return int((datetime(int(years), int(months), int(days), hours, int(minutes), int(seconds)) + timedelta(days = deltadays)).strftime("%s"))
    else:
        #print();
        #return int(datetime(int(years), int(months), int(days), hours, int(minutes), int(seconds)).strftime("%s"))
        return int(datetime(int(years), int(months), int(days), hours, int(minutes), int(seconds)).timestamp());

def recvPackage(content):
    #print(content.decode('UTF-8'))
    data = {}
    a_list = []
    for line in content.decode('UTF-8').split('\r\n')[:-1]:
        if line[0] == '\\':
                # control characters
            if line[1] == 'G':
                label, name, subscription, path, endian, enc, res1, timestamp, _ = line[2:].split('|')
            elif line[1] == 'T':
                type = line[2:].split('|')[1]
            elif line[1] == 'L':
                keys = line[2:].split('|')
        else:
            row = {}
            values = line.split('|')
            for key in keys:
                for value in values:
                    if value == '\\0':
                        row[key] = None
                    else:          
                        row[key] = value
                    values.remove(value)
                    break
            for x in ['ReasonType', 'AdviceType', 'AdviceContent','SubAdviceType','MessageType','ReasonContent','OperatorCode', 'SubReasonType', 'MessageContent']:
                if x in row and row[x] is None:
                    del(row[x])
            if type == 'DATEDPASSTIME':
                if 'SideCode' in row and row['SideCode'] in ['-','Left','Right']:
                    del(row['SideCode'])
                elif 'SideCode' in row:
                    row['SideCode'] = intern(row['SideCode'])
                if row['TripStopStatus'] != 'UNKNOWN' and row['TripStopStatus'] != 'PLANNED': #Keeps status of the dataowners supplying us data
                    last_updatestore['DataOwner'][row['DataOwnerCode']] = row['LastUpdateTimeStamp']
                    last_updatestore['Subscription'][subscription] = row['LastUpdateTimeStamp']
                elif row['DataOwnerCode'] not in last_updatestore['DataOwner']:
                    last_updatestore['DataOwner'][row['DataOwnerCode']] = 'ERROR'
                if subscription not in last_updatestore['Subscription']:
                    last_updatestore['Subscription'][subscription] = 'ERROR'
                if row['JourneyStopType'] != 'INFOPOINT':
                    storecurrect(row)
            elif type == 'GENERALMESSAGEUPDATE':
                print('GENERAL MESSAGE UPDATE');
                storemessage(row)
                print(content);
            elif type == 'GENERALMESSAGEDELETE':
                print('GENERAL MESSAGE DELETE');
                deletemessage(row)
                print(content);
            else:
                print('UNKNOWN TYPE : !!!!!' +  type);
                print(content);
            a_list.append(row)
            
    KV78Data = panda.DataFrame(a_list)
    KV78Data.to_csv('KV78_StopPointMonitoring',index=False, mode='a', header=False)
    #print("done")


tpc_store = {}
stopareacode_store = {}
line_store = {}
journey_store = {}
last_updatestore = {'DataOwner' : {}, 'Subscription' : {}}
generalmessagestore = {}

def worker_kv78turbo():
    socket = zmq_context.socket(zmq.SUB)
    socket.connect('tcp://pubsub.besteffort.ndovloket.nl:7817')
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)
    gevent.sleep()
    received = 0
    a= []
    count = 0

    print("Running KV78Turbo Poller...")
    while True:
        count = count + 1
        multipart = socket.recv_multipart()
        address = multipart[0]
        contents = b"".join(multipart[1:]);
        contents = GzipFile('','r',0,BytesIO(contents)).read()
        recvPackage(contents);
        gevent.sleep()
#
    #    multipart = socket.recv_multipart()
    #    address = multipart[0]
    #    contents = b"".join(multipart[1:]);
    #    try:
    #        contents = [GzipFile('','r',0,BytesIO(contents)).read()]
    #    except:
    #        raise print('NOT ', contents)
    #    for i in contents:
    #         a.append(i)
    #         count = count + 1
    #         np.savetxt("kv8rough.csv", a, delimiter="", fmt='%s')
    
    #    data = panda.read_csv(r'kv8rough.csv', error_bad_lines=False, header=None)
    #    data1 = data.iloc[:,0]
    #    data2 = data1.str.rsplit("|", expand=True)
    #    data3= data2.drop([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,
    #                    32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,
    #                    56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74], 1)
    #    data4= data3.values.tolist()
    #    labels = ['OperationDate', 'LinePlanningNumber'	,'JourneyNumber',	'FortifyOrderNumber',	'UserStopOrderNumber',	'UserStopCode',	'LocalServiceLevelCode',
    #            'JourneyPatternCode',	'LineDirection',	'LastUpdateTimeStamp',	'DestinationCode',	'IsTimingStop',	'ExpectedArrivalTime',	'ExpectedDepartureTime',
    #            'TripStopStatus',	'MessageContent',	'MessageType',	'SideCode',	'NumberOfCoaches',	'WheelChairAccessible',	'OperatorCode',	'ReasonType',
    #            'SubReasonType',	'ReasonContent',	'AdviceType', 'SubAdviceType',	'AdviceContent',	'TimingPointDataOwnerCode',
    #            'TimingPointCode',	'JourneyStopType',	'TargetArrivalTime',	'TargetDepartureTime',	'RecordedArrivalTime',
    #            'RecordedDepartureTime',	'DetectedUserStopCode',	'DistanceSinceDetectedUserStop',	'Detected_RD_X',	'Detected_RD_Y',
    #            'VehicleNumber',	'BlockCode',	'LineVeTagNumber',	'VejoJourneyNumber',	'VehicleJourneyType',	'VejoBlockNumCode',
    #            'JourneyModificationType',	'VejoDepartureTime',	'VejoArrivalTime',	'VejoTripStatusType',	'ExtraJourney',
    #            'CancelledJourney',	'ShowCancelledTrip',	'ShowFlexibleTrip',	'Monitored',	'MonitoringError',	'ExtraCall',	'CancelledCall',
    #            'ShowCancelledStop',	'AimedQuayRef',	'ExpectedQuayRef',	'ActualQuayRef',	'Occupancy',	'LineDestIcon',	'LineDestColor',
    #            'LineDestTextColor\r\nSYNTUS']
    #    d = []
    #    row = -1
    #    column =0
    #    for i in range(len(data4)):
    #        e=[]
    #        for j in range(len(data4[i])):
    #            if data4[i][j] != None:
    #                e.append(data4[i][j])
    #                column = column + 1
    #                if column > 63:
    #                    d.append(e)
    #                    e = []
    #                    column = 0
    #                    my_df = panda.DataFrame(d)
                          
    #        column  = 0
    #    my_df.to_csv('kv8finaldata.csv', index=False, header=False)
#
        # try:
        #     received += 1
        #     print("data counter : "+ str(received))
        #     message = gzip.decompress(message).toString();
        #     print(message.split('\r\n'))
        #     #recvPackage(message)
        # except OSError: pass
       #contents = str(contents,'utf-8-sig')
       #gevent.sleep()


@socketio.on('my event')
def test_messageev(message):
    emit('my_response', {'data': message['data']})

@socketio.on('my broadcast event')
def test_messagebc(message):
    emit('my_response', {'data': message['data']}, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('my_response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def my_event(message):
    #session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data']})


@socketio.event
def my_broadcast_event(message):
    #session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data']},
         broadcast=True)

@app.route('/', methods=['GET'])
def home():
    return render_template('sitemap.html', async_mode=socketio.async_mode)


@app.route('/resourceframe/datasources', methods=['GET'])
def datasources():
    response = make_response(
        json.dumps(
            json.loads(
                RFDatasources.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/resourceframe/responsibilitysets', methods=['GET'])
def responsibilitysets():
    response = make_response(
        json.dumps(
            json.loads(
                RFResponsibilitySets.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/resourceframe/typesofvalue', methods=['GET'])
def typesofvalue():
    response = make_response(
        json.dumps(
            json.loads(
                RFTypesOfValue.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/resourceframe/operator', methods=['GET'])
def operator():
    response = make_response(
        json.dumps(
            json.loads(
                RFOperator.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/resourceframe/authority', methods=['GET'])
def authority():
    response = make_response(
        json.dumps(
            json.loads(
                RFAuthority.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response



@app.route('/serviceframe/routepoints', methods=['GET'])
def routepoint():
    response = make_response(
        json.dumps(
            json.loads(
                SFRoutePoint.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/lines', methods=['GET'])
def line():
    response = make_response(
        json.dumps(
            json.loads(
                SFLine.to_json(orient = "records")
                #fixme presentation
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/timinglinks', methods=['GET'])
def timinglink():
    response = make_response(
        json.dumps(
            json.loads(
                SFTimingLinks.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/destinationdisplays', methods=['GET'])
def destinationdisplay():
    response = make_response(
        json.dumps(
            json.loads(
                SFDestinationDisplays.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/scheduledstoppoint', methods=['GET'])
def scheduledstoppoint():
    response = make_response(
        json.dumps(
            json.loads(
                SFScheduledStopPoints.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/servicejourneypattern', methods=['GET'])
def servicejourneypattern():
    response = make_response(
        json.dumps(
            json.loads(
                SFJourneyPatterns.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/timedemandtype', methods=['GET'])
def timedemandtype():
    response = make_response(
        json.dumps(
            json.loads(
                SFTimeDemandTypes.to_json(orient = "records") #.head(10)
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/notices', methods=['GET'])
def notices():
    response = make_response(
        json.dumps(
            json.loads(
                SFNotices.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/noticeassignments', methods=['GET'])
def noticeassignments():
    response = make_response(
        json.dumps(
            json.loads(
                SFNoticesAssignments.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/serviceframe/timetables', methods=['GET'])
def timetables():
    response = make_response(
        json.dumps(
            json.loads(
                SFTimeTableFrame.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/resourceframe/baseline/datasources', methods=['GET'])
def baseline_datasources():
    response = make_response(
        json.dumps(
            json.loads(
                RFDatasources_baseline.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/resourceframe/baseline/responsibilitysets', methods=['GET'])
def baseline_responsibilitysets():
    response = make_response(
        json.dumps(
            json.loads(
                RFResponsibilitySets_baseline.to_json(orient = "records")
            )
        )
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/transit/operators', methods=['GET'])
def transit_operators():
    operator_id = request.args.get('operator_id')
    if operator_id is None:
        transit_operators = RFOperator
    else:
        transit_operators = RFOperator.loc[RFOperator['id']==operator_id]

    newline_cols = ['id', 'name', 'short_name', 'modification', 'version']
    transit_operators = transit_operators[newline_cols]
    operators_dicts = transit_operators.to_dict('records')
    operator_list = []
    for operator_dict in operators_dicts:
        operator_list.append(Operator(id=operator_dict['id'],version=operator_dict['version'],name=operator_dict['name'],short_name=operator_dict['short_name']))

    sd = ServiceDelivery(
        response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        data_object_delivery=[
            DataObjectDelivery(
                response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                data_objects = DataObjectsRelStructure(
                   resource_frame = ResourceFrame(
                        organisations = OrganisationsInFrameRelStructure(
                            operator = operator_list
                        )
                    )
                )
            )
        ]
    )
    xml = serializer.render(sd, ns_map={"siri": "http://www.siri.org.uk/siri", None:"http://www.netex.org.uk/netex"})
    response = make_response(
        xml
    )
    response.headers['Content-Type'] = 'text/xml'
    return response

@app.route('/transit/line', methods=['GET'])
def transit_line():
    line = request.args.get('line')
    if line is None:
        transit_line = SFLine
    else:
        transit_line = SFLine.loc[SFLine['id']==line]

    newline_cols = ['name', 'transport_mode']
    transit_line = transit_line[newline_cols]
    line_dicts = transit_line.to_dict('records')
    line_list = []
    for line_dict in line_dicts:
        line_list.append(LineVersionStructure(name=line_dict['name'],transport_mode=line_dict['transport_mode']))

    sd = ServiceDelivery(
        response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        data_object_delivery=[
            DataObjectDelivery(
                response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                data_objects = DataObjectsRelStructure(
                    service_frame = ServiceFrame(
                        lines = LinesInFrameRelStructure(
                            line = line_list
                        )
                    )
                )
            )
        ]
    )
    xml = serializer.render(sd, ns_map={"siri": "http://www.siri.org.uk/siri", None:"http://www.netex.org.uk/netex"})
    response = make_response(
        xml
    )
    response.headers['Content-Type'] = 'text/xml'
    return response

@app.route('/transit/VehicleMonitoring', methods=['GET'])
def kv6postinfo():
    KV6postinfo = panda.read_csv('KV6_VehiclePosInfo', dtype={
        'id': str,
        'vehiclenumber': str,
        'userstopcode':str,
        'punctuality':str,
        'rd_x':str,
        'rd_y':str,
        'passagesequencenumber':str
        })
    KV6postinfo['vehiclenumber'] = KV6postinfo['vehiclenumber'].astype(str)
    
    agency = request.args.get('agency')
    vehicleid = request.args.get('vehicleid')
    #print(vehicleid)
    if ((agency is not None) and (vehicleid is None)):
        transit_vehicleinfo = KV6postinfo.loc[KV6postinfo['dataownercode']==agency]
        #print("agency mode")
    elif ((vehicleid is not None) and (agency is None)):
        transit_vehicleinfo = KV6postinfo.loc[KV6postinfo['vehiclenumber']==vehicleid]
        # print("vehicleid mode")
        #print(transit_vehicleinfo)
    elif ((vehicleid is not None) and (agency is not None)):
        transit_vehicleinfo = KV6postinfo.loc[KV6postinfo['dataownercode']==agency]
        transit_vehicleinfo = transit_vehicleinfo.loc[KV6postinfo['vehiclenumber']==vehicleid]
        #print("both mode")
    else:
        transit_vehicleinfo = KV6postinfo
        #print("none mode")

    transit_vehicleinfo = transit_vehicleinfo.sort_values("timestamp", ascending = False)
    vehicleinfo_dicts = transit_vehicleinfo.to_dict('records')
    vehicleinfo_list = []
    for vehicleinfo_dict in vehicleinfo_dicts:
        vehicleinfo_list.append(
            sirimod_VehicleActivityStructure(
                recorded_at_time = vehicleinfo_dict['timestamp'],
                valid_until_time = "",
                monitored_vehicle_journey = sirimod_MonitoredVehicleJourneyStructure(
                    line_ref = vehicleinfo_dict['lineplanningnumber'],
                    direction_ref = "S",
                    framed_vehicle_journey_ref = sirimod_FramedVehicleJourneyRefStructure(
                        data_frame_ref = vehicleinfo_dict['timestamp'],
                        dated_vehicle_journey_ref = "11514020",
                    ),
                    published_line_name = "Parchester - Rumrill - Carlson",
                    operator_ref = vehicleinfo_dict['dataownercode'],
                    origin_ref = "56780",
                    origin_name = "Richmond Pkwy Transit Center (Park & Ride)",
                    destination_ref = strClean(vehicleinfo_dict['userstopcode']), #"57286",
                    destination_name = getStopPoint(vehicleinfo_dict['userstopcode'],"name"), #"El Cerrito Plaza BART",
                    monitored = True,
                    in_congestion = "",
                    vehicle_location = sirimod_LocationStructure(
                        longitude = vehicleinfo_dict['rd_x'],
                        latitude = vehicleinfo_dict['rd_y']
                    ),
                    bearing = vehicleinfo_dict['punctuality'],
                    occupancy = "seatsAvailable",
                    vehicle_ref = "1201",
                    monitored_call = sirimod_MonitoredCallStructure(
                        stop_point_ref = strClean(vehicleinfo_dict['userstopcode']),
                        stop_point_name = getStopPoint(vehicleinfo_dict['userstopcode'],"name"),
                        vehicle_location_at_stop = "", #LocationStructure
                        vehicle_at_stop = "", #bool
                        aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    ),
                    onward_calls = sirimod_OnwardCallsStructure(
                        onward_call = [
                            sirimod_OnwardCallStructure(
                                stop_point_ref = "54066",
                                stop_point_name = "Rumrill Blvd & 19th St",
                                aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            ),
                            sirimod_OnwardCallStructure(
                                stop_point_ref = "55892",
                                stop_point_name = "Rumrill Blvd & 17th St",
                                aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            ),
                        ]
                    )
                )
            )
        )

    vehicle_xml = sirimod_Siri(
        service_delivery= sirimod_ServiceDelivery(
            response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            status = True,
            producer_ref ="AC",
            vehicle_monitoring_delivery = sirimod_VehicleMonitoringDelivery(
                response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                vehicle_activity = vehicleinfo_list
            )
        )
    )
    nonsiri_serializer = XmlSerializer(SerializerConfig(pretty_print=True))
    xml = nonsiri_serializer.render(vehicle_xml, ns_map={None:"http://www.siri.org.uk/siri"})
    #print(xml)

    # newline_cols = ['id', 'name', 'short_name', 'modification', 'version']
    # newline = RFOperator; #.loc[SFLine['id']=="cxx:LN:N067" or SFLine['id']=="cxx:LN:N068"]
    # newline = newline[newline_cols]
    # line_dicts = newline.to_dict('records')
    # operator_list = []
    # for line_dict in line_dicts:
    #     operator_list.append(Operator(id=line_dict['name'],version=line_dict['version'],name=line_dict['name'],short_name=line_dict['short_name']))

    response = make_response(
        xml
    )
    response.headers['Content-Type'] = 'text/xml'
    return response


@app.route('/transit/stoptimetable', methods=['GET'])
def stoptimetable():
    KV6postinfo = panda.read_csv('KV6_VehiclePosInfo', dtype={
        'id': str,
        'vehiclenumber': str,
        'userstopcode':str,
        'punctuality':str,
        'rd_x':str,
        'rd_y':str,
        'passagesequencenumber':str
        })
    KV6postinfo['vehiclenumber'] = KV6postinfo['vehiclenumber'].astype(str)
    
    agency = request.args.get('agency')
    vehicleid = request.args.get('vehicleid')
    #print(vehicleid)
    if ((agency is not None) and (vehicleid is None)):
        transit_vehicleinfo = KV6postinfo.loc[KV6postinfo['dataownercode']==agency]
        #print("agency mode")
    elif ((vehicleid is not None) and (agency is None)):
        print(KV6postinfo['vehiclenumber'].astype(str))
        transit_vehicleinfo = KV6postinfo.loc[KV6postinfo['vehiclenumber']==vehicleid]
        # print("vehicleid mode")
        #print(transit_vehicleinfo)
    elif ((vehicleid is not None) and (agency is not None)):
        transit_vehicleinfo = KV6postinfo.loc[KV6postinfo['dataownercode']==agency]
        transit_vehicleinfo = transit_vehicleinfo.loc[KV6postinfo['vehiclenumber']==vehicleid]
        #print("both mode")
    else:
        transit_vehicleinfo = KV6postinfo
        #print("none mode")

    transit_vehicleinfo = transit_vehicleinfo.sort_values("timestamp", ascending = False)

    # print(stoppoints_dicts['cxx:SP:53111291'])
    # for vehicleinfo_dict in stoppoints_dicts:
    #     print(vehicleinfo_dict)    
    vehicleinfo_dicts = transit_vehicleinfo.to_dict('records')
    vehicleinfo_list = []
    for vehicleinfo_dict in vehicleinfo_dicts:
        vehicleinfo_list.append(
            sirimod_VehicleActivityStructure(
                recorded_at_time = vehicleinfo_dict['timestamp'],
                valid_until_time = "",
                monitored_vehicle_journey = sirimod_MonitoredVehicleJourneyStructure(
                    line_ref = vehicleinfo_dict['lineplanningnumber'],
                    direction_ref = "S",
                    framed_vehicle_journey_ref = sirimod_FramedVehicleJourneyRefStructure(
                        data_frame_ref = vehicleinfo_dict['timestamp'],
                        dated_vehicle_journey_ref = "11514020",
                    ),
                    published_line_name = "Parchester - Rumrill - Carlson",
                    operator_ref = vehicleinfo_dict['dataownercode'],
                    origin_ref = "56780",
                    origin_name = "Richmond Pkwy Transit Center (Park & Ride)",
                    destination_ref = "57286",
                    destination_name = "El Cerrito Plaza BART",
                    monitored = True,
                    in_congestion = "",
                    vehicle_location = sirimod_LocationStructure(
                        longitude = vehicleinfo_dict['rd_x'],
                        latitude = vehicleinfo_dict['rd_y']
                    ),
                    bearing = "51.0000000000",
                    occupancy = "seatsAvailable",
                    vehicle_ref = "1201",
                    monitored_call = sirimod_MonitoredCallStructure(
                        stop_point_ref = strClean(vehicleinfo_dict['userstopcode']),
                        stop_point_name = getStopPoint(vehicleinfo_dict['userstopcode'],"name"),
                        vehicle_location_at_stop = "", #LocationStructure
                        vehicle_at_stop = "", #bool
                        aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    ),
                    onward_calls = sirimod_OnwardCallsStructure(
                        onward_call = [
                            sirimod_OnwardCallStructure(
                                stop_point_ref = "54066",
                                stop_point_name = "Rumrill Blvd & 19th St",
                                aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            ),
                            sirimod_OnwardCallStructure(
                                stop_point_ref = "55892",
                                stop_point_name = "Rumrill Blvd & 17th St",
                                aimed_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                expected_arrival_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                aimed_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                expected_departure_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            ),
                        ]
                    )
                )
            )
        )

    vehicle_xml = sirimod_Siri(
        service_delivery= sirimod_ServiceDelivery(
            response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            status = True,
            producer_ref ="AC",
            vehicle_monitoring_delivery = sirimod_VehicleMonitoringDelivery(
                response_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                vehicle_activity = vehicleinfo_list
            )
        )
    )
    nonsiri_serializer = XmlSerializer(SerializerConfig(pretty_print=True))
    xml = nonsiri_serializer.render(vehicle_xml, ns_map={None:"http://www.siri.org.uk/siri"})
    #print(xml)

    # newline_cols = ['id', 'name', 'short_name', 'modification', 'version']
    # newline = RFOperator; #.loc[SFLine['id']=="cxx:LN:N067" or SFLine['id']=="cxx:LN:N068"]
    # newline = newline[newline_cols]
    # line_dicts = newline.to_dict('records')
    # operator_list = []
    # for line_dict in line_dicts:
    #     operator_list.append(Operator(id=line_dict['name'],version=line_dict['version'],name=line_dict['name'],short_name=line_dict['short_name']))

    response = make_response(
        xml
    )
    response.headers['Content-Type'] = 'text/xml'
    return response
    
@app.route('/upload', methods = ['POST'])
def task_upload_netex():
   if request.method == 'POST':
       task_name = request.form.get('name')
       f = request.files['file']
       thread = Thread(target=thread_upload_netex, args=(f,task_name,))
       thread.name = "Thread-import-"+str(task_name)
       thread.daemon = True
       thread.start()
       return json.dumps({'thread_name': str(thread.name),'started': True})

@app.route("/foo", defaults={'duration': 5})
@app.route("/foo/<int:duration>")
def threaduration(duration):
    thread = Thread(target=threaded_task, args=(duration,))
    thread.name = "Thread-foo-"+str(duration)
    thread.daemon = True
    thread.start()
    return json.dumps({'thread_name': str(thread.name),
                    'started': True})

def threaded_task(duration):
    for i in range(duration):
        print("Working... {}/{}".format(i + 1, duration))
        time.sleep(1)

@app.route("/import")
def importnetex():
    task_name = request.args.get('name')
    filename = request.args.get('filename')
    path_xml = os.path.join("upload/"+task_name+"/"+filename.replace(".zip",""))
    path_dest = os.path.join("database/"+task_name+"/")
    thread = Process(name="Thread-importxml-"+task_name, target=netex_import_new,args=(path_xml,path_dest))
    #thread.daemon = True
    thread.start()
    return json.dumps({'thread_name': str(thread.name),
                    'started': True})


@app.route("/threadlist")
def threadlist():
    thread_lists = []
    for thread in threading.enumerate():
        thread_lists.append(thread.name)
        print(thread.name)
    return '<br>'.join(map(str, thread_lists))



@app.route("/processlist")
def processlist():
    process_lists = []
    for p in multiprocessing.active_children():
        process_lists.append(p.name)
        # if p.name == "foo":
        #     p.terminate()
    return '<br>'.join(map(str, process_lists))


if __name__ == "__main__":
    if thread_kv6 is None:
        thread_kv6 = Thread(name="Thread-KV6-Worker", target=worker_kv6)
        thread_kv6.daemon = True
        thread_kv6.start()

    if thread_kv78turbo is None:
        thread_kv78turbo = Thread(name = "Thread-KV78-Worker",target=worker_kv78turbo)
        thread_kv78turbo.daemon = True
        thread_kv78turbo.start()
        
    print("Server has been started")
    socketio.run(app,host='0.0.0.0',port=50000, debug=False)