from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ArrivalBoardingActivityEnumeration(Enum):
    ALIGHTING = "alighting"
    NO_ALIGHTING = "noAlighting"
    PASS_THRU = "passThru"


class DepartureBoardingActivityEnumeration(Enum):
    BOARDING = "boarding"
    NO_BOARDING = "noBoarding"
    PASS_THRU = "passThru"


@dataclass
class EstimatedTimetableDelivery:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    response_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
        }
    )
    subscription_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "required": True,
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
        }
    )
    version: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )


class FirstOrLastJourneyEnumeration(Enum):
    FIRST_SERVICE_OF_DAY = "firstServiceOfDay"
    OTHER_SERVICE = "otherService"
    LAST_SERVICE_OF_DAY = "lastServiceOfDay"
    UNSPECIFIED = "unspecified"


@dataclass
class FramedVehicleJourneyRefStructure:
    data_frame_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    dated_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )


@dataclass
class IncludedSituationExchangeDelivery:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    response_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
        }
    )
    subscription_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "required": True,
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
        }
    )
    version: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )


@dataclass
class SituationExchangeDelivery:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    response_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
        }
    )
    subscription_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "required": True,
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
        }
    )
    version: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )


class VehicleModesEnumeration(Enum):
    AIR = "air"
    BUS = "bus"
    COACH = "coach"
    FERRY = "ferry"
    METRO = "metro"
    RAIL = "rail"
    TRAM = "tram"
    UNDERGROUND = "underground"


@dataclass
class VehicleMonitoringDelivery:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    response_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
        }
    )
    subscription_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "required": True,
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
        }
    )
    version: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )


class LangValue(Enum):
    AA = "AA"
    AB = "AB"
    AF = "AF"
    AM = "AM"
    AR = "AR"
    AS_VALUE = "AS"
    AY = "AY"
    AZ = "AZ"
    BA = "BA"
    BE = "BE"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BN = "BN"
    BO = "BO"
    BR = "BR"
    CA = "CA"
    CO = "CO"
    CS = "CS"
    CY = "CY"
    DA = "DA"
    DE = "DE"
    DZ = "DZ"
    EL = "EL"
    EN = "EN"
    EO = "EO"
    ES = "ES"
    ET = "ET"
    EU = "EU"
    FA = "FA"
    FI = "FI"
    FJ = "FJ"
    FO = "FO"
    FR = "FR"
    FY = "FY"
    GA = "GA"
    GD = "GD"
    GL = "GL"
    GN = "GN"
    GU = "GU"
    HA = "HA"
    HI = "HI"
    HR = "HR"
    HU = "HU"
    HY = "HY"
    IA = "IA"
    IE = "IE"
    IK = "IK"
    IN_VALUE = "IN"
    IS_VALUE = "IS"
    IT = "IT"
    IW = "IW"
    JA = "JA"
    JI = "JI"
    JW = "JW"
    KA = "KA"
    KK = "KK"
    KL = "KL"
    KM = "KM"
    KN = "KN"
    KO = "KO"
    KS = "KS"
    KU = "KU"
    KY = "KY"
    LA = "LA"
    LN = "LN"
    LO = "LO"
    LT = "LT"
    LV = "LV"
    MG = "MG"
    MI = "MI"
    MK = "MK"
    ML = "ML"
    MN = "MN"
    MO = "MO"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MY = "MY"
    NA = "NA"
    NE = "NE"
    NL = "NL"
    NO = "NO"
    OC = "OC"
    OM = "OM"
    OR_VALUE = "OR"
    PA = "PA"
    PL = "PL"
    PS = "PS"
    PT = "PT"
    QU = "QU"
    RM = "RM"
    RN = "RN"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SD = "SD"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SQ = "SQ"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SU = "SU"
    SV = "SV"
    SW = "SW"
    TA = "TA"
    TE = "TE"
    TG = "TG"
    TH = "TH"
    TI = "TI"
    TK = "TK"
    TL = "TL"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TS = "TS"
    TT = "TT"
    TW = "TW"
    UK = "UK"
    UR = "UR"
    UZ = "UZ"
    VI = "VI"
    VO = "VO"
    WO = "WO"
    XH = "XH"
    YO = "YO"
    ZH = "ZH"
    ZU = "ZU"


class SpaceValue(Enum):
    DEFAULT = "default"
    PRESERVE = "preserve"


@dataclass
class NaturalLanguageString:
    class Meta:
        name = "naturalLanguageString"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    lang: Optional[LangValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class DatedCall:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "required": True,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
        }
    )
    extra_call: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtraCall",
            "type": "Element",
        }
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Element",
        }
    )
    destination_display: List[NaturalLanguageString] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
        }
    )
    aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
        }
    )
    arrival_boarding_activity: Optional[ArrivalBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalBoardingActivity",
            "type": "Element",
        }
    )
    arrival_stop_assignment: Optional["DatedCall.ArrivalStopAssignment"] = field(
        default=None,
        metadata={
            "name": "ArrivalStopAssignment",
            "type": "Element",
        }
    )
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
        }
    )
    departure_boarding_activity: Optional[DepartureBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureBoardingActivity",
            "type": "Element",
        }
    )
    departure_stop_assignment: Optional["DatedCall.DepartureStopAssignment"] = field(
        default=None,
        metadata={
            "name": "DepartureStopAssignment",
            "type": "Element",
        }
    )

    @dataclass
    class ArrivalStopAssignment:
        aimed_quay_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "AimedQuayRef",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class DepartureStopAssignment:
        aimed_quay_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "AimedQuayRef",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class DatedVehicleJourney:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
            "type": "Element",
            "required": True,
        }
    )
    extra_journey: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtraJourney",
            "type": "Element",
        }
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Element",
        }
    )
    vehicle_mode: List[VehicleModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
        }
    )
    published_line_name: List[NaturalLanguageString] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
        }
    )
    external_line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
        }
    )
    branding_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
        }
    )
    via: List["DatedVehicleJourney.Via"] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
        }
    )
    destination_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
        }
    )
    destination_name: List[NaturalLanguageString] = field(
        default_factory=list,
        metadata={
            "name": "DestinationName",
            "type": "Element",
        }
    )
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
        }
    )
    product_category_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductCategoryRef",
            "type": "Element",
        }
    )
    service_feature_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceFeatureRef",
            "type": "Element",
        }
    )
    first_or_last_journey: Optional[FirstOrLastJourneyEnumeration] = field(
        default=None,
        metadata={
            "name": "FirstOrLastJourney",
            "type": "Element",
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
        }
    )
    block_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
        }
    )
    dated_calls: Optional["DatedVehicleJourney.DatedCalls"] = field(
        default=None,
        metadata={
            "name": "DatedCalls",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class DatedCalls:
        dated_call: List[DatedCall] = field(
            default_factory=list,
            metadata={
                "name": "DatedCall",
                "type": "Element",
                "min_occurs": 2,
            }
        )

    @dataclass
    class Via:
        place_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "PlaceRef",
                "type": "Element",
            }
        )
        via_priority: Optional[int] = field(
            default=None,
            metadata={
                "name": "ViaPriority",
                "type": "Element",
            }
        )


@dataclass
class DatedTimetableVersionFrame:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    recorded_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RecordedAtTime",
            "type": "Element",
            "required": True,
        }
    )
    version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionRef",
            "type": "Element",
        }
    )
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "required": True,
        }
    )
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "required": True,
        }
    )
    dated_vehicle_journey: List[DatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourney",
            "type": "Element",
        }
    )


@dataclass
class ProductionTimetableDelivery:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    response_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
        }
    )
    subscription_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "required": True,
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
        }
    )
    dated_timetable_version_frame: List[DatedTimetableVersionFrame] = field(
        default_factory=list,
        metadata={
            "name": "DatedTimetableVersionFrame",
            "type": "Element",
        }
    )
    version: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )


@dataclass
class ServiceDelivery:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    response_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    producer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "required": True,
        }
    )
    response_message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseMessageIdentifier",
            "type": "Element",
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    production_timetable_delivery: List[ProductionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableDelivery",
            "type": "Element",
        }
    )
    
    items: List[str] = field(
        default=list,
        metadata={
            "name": "lines",
            "type": "Element",
        }
    )

    srs_name: str = field(
        default="epsg:4326",
        metadata={
            "name": "srsName",
            "type": "Attribute",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
