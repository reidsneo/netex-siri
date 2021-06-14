from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod, XmlTime

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class AccessFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    LIFT = "lift"
    WHEELCHAIR_LIFT = "wheelchairLift"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    AUTOMATIC_RAMP = "automaticRamp"
    STEPS = "steps"
    STAIRS = "stairs"
    SLIDING_STEP = "slidingStep"
    SHUTTLE = "shuttle"
    NARROW_ENTRANCE = "narrowEntrance"
    BARRIER = "barrier"
    LOW_FLOOR_ACCESS = "lowFloorAccess"
    VALIDATOR = "validator"
    LEVEL_FLOOR_ACCESS = "levelFloorAccess"


class BisonTypeOfCompositeFrame(Enum):
    BISON_TYPE_OF_FRAME_NL_TT_BASELINE = "BISON:TypeOfFrame:NL_TT_BASELINE"
    BISON_TYPE_OF_FRAME_NL_TT_DELTA = "BISON:TypeOfFrame:NL_TT_DELTA"
    BISON_TYPE_OF_FRAME_NL_CODESPACES = "BISON:TypeOfFrame:NL_CODESPACES"
    BISON_TYPE_OF_FRAME_NL_BISON_ENUMS = "BISON:TypeOfFrame:NL_BISON_ENUMS"
    BISON_TYPE_OF_FRAME_NL_DOVA_LISTS = "BISON:TypeOfFrame:NL_DOVA_LISTS"
    BISON_TYPE_OF_FRAME_NL_VEHICLES = "BISON:TypeOfFrame:NL_VEHICLES"


class BisonTypeOfGeneralFrame(Enum):
    BISON_TYPE_OF_FRAME_NL_AUTHORITY_LIST = "BISON:TypeOfFrame:NL_AuthorityList"
    BISON_TYPE_OF_FRAME_NL_TARIFF_ZONE_LIST = "BISON:TypeOfFrame:NL_TariffZoneList"
    BISON_TYPE_OF_FRAME_NL_NETWORK_LIST = "BISON:TypeOfFrame:NL_NetworkList"
    BISON_TYPE_OF_FRAME_NL_TYPE_OF_EQUIPMENT_VALUES = "BISON:TypeOfFrame:NL_TypeOfEquipmentValues"
    BISON_TYPE_OF_FRAME_NL_TYPE_OF_ACTIVATION_VALUES = "BISON:TypeOfFrame:NL_TypeOfActivationValues"
    BISON_TYPE_OF_FRAME_NL_TYPE_OF_SERVICE_VALUES = "BISON:TypeOfFrame:NL_TypeOfServiceValues"
    BISON_TYPE_OF_FRAME_NL_TECHNICAL_ENUMERATIONS = "BISON:TypeOfFrame:NL_TechnicalEnumerations"
    BISON_TYPE_OF_FRAME_NL_VEH_METADATA = "BISON:TypeOfFrame:NL_VEH_METADATA"
    BISON_TYPE_OF_FRAME_NL_VEH_DATA = "BISON:TypeOfFrame:NL_VEH_DATA"


class BisonTypeOfProfileFrame(Enum):
    BISON_TYPE_OF_FRAME_NL_TT_RESOURCE = "BISON:TypeOfFrame:NL_TT_RESOURCE"
    BISON_TYPE_OF_FRAME_NL_TT_INFRA = "BISON:TypeOfFrame:NL_TT_INFRA"
    BISON_TYPE_OF_FRAME_NL_TT_SERVICE = "BISON:TypeOfFrame:NL_TT_SERVICE"
    BISON_TYPE_OF_FRAME_NL_TT_TIMETABLE = "BISON:TypeOfFrame:NL_TT_TIMETABLE"
    BISON_TYPE_OF_FRAME_NL_TT_CALENDAR = "BISON:TypeOfFrame:NL_TT_CALENDAR"
    BISON_TYPE_OF_FRAME_NL_TT_VEHICLE = "BISON:TypeOfFrame:NL_TT_VEHICLE"


class BusSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    LOCAL_BUS = "localBus"
    REGIONAL_BUS = "regionalBus"
    EXPRESS_BUS = "expressBus"
    NIGHT_BUS = "nightBus"
    POST_BUS = "postBus"
    SPECIAL_NEEDS_BUS = "specialNeedsBus"
    MOBILITY_BUS = "mobilityBus"
    MOBILITY_BUS_FOR_REGISTERED_DISABLED = "mobilityBusForRegisteredDisabled"
    SIGHTSEEING_BUS = "sightseeingBus"
    SHUTTLE_BUS = "shuttleBus"
    HIGH_FREQUENCY_BUS = "highFrequencyBus"
    DEDICATED_LANE_BUS = "dedicatedLaneBus"
    SCHOOL_BUS = "schoolBus"
    SCHOOL_AND_PUBLIC_SERVICE_BUS = "schoolAndPublicServiceBus"
    RAIL_REPLACEMENT_BUS = "railReplacementBus"
    DEMAND_AND_RESPONSE_BUS = "demandAndResponseBus"
    AIRPORT_LINK_BUS = "airportLinkBus"


class CoachSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INTERNATIONAL_COACH = "internationalCoach"
    NATIONAL_COACH = "nationalCoach"
    SHUTTLE_COACH = "shuttleCoach"
    REGIONAL_COACH = "regionalCoach"
    SPECIAL_COACH = "specialCoach"
    SCHOOL_COACH = "schoolCoach"
    SIGHTSEEING_COACH = "sightseeingCoach"
    TOURIST_COACH = "touristCoach"
    COMMUTER_COACH = "commuterCoach"


class CrowdingEnumeration(Enum):
    VERY_QUIET = "veryQuiet"
    QUIET = "quiet"
    NORMAL = "normal"
    BUSY = "busy"
    VERY_BUSY = "veryBusy"


class DayEventEnumeration(Enum):
    ANY_DAY = "anyDay"
    NORMAL_DAY = "normalDay"
    MARKET_DAY = "marketDay"
    MATCH_DAY = "matchDay"
    EVENT_DAY = "eventDay"


class DayOfWeekEnumeration(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    EVERYDAY = "Everyday"
    WEEKDAYS = "Weekdays"
    WEEKEND = "Weekend"
    NONE_VALUE = "none"


class DeadRunTypeEnumeration(Enum):
    GARAGE_RUN_OUT = "garageRunOut"
    GARAGE_RUN_IN = "garageRunIn"
    TURNING_MANOEUVRE = "turningManoeuvre"
    OTHER = "other"


class DeliveryVariantTypeEnumeration(Enum):
    ANY = "any"
    PRINTED = "printed"
    TEXT_TO_SPEECH = "textToSpeech"
    RECORDED_ANNOUNCEMENT = "recordedAnnouncement"
    WEB = "web"
    MOBILE = "mobile"
    OTHER = "other"


class DirectionTypeEnumeration(Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anticlockwise"


class DynamicAdvertisementEnumeration(Enum):
    ALWAYS = "always"
    NEVER = "never"
    ONLY_IF_ORDERED = "onlyIfOrdered"
    ONLY_IF_SIGNED_ON = "onlyIfSignedOn"


@dataclass
class ExternalObjectRefStructure:
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class FareClassEnumeration(Enum):
    UNKNOWN = "unknown"
    FIRST_CLASS = "firstClass"
    SECOND_CLASS = "secondClass"
    THIRD_CLASS = "thirdClass"
    PREFERENTE = "preferente"
    PREMIUM_CLASS = "premiumClass"
    BUSINESS_CLASS = "businessClass"
    STANDARD_CLASS = "standardClass"
    TURISTA = "turista"
    ECONOMY_CLASS = "economyClass"
    ANY = "any"


class GroupOfLinesTypeEnumeration(Enum):
    MARKETING = "marketing"
    ADMINISTRATIVE = "administrative"
    SCHEDULING = "scheduling"
    CONTROL = "control"
    TARIFF = "tariff"
    OTHER = "other"


class HolidayTypeEnumeration(Enum):
    ANY_DAY = "AnyDay"
    WORKING_DAY = "WorkingDay"
    SCHOOL_DAY = "SchoolDay"
    NOT_HOLIDAY = "NotHoliday"
    NOT_WORKING_DAY = "NotWorkingDay"
    NOT_SCHOOL_DAY = "NotSchoolDay"
    ANY_HOLIDAY = "AnyHoliday"
    LOCAL_HOLIDAY = "LocalHoliday"
    REGIONAL_HOLIDAY = "RegionalHoliday"
    NATIONAL_HOLIDAY = "NationalHoliday"
    HOLIDAY_DISPLACEMENT_DAY = "HolidayDisplacementDay"
    EVE_OF_HOLIDAY = "EveOfHoliday"


@dataclass
class KeyListStructure:
    key_value: List["KeyListStructure.KeyValue"] = field(
        default_factory=list,
        metadata={
            "name": "KeyValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )

    @dataclass
    class KeyValue:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
        value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )


class LimitationStatusEnumeration(Enum):
    TRUE_VALUE = "true"
    FALSE_VALUE = "false"
    UNKNOWN = "unknown"
    PARTIAL = "partial"


@dataclass
class LocationStructure:
    pos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


class MetroSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    METRO = "metro"
    TUBE = "tube"
    URBAN_RAILWAY = "urbanRailway"


class MobilityFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    LOW_FLOOR = "lowFloor"
    STEP_FREE_ACCESS = "stepFreeAccess"
    SUITABLE_FOR_WHEELCHAIRS = "suitableForWheelchairs"
    SUITABLE_FOR_HEAVILIY_DISABLED = "suitableForHeaviliyDisabled"
    BOARDING_ASSISTANCE = "boardingAssistance"
    ONBOARD_ASSISTANCE = "onboardAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    TACTILE_PLATFORM_EDGES = "tactilePlatformEdges"
    TACTILE_GUIDING_STRIPS = "tactileGuidingStrips"


class ModificationEnumeration(Enum):
    NEW = "new"
    DELETE = "delete"
    REVISE = "revise"
    UNCHANGED = "unchanged"
    DELTA = "delta"


@dataclass
class MultilingualString:
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


class PassengerCommsFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    FREE_WIFI = "freeWifi"
    PUBLIC_WIFI = "publicWifi"
    POWER_SUPPLY_SOCKETS = "powerSupplySockets"
    TELEPHONE = "telephone"
    AUDIO_ENTERTAINMENT = "audioEntertainment"
    VIDEO_ENTERTAINMENT = "videoEntertainment"
    BUSINESS_SERVICES = "businessServices"
    INTERNET = "internet"
    POST_OFFICE = "postOffice"
    POST_BOX = "postBox"


@dataclass
class PrivateCodeStructure:
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class RailSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    LOCAL = "local"
    HIGH_SPEED_RAIL = "highSpeedRail"
    SUBURBAN_RAILWAY = "suburbanRailway"
    REGIONAL_RAIL = "regionalRail"
    INTERREGIONAL_RAIL = "interregionalRail"
    LONG_DISTANCE = "longDistance"
    INTERNATIONAL = "international"
    SLEEPER_RAIL_SERVICE = "sleeperRailService"
    NIGHT_RAIL = "nightRail"
    CAR_TRANSPORT_RAIL_SERVICE = "carTransportRailService"
    TOURIST_RAILWAY = "touristRailway"
    AIRPORT_LINK_RAIL = "airportLinkRail"
    RAIL_SHUTTLE = "railShuttle"
    REPLACEMENT_RAIL_SERVICE = "replacementRailService"
    SPECIAL_TRAIN = "specialTrain"
    CROSS_COUNTRY_RAIL = "crossCountryRail"
    RACK_AND_PINION_RAILWAY = "rackAndPinionRailway"


class SanitaryFacilityEnumeration(Enum):
    NONE_VALUE = "none"
    TOILET = "toilet"
    WHEEL_CHAIR_ACCESS_TOILET = "wheelChairAccessToilet"
    SHOWER = "shower"
    WASHING_AND_CHANGE_FACILITIES = "washingAndChangeFacilities"
    BABY_CHANGE = "babyChange"
    WHEELCHAIR_BABY_CHANGE = "wheelchairBabyChange"
    SHOE_SHINER = "shoeShiner"
    OTHER = "other"


class SeasonEnumeration(Enum):
    SPRING = "Spring"
    SUMMER = "Summer"
    AUTUMN = "Autumn"
    WINTER = "Winter"
    PERENNIALLY = "Perennially"


@dataclass
class SimpleObjectRefStructure:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SimpleObjectStructure:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class StakeholderRoleTypeEnumeration(Enum):
    PLANNING = "Planning"
    OPERATION = "Operation"
    CONTROL = "Control"
    RESERVATION = "Reservation"
    ENTITY_LEGAL_OWNERSHIP = "EntityLegalOwnership"
    FARE_MANAGEMENT = "FareManagement"
    SECURITY_MANAGEMENT = "SecurityManagement"
    DATA_REGISTRAR = "DataRegistrar"
    OTHER = "Other"


class StatusEnumeration(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    OTHER = "other"


class TicketingServiceFacilityEnumeration(Enum):
    PURCHASE = "purchase"
    COLLECTION = "collection"
    CARD_TOP_UP = "cardTopUp"
    RESERVATIONS = "reservations"
    EXCHANGE = "exchange"
    REFUND = "refund"
    RENEWAL = "renewal"
    EXCESS_FARES = "excessFares"
    OTHER = "other"
    ALL = "all"


class TideEnumeration(Enum):
    HIGH_TIDE = "HighTide"
    LOW_TIDE = "LowTide"
    NEAP_TIDE = "NeapTide"
    ALL_TIDES = "AllTides"


class TramSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    CITY_TRAM = "cityTram"
    LOCAL_TRAM = "localTram"
    REGIONAL_TRAM = "regionalTram"
    SIGHTSEEING_TRAM = "sightseeingTram"
    SHUTTLE_TRAM = "shuttleTram"
    TRAIN_TRAM = "trainTram"


class TransportmodeEnum(Enum):
    BUS = "bus"
    TRAM = "tram"
    RAIL = "rail"
    METRO = "metro"
    WATER = "water"
    ALL = "all"
    UNKNOWN = "unknown"


@dataclass
class TypeOfFrameRefStructure:
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class TypeOfFuelEnumeration(Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    NATURAL_GAS = "naturalGas"
    BIODIESEL = "biodiesel"
    ELECTRICITY = "electricity"
    HYDROGEN = "hydrogen"
    OTHER = "other"


class VehicleAccessFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    WHEELCHAIR_LIFT = "wheelchairLift"
    MANUAL_RAMP = "manualRamp"
    AUTOMATIC_RAMP = "automaticRamp"
    STEPS = "steps"
    SLIDING_STEP = "slidingStep"
    NARROW_ENTRANCE = "narrowEntrance"
    VALIDATOR = "validator"


@dataclass
class VersionOfObjectRefStructure:
    version: str = field(
        default="any",
        metadata={
            "type": "Attribute",
        }
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VersionOfObjectRefStructureWithClass:
    class Meta:
        name = "VersionOfObjectRefStructure-with-class"

    name_of_ref_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfRefClass",
            "type": "Attribute",
            "required": True,
        }
    )
    version: str = field(
        default="any",
        metadata={
            "type": "Attribute",
        }
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class VersionTypeEnumeration(Enum):
    POINT = "point"
    BASELINE = "baseline"
    OTHER = "other"


class WaterSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INTERNATIONAL_CAR_FERRY = "internationalCarFerry"
    NATIONAL_CAR_FERRY = "nationalCarFerry"
    REGIONAL_CAR_FERRY = "regionalCarFerry"
    LOCAL_CAR_FERRY = "localCarFerry"
    INTERNATIONAL_PASSENGER_FERRY = "internationalPassengerFerry"
    NATIONAL_PASSENGER_FERRY = "nationalPassengerFerry"
    REGIONAL_PASSENGER_FERRY = "regionalPassengerFerry"
    LOCAL_PASSENGER_FERRY = "localPassengerFerry"
    POST_BOAT = "postBoat"
    TRAIN_FERRY = "trainFerry"
    ROAD_FERRY_LINK = "roadFerryLink"
    AIRPORT_BOAT_LINK = "airportBoatLink"
    HIGH_SPEED_VEHICLE_SERVICE = "highSpeedVehicleService"
    HIGH_SPEED_PASSENGER_SERVICE = "highSpeedPassengerService"
    SIGHTSEEING_SERVICE = "sightseeingService"
    SCHOOL_BOAT = "schoolBoat"
    CABLE_FERRY = "cableFerry"
    RIVER_BUS = "riverBus"
    SCHEDULED_FERRY = "scheduledFerry"
    SHUTTLE_FERRY_SERVICE = "shuttleFerryService"


class WeekOfMonthEnumeration(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    EVERY_WEEK = "EveryWeek"


@dataclass
class ExtensionMaxLength:
    class Meta:
        name = "extensionMaxLength"

    max_length: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ExtensionViaOrder:
    class Meta:
        name = "extensionViaOrder"

    via_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ViaOrder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class IconUri:
    class Meta:
        name = "iconURI"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    type_of_info_link: str = field(
        init=False,
        default="icon",
        metadata={
            "name": "typeOfInfoLink",
            "type": "Attribute",
        }
    )


@dataclass
class LanguageUsage:
    class Meta:
        name = "languageUsage"

    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    language_use: str = field(
        init=False,
        default="allUses",
        metadata={
            "name": "LanguageUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class Pos:
    class Meta:
        name = "pos"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PosList:
    class Meta:
        name = "posList"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DataManagedObjectStructure:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: str = field(
        default="any",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DataManagedObjectStructureAnyVersion:
    class Meta:
        name = "DataManagedObjectStructure-any-version"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: str = field(
        init=False,
        default="any",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DataManagedObjectStructureWithStatus:
    class Meta:
        name = "DataManagedObjectStructure-with-status"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: str = field(
        init=False,
        default="any",
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DataManagedObjectStructureWithVersion:
    class Meta:
        name = "DataManagedObjectStructure-with-version"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class LocaleStructure:
    time_zone_offset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TimeZoneOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_zone: str = field(
        init=False,
        default="Europe/Amsterdam",
        metadata={
            "name": "TimeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    summer_time_zone_offset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SummerTimeZoneOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_language: str = field(
        init=False,
        default="nl",
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    languages: Optional["LocaleStructure.Languages"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class Languages:
        language_usage: List[LanguageUsage] = field(
            default_factory=list,
            metadata={
                "name": "LanguageUsage",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class OrderedVersionOfObjectStructure:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: str = field(
        default="any",
        metadata={
            "type": "Attribute",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OrderedVersionOfObjectStructureFixed:
    class Meta:
        name = "OrderedVersionOfObjectStructure-fixed"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: str = field(
        default="any",
        metadata={
            "type": "Attribute",
        }
    )
    order: int = field(
        init=False,
        default=1,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PresentationStructure:
    colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Colour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
        }
    )
    text_colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TextColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
        }
    )
    info_links: Optional["PresentationStructure.InfoLinks"] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class InfoLinks:
        info_link: Optional[IconUri] = field(
            default=None,
            metadata={
                "name": "InfoLink",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )


@dataclass
class PtSubmodeChoice:
    bus_submode: Optional[BusSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    coach_submode: Optional[CoachSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    metro_submode: Optional[MetroSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tram_submode: Optional[TramSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rail_submode: Optional[RailSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    water_submode: Optional[WaterSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TypeOfFrameRefStructureBaseline:
    class Meta:
        name = "TypeOfFrameRefStructure-baseline"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfCompositeFrame = field(
        init=False,
        default=BisonTypeOfCompositeFrame.BISON_TYPE_OF_FRAME_NL_TT_BASELINE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureBisonEnums:
    class Meta:
        name = "TypeOfFrameRefStructure-bison-enums"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfCompositeFrame = field(
        init=False,
        default=BisonTypeOfCompositeFrame.BISON_TYPE_OF_FRAME_NL_BISON_ENUMS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureCalendar:
    class Meta:
        name = "TypeOfFrameRefStructure-calendar"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfProfileFrame = field(
        init=False,
        default=BisonTypeOfProfileFrame.BISON_TYPE_OF_FRAME_NL_TT_CALENDAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureCodespace:
    class Meta:
        name = "TypeOfFrameRefStructure-codespace"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfCompositeFrame = field(
        init=False,
        default=BisonTypeOfCompositeFrame.BISON_TYPE_OF_FRAME_NL_CODESPACES,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureComposite:
    class Meta:
        name = "TypeOfFrameRefStructure-composite"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: Optional[BisonTypeOfCompositeFrame] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeOfFrameRefStructureDelta:
    class Meta:
        name = "TypeOfFrameRefStructure-delta"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfCompositeFrame = field(
        init=False,
        default=BisonTypeOfCompositeFrame.BISON_TYPE_OF_FRAME_NL_TT_DELTA,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureDovaLists:
    class Meta:
        name = "TypeOfFrameRefStructure-dova-lists"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfCompositeFrame = field(
        init=False,
        default=BisonTypeOfCompositeFrame.BISON_TYPE_OF_FRAME_NL_DOVA_LISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureGeneral:
    class Meta:
        name = "TypeOfFrameRefStructure-general"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: Optional[BisonTypeOfGeneralFrame] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeOfFrameRefStructureInfra:
    class Meta:
        name = "TypeOfFrameRefStructure-infra"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfProfileFrame = field(
        init=False,
        default=BisonTypeOfProfileFrame.BISON_TYPE_OF_FRAME_NL_TT_INFRA,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureResource:
    class Meta:
        name = "TypeOfFrameRefStructure-resource"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfProfileFrame = field(
        init=False,
        default=BisonTypeOfProfileFrame.BISON_TYPE_OF_FRAME_NL_TT_RESOURCE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureService:
    class Meta:
        name = "TypeOfFrameRefStructure-service"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfProfileFrame = field(
        init=False,
        default=BisonTypeOfProfileFrame.BISON_TYPE_OF_FRAME_NL_TT_SERVICE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureTimetable:
    class Meta:
        name = "TypeOfFrameRefStructure-timetable"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfProfileFrame = field(
        init=False,
        default=BisonTypeOfProfileFrame.BISON_TYPE_OF_FRAME_NL_TT_TIMETABLE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TypeOfFrameRefStructureVehicle:
    class Meta:
        name = "TypeOfFrameRefStructure-vehicle"

    version: str = field(
        init=False,
        default="9.2.1",
        metadata={
            "type": "Attribute",
        }
    )
    ref: BisonTypeOfProfileFrame = field(
        init=False,
        default=BisonTypeOfProfileFrame.BISON_TYPE_OF_FRAME_NL_TT_VEHICLE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class VersionFrameDefaultsStructureService:
    class Meta:
        name = "VersionFrameDefaultsStructure-service"

    default_responsibility_set_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DefaultResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class VersionFrameVersionStructure:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Codespace(SimpleObjectStructure):
    class Meta:
        name = "codespace"

    xmlns: Optional[str] = field(
        default=None,
        metadata={
            "name": "Xmlns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    xmlns_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmlnsUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ExtensionPrivateCode:
    class Meta:
        name = "extensionPrivateCode"

    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ExtensionTransportMode:
    class Meta:
        name = "extensionTransportMode"

    transport_mode: Optional[TransportmodeEnum] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ExtensionTypeOfProductCategory:
    class Meta:
        name = "extensionTypeOfProductCategory"

    type_of_product_category_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class JourneyDayTypes:
    class Meta:
        name = "journeyDayTypes"

    day_type_ref: List[VersionOfObjectRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class JourneyValidityConditions:
    class Meta:
        name = "journeyValidityConditions"

    availability_condition_ref: List[VersionOfObjectRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class PassengerCapacity:
    class Meta:
        name = "passengerCapacity"

    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    seating_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeatingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    standing_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "StandingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    special_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecialPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    pushchair_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PushchairCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    wheelchair_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class PropertyOfDay:
    class Meta:
        name = "propertyOfDay"

    days_of_week: List[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeek",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    weeks_of_month: List[WeekOfMonthEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "WeeksOfMonth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    day_of_year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "DayOfYear",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    holiday_types: List[HolidayTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HolidayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    seasons: List[SeasonEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Seasons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    tides: List[TideEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Tides",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    day_event: Optional[DayEventEnumeration] = field(
        default=None,
        metadata={
            "name": "DayEvent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crowding: Optional[CrowdingEnumeration] = field(
        default=None,
        metadata={
            "name": "Crowding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class Via:
    class Meta:
        name = "via"

    extensions: Optional[ExtensionViaOrder] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class LineString:
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class TypeOfValueVersionStructure(DataManagedObjectStructureAnyVersion):
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TypeOfValueVersionStructureWithVersion(DataManagedObjectStructureWithVersion):
    class Meta:
        name = "TypeOfValueVersionStructure-with-version"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class VersionFrameDefaultsStructure:
    default_codespace_ref: Optional[SimpleObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DefaultCodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    default_data_source_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DefaultDataSourceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_responsibility_set_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DefaultResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_locale: Optional[LocaleStructure] = field(
        default=None,
        metadata={
            "name": "DefaultLocale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_location_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLocationSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_system_of_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultSystemOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class AccessibilityAssessment(DataManagedObjectStructure):
    class Meta:
        name = "accessibilityAssessment"

    mobility_impaired_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ActivationPoint(DataManagedObjectStructure):
    class Meta:
        name = "activationPoint"

    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    type_of_activation_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class Authority(DataManagedObjectStructureWithStatus):
    class Meta:
        name = "authority"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class AvailabilityCondition(DataManagedObjectStructure):
    class Meta:
        name = "availabilityCondition"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FromDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    valid_day_bits: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidDayBits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
            "pattern": r"[0-1]+",
        }
    )


@dataclass
class Block(DataManagedObjectStructure):
    class Meta:
        name = "block"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    finishing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EndTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[JourneyDayTypes] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journeys: Optional["Block.Journeys"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class Journeys:
        dead_run_ref: List[VersionOfObjectRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "DeadRunRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )
        service_journey_ref: List[VersionOfObjectRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "ServiceJourneyRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )


@dataclass
class Branding(DataManagedObjectStructure):
    class Meta:
        name = "branding"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 1024,
            "pattern": r"(http|HTTP|https|HTTPS|ftp|FTP)://.+\.(jpg|JPG|jpeg|JPEG|gif|GIF|png|PNG|svg|SVG)",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 1024,
            "pattern": r"(http|HTTP|https|HTTPS)://.+",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class Codespaces:
    class Meta:
        name = "codespaces"

    codespace: List[Codespace] = field(
        default_factory=list,
        metadata={
            "name": "Codespace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class DataSource(DataManagedObjectStructure):
    class Meta:
        name = "dataSource"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class DayType(DataManagedObjectStructure):
    class Meta:
        name = "dayType"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    properties: Optional["DayType.Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class Properties:
        property_of_day: List[PropertyOfDay] = field(
            default_factory=list,
            metadata={
                "name": "PropertyOfDay",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class DayTypeAssignment(OrderedVersionOfObjectStructureFixed):
    class Meta:
        name = "dayTypeAssignment"

    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    day_type_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class DeadRun(DataManagedObjectStructure):
    class Meta:
        name = "deadRun"

    validity_conditions: Optional[JourneyValidityConditions] = field(
        default=None,
        metadata={
            "name": "validityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[JourneyDayTypes] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_journey_pattern_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    time_demand_type_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_type_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_type: Optional[DeadRunTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DeadRunType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class DestinationDisplayVariant(DataManagedObjectStructure):
    class Meta:
        name = "destinationDisplayVariant"

    extensions: Optional[ExtensionMaxLength] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    destination_display_variant_media_type: Optional[DeliveryVariantTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayVariantMediaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vias: Optional["DestinationDisplayVariant.Vias"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class Vias:
        via: List[Via] = field(
            default_factory=list,
            metadata={
                "name": "Via",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class GroupOfLines(DataManagedObjectStructure):
    class Meta:
        name = "groupOfLines"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional["GroupOfLines.Members"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    transport_mode: Optional[TransportmodeEnum] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_lines_type: GroupOfLinesTypeEnumeration = field(
        init=False,
        default=GroupOfLinesTypeEnumeration.SCHEDULING,
        metadata={
            "name": "GroupOfLinesType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class Members:
        line_ref: List[VersionOfObjectRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "LineRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class JourneyLayover(DataManagedObjectStructure):
    class Meta:
        name = "journeyLayover"

    layover: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Layover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    scheduled_stop_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class JourneyRunTime(DataManagedObjectStructure):
    class Meta:
        name = "journeyRunTime"

    timing_link_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    run_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class JourneyWaitTime(DataManagedObjectStructure):
    class Meta:
        name = "journeyWaitTime"

    scheduled_stop_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class Network(DataManagedObjectStructureWithStatus):
    class Meta:
        name = "network"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[TransportmodeEnum] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_lines_type: Optional[GroupOfLinesTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    authority_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class Notice(DataManagedObjectStructure):
    class Meta:
        name = "notice"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class NoticeAssignment(DataManagedObjectStructure):
    class Meta:
        name = "noticeAssignment"

    notice_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    noticed_object_ref: Optional[VersionOfObjectRefStructureWithClass] = field(
        default=None,
        metadata={
            "name": "NoticedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OperationalContext(DataManagedObjectStructure):
    class Meta:
        name = "operationalContext"

    vehicle_mode: Optional[TransportmodeEnum] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    transport_submode: Optional[PtSubmodeChoice] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class Operator(DataManagedObjectStructure):
    class Meta:
        name = "operator"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_service_contact_details: Optional["Operator.CustomerServiceContactDetails"] = field(
        default=None,
        metadata={
            "name": "CustomerServiceContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class CustomerServiceContactDetails:
        email: Optional[str] = field(
            default=None,
            metadata={
                "name": "Email",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        phone: Optional[str] = field(
            default=None,
            metadata={
                "name": "Phone",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        url: Optional[str] = field(
            default=None,
            metadata={
                "name": "Url",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "max_length": 1024,
                "pattern": r"(http|HTTP|https|HTTPS)://.+",
            }
        )


@dataclass
class Organisation(DataManagedObjectStructure):
    class Meta:
        name = "organisation"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_organisation: Optional["Organisation.TypesOfOrganisation"] = field(
        default=None,
        metadata={
            "name": "typesOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class TypesOfOrganisation:
        type_of_organisation_ref: Optional[VersionOfObjectRefStructure] = field(
            default=None,
            metadata={
                "name": "TypeOfOrganisationRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )


@dataclass
class PassengerStopAssignment(OrderedVersionOfObjectStructureFixed):
    class Meta:
        name = "passengerStopAssignment"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    stop_place_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class PointOnLink(DataManagedObjectStructure):
    class Meta:
        name = "pointOnLink"

    distance_from_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    activation_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ActivationPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class PointOnRoute(OrderedVersionOfObjectStructure):
    class Meta:
        name = "pointOnRoute"

    route_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "RoutePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    onward_route_link_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardRouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class PointProjection(DataManagedObjectStructure):
    class Meta:
        name = "pointProjection"

    project_to_point_ref: Optional[VersionOfObjectRefStructureWithClass] = field(
        default=None,
        metadata={
            "name": "ProjectToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ResponsibilityRoleAssignment(DataManagedObjectStructure):
    class Meta:
        name = "responsibilityRoleAssignment"

    stakeholder_role_type: List[StakeholderRoleTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "StakeholderRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    type_of_responsibility_role_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsible_organisation_ref: Optional[VersionOfObjectRefStructureWithClass] = field(
        default=None,
        metadata={
            "name": "ResponsibleOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsible_area_ref: Optional[VersionOfObjectRefStructureWithClass] = field(
        default=None,
        metadata={
            "name": "ResponsibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class RoutePoint(DataManagedObjectStructure):
    class Meta:
        name = "routePoint"

    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ServiceFacilitySet(DataManagedObjectStructure):
    class Meta:
        name = "serviceFacilitySet"

    mobility_facility_list: List[MobilityFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MobilityFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    passenger_comms_facility_list: List[PassengerCommsFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCommsFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    sanitary_facility_list: List[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticketing_service_facility_list: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    vehicle_access_facility_list: List[AccessFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleAccessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )


@dataclass
class ServiceJourney(DataManagedObjectStructure):
    class Meta:
        name = "serviceJourney"

    key_list: Optional[KeyListStructure] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_conditions: Optional[JourneyValidityConditions] = field(
        default=None,
        metadata={
            "name": "validityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[JourneyDayTypes] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_pattern_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    time_demand_type_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_type_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    print: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dynamic: Optional[DynamicAdvertisementEnumeration] = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ServiceJourneyInterchange(DataManagedObjectStructure):
    class Meta:
        name = "serviceJourneyInterchange"

    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    from_journey_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "FromJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_journey_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ToJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class StopArea(DataManagedObjectStructure):
    class Meta:
        name = "stopArea"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_view: Optional["StopArea.TopographicPlaceView"] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class TopographicPlaceView:
        name: Optional[MultilingualString] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )


@dataclass
class StopPointInJourneyPattern(OrderedVersionOfObjectStructure):
    class Meta:
        name = "stopPointInJourneyPattern"

    scheduled_stop_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    onward_timing_link_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_wait_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWaitPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_alighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_boarding: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForBoarding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TariffZone(DataManagedObjectStructureWithStatus):
    class Meta:
        name = "tariffZone"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TimingLink(DataManagedObjectStructure):
    class Meta:
        name = "timingLink"

    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    from_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    operational_context_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TimingPointInJourneyPattern(OrderedVersionOfObjectStructure):
    class Meta:
        name = "timingPointInJourneyPattern"

    timing_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    onward_timing_link_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_wait_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWaitPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TransportAdministrativeZone(DataManagedObjectStructureWithStatus):
    class Meta:
        name = "transportAdministrativeZone"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TypeOfProductCategory(DataManagedObjectStructure):
    class Meta:
        name = "typeOfProductCategory"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 1024,
            "pattern": r"(http|HTTP|https|HTTPS|ftp|FTP)://.+\.(jpg|JPG|jpeg|JPEG|gif|GIF|png|PNG|svg|SVG)",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 1024,
            "pattern": r"(http|HTTP|https|HTTPS)://.+",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class Vehicle(DataManagedObjectStructure):
    class Meta:
        name = "vehicle"

    valid_between: Optional["Vehicle.ValidBetween"] = field(
        default=None,
        metadata={
            "name": "ValidBetween",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    extensions: Optional[ExtensionTransportMode] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    registration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistrationNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationalNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    responsibility_set_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
        }
    )

    @dataclass
    class ValidBetween:
        from_date: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "FromDate",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
        to_date: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "ToDate",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )


@dataclass
class Version(DataManagedObjectStructureWithVersion):
    class Meta:
        name = "version"

    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_type: Optional[VersionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "VersionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    derived_from_version_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DerivedFromVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class DeadRunJourneyPattern(DataManagedObjectStructure):
    class Meta:
        name = "deadRunJourneyPattern"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_in_sequence: Optional["DeadRunJourneyPattern.PointsInSequence"] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class PointsInSequence:
        stop_point_in_journey_pattern: List[StopPointInJourneyPattern] = field(
            default_factory=list,
            metadata={
                "name": "StopPointInJourneyPattern",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 2,
            }
        )
        timing_point_in_journey_pattern: List[TimingPointInJourneyPattern] = field(
            default_factory=list,
            metadata={
                "name": "TimingPointInJourneyPattern",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 2,
            }
        )


@dataclass
class DestinationDisplay(DataManagedObjectStructure):
    class Meta:
        name = "destinationDisplay"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    side_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "SideText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    front_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "FrontText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vias: Optional["DestinationDisplay.Vias"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    variants: Optional["DestinationDisplay.Variants"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class Vias:
        via: List[Via] = field(
            default_factory=list,
            metadata={
                "name": "Via",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Variants:
        destination_display_variant: List[DestinationDisplayVariant] = field(
            default_factory=list,
            metadata={
                "name": "DestinationDisplayVariant",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 4,
            }
        )


@dataclass
class DisplayTextLength(TypeOfValueVersionStructure):
    class Meta:
        name = "displayTextLength"


@dataclass
class Facilities:
    class Meta:
        name = "facilities"

    service_facility_set: List[ServiceFacilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class InfrastructureFrame(VersionFrameVersionStructure):
    class Meta:
        name = "infrastructureFrame"

    type_of_frame_ref: Optional[TypeOfFrameRefStructureInfra] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    activation_points: Optional["InfrastructureFrame.ActivationPoints"] = field(
        default=None,
        metadata={
            "name": "activationPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class ActivationPoints:
        activation_point: List[ActivationPoint] = field(
            default_factory=list,
            metadata={
                "name": "ActivationPoint",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class Line(DataManagedObjectStructure):
    class Meta:
        name = "line"

    branding_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    transport_mode: Optional[TransportmodeEnum] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    transport_submode: Optional[PtSubmodeChoice] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    external_line_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_product_category_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    responsibility_set_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Projections:
    class Meta:
        name = "projections"

    point_projection: Optional[PointProjection] = field(
        default=None,
        metadata={
            "name": "PointProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ResponsibilitySet(DataManagedObjectStructure):
    class Meta:
        name = "responsibilitySet"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    roles: Optional["ResponsibilitySet.Roles"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class Roles:
        responsibility_role_assignment: List[ResponsibilityRoleAssignment] = field(
            default_factory=list,
            metadata={
                "name": "ResponsibilityRoleAssignment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class Route(DataManagedObjectStructure):
    class Meta:
        name = "route"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    points_in_sequence: Optional["Route.PointsInSequence"] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class PointsInSequence:
        point_on_route: List[PointOnRoute] = field(
            default_factory=list,
            metadata={
                "name": "PointOnRoute",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 2,
            }
        )


@dataclass
class RouteLink(DataManagedObjectStructure):
    class Meta:
        name = "routeLink"

    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    passing_through: Optional["RouteLink.PassingThrough"] = field(
        default=None,
        metadata={
            "name": "passingThrough",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    operational_context_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_set_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
        }
    )

    @dataclass
    class PassingThrough:
        point_on_link: List[PointOnLink] = field(
            default_factory=list,
            metadata={
                "name": "PointOnLink",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class ServiceCalendarFrame(VersionFrameVersionStructure):
    class Meta:
        name = "serviceCalendarFrame"

    type_of_frame_ref: Optional[TypeOfFrameRefStructureCalendar] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    day_types: Optional["ServiceCalendarFrame.DayTypes"] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    day_type_assignments: Optional["ServiceCalendarFrame.DayTypeAssignments"] = field(
        default=None,
        metadata={
            "name": "dayTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class DayTypes:
        day_type: List[DayType] = field(
            default_factory=list,
            metadata={
                "name": "DayType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class DayTypeAssignments:
        day_type_assignment: List[DayTypeAssignment] = field(
            default_factory=list,
            metadata={
                "name": "DayTypeAssignment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class ServiceJourneyPattern(DataManagedObjectStructure):
    class Meta:
        name = "serviceJourneyPattern"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    points_in_sequence: Optional["ServiceJourneyPattern.PointsInSequence"] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class PointsInSequence:
        stop_point_in_journey_pattern: List[StopPointInJourneyPattern] = field(
            default_factory=list,
            metadata={
                "name": "StopPointInJourneyPattern",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 2,
            }
        )
        timing_point_in_journey_pattern: List[TimingPointInJourneyPattern] = field(
            default_factory=list,
            metadata={
                "name": "TimingPointInJourneyPattern",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 2,
            }
        )


@dataclass
class TimeDemandType(DataManagedObjectStructure):
    class Meta:
        name = "timeDemandType"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    run_times: Optional["TimeDemandType.RunTimes"] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    wait_times: Optional["TimeDemandType.WaitTimes"] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layovers: Optional["TimeDemandType.Layovers"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class RunTimes:
        journey_run_time: List[JourneyRunTime] = field(
            default_factory=list,
            metadata={
                "name": "JourneyRunTime",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class WaitTimes:
        journey_wait_time: List[JourneyWaitTime] = field(
            default_factory=list,
            metadata={
                "name": "JourneyWaitTime",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Layovers:
        journey_layover: List[JourneyLayover] = field(
            default_factory=list,
            metadata={
                "name": "JourneyLayover",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class TimetableFrame(VersionFrameVersionStructure):
    class Meta:
        name = "timetableFrame"

    type_of_frame_ref: Optional[TypeOfFrameRefStructureTimetable] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    content_validity_conditions: Optional["TimetableFrame.ContentValidityConditions"] = field(
        default=None,
        metadata={
            "name": "contentValidityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    operator_view: Optional["TimetableFrame.OperatorView"] = field(
        default=None,
        metadata={
            "name": "OperatorView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_journeys: Optional["TimetableFrame.VehicleJourneys"] = field(
        default=None,
        metadata={
            "name": "vehicleJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    journey_interchanges: Optional["TimetableFrame.JourneyInterchanges"] = field(
        default=None,
        metadata={
            "name": "journeyInterchanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class ContentValidityConditions:
        availability_condition: List[AvailabilityCondition] = field(
            default_factory=list,
            metadata={
                "name": "AvailabilityCondition",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class OperatorView:
        operator_ref: Optional[VersionOfObjectRefStructure] = field(
            default=None,
            metadata={
                "name": "OperatorRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )

    @dataclass
    class VehicleJourneys:
        service_journey: List[ServiceJourney] = field(
            default_factory=list,
            metadata={
                "name": "ServiceJourney",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )
        dead_run: List[DeadRun] = field(
            default_factory=list,
            metadata={
                "name": "DeadRun",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )

    @dataclass
    class JourneyInterchanges:
        service_journey_interchange: List[ServiceJourneyInterchange] = field(
            default_factory=list,
            metadata={
                "name": "ServiceJourneyInterchange",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class TypeOfActivation(TypeOfValueVersionStructure):
    class Meta:
        name = "typeOfActivation"


@dataclass
class TypeOfEquipment(TypeOfValueVersionStructure):
    class Meta:
        name = "typeOfEquipment"


@dataclass
class TypeOfFrame(TypeOfValueVersionStructureWithVersion):
    class Meta:
        name = "typeOfFrame"


@dataclass
class TypeOfOrganisation(TypeOfValueVersionStructure):
    class Meta:
        name = "typeOfOrganisation"


@dataclass
class TypeOfResponsibilityRole(TypeOfValueVersionStructure):
    class Meta:
        name = "typeOfResponsibilityRole"


@dataclass
class TypeOfService(TypeOfValueVersionStructure):
    class Meta:
        name = "typeOfService"


@dataclass
class VehicleScheduleFrame(VersionFrameVersionStructure):
    class Meta:
        name = "vehicleScheduleFrame"

    type_of_frame_ref: Optional[TypeOfFrameRefStructureVehicle] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    blocks: Optional["VehicleScheduleFrame.Blocks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class Blocks:
        block: List[Block] = field(
            default_factory=list,
            metadata={
                "name": "Block",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class Versions:
    class Meta:
        name = "versions"

    version: Optional[Version] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ScheduledStopPoint(DataManagedObjectStructure):
    class Meta:
        name = "scheduledStopPoint"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    projections: Optional[Projections] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    stop_areas: Optional["ScheduledStopPoint.StopAreas"] = field(
        default=None,
        metadata={
            "name": "stopAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zones: Optional["ScheduledStopPoint.TariffZones"] = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    for_alighting: bool = field(
        default=True,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_boarding: bool = field(
        default=True,
        metadata={
            "name": "ForBoarding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class StopAreas:
        stop_area_ref: Optional[VersionOfObjectRefStructure] = field(
            default=None,
            metadata={
                "name": "StopAreaRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )

    @dataclass
    class TariffZones:
        tariff_zone_ref: List[VersionOfObjectRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "TariffZoneRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class TimingPoint(DataManagedObjectStructure):
    class Meta:
        name = "timingPoint"

    key_list: Optional[KeyListStructure] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    projections: Optional[Projections] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ValueSet(DataManagedObjectStructure):
    class Meta:
        name = "valueSet"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    values: Optional["ValueSet.Values"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class Values:
        type_of_frame: List[TypeOfFrame] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        type_of_activation: List[TypeOfActivation] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfActivation",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        type_of_equipment: List[TypeOfEquipment] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfEquipment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        type_of_service: List[TypeOfService] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfService",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        type_of_organisation: List[TypeOfOrganisation] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfOrganisation",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        type_of_responsibility_role: List[TypeOfResponsibilityRole] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfResponsibilityRole",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        type_of_entity: List[DisplayTextLength] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfEntity",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )


@dataclass
class VehicleType(DataManagedObjectStructure):
    class Meta:
        name = "vehicleType"

    extensions: Optional[ExtensionTypeOfProductCategory] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    branding_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    private_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fuel: Optional[TypeOfFuelEnumeration] = field(
        default=None,
        metadata={
            "name": "TypeOfFuel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    euro_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capacities: Optional["VehicleType.Capacities"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    has_lift_or_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    has_hoist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasHoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gap_to_platform: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facilities: Optional[Facilities] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    transport_mode: Optional[TransportmodeEnum] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class Capacities:
        passenger_capacity: List[PassengerCapacity] = field(
            default_factory=list,
            metadata={
                "name": "PassengerCapacity",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class GeneralFrame(VersionFrameVersionStructure):
    class Meta:
        name = "generalFrame"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame_ref: Optional[TypeOfFrameRefStructureGeneral] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    members: Optional["GeneralFrame.Members"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class Members:
        value_set: List[ValueSet] = field(
            default_factory=list,
            metadata={
                "name": "ValueSet",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        tariff_zone: List[TariffZone] = field(
            default_factory=list,
            metadata={
                "name": "TariffZone",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        authority: List[Authority] = field(
            default_factory=list,
            metadata={
                "name": "Authority",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        network: List[Network] = field(
            default_factory=list,
            metadata={
                "name": "Network",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )
        transport_administrative_zone: List[TransportAdministrativeZone] = field(
            default_factory=list,
            metadata={
                "name": "TransportAdministrativeZone",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )
        data_source: Optional[DataSource] = field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        responsibility_set: List[ResponsibilitySet] = field(
            default_factory=list,
            metadata={
                "name": "ResponsibilitySet",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        vehicle: List[Vehicle] = field(
            default_factory=list,
            metadata={
                "name": "Vehicle",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )


@dataclass
class ResourceFrame(VersionFrameVersionStructure):
    class Meta:
        name = "resourceFrame"

    type_of_frame_ref: Optional[TypeOfFrameRefStructureResource] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    data_sources: Optional["ResourceFrame.DataSources"] = field(
        default=None,
        metadata={
            "name": "dataSources",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    responsibility_sets: Optional["ResourceFrame.ResponsibilitySets"] = field(
        default=None,
        metadata={
            "name": "responsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    types_of_value: Optional["ResourceFrame.TypesOfValue"] = field(
        default=None,
        metadata={
            "name": "typesOfValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisations: Optional["ResourceFrame.Organisations"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    operational_contexts: Optional["ResourceFrame.OperationalContexts"] = field(
        default=None,
        metadata={
            "name": "operationalContexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_types: Optional["ResourceFrame.VehicleTypes"] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    zones: Optional["ResourceFrame.Zones"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    @dataclass
    class DataSources:
        data_source: List[DataSource] = field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )

    @dataclass
    class ResponsibilitySets:
        responsibility_set: List[ResponsibilitySet] = field(
            default_factory=list,
            metadata={
                "name": "ResponsibilitySet",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class TypesOfValue:
        branding: List[Branding] = field(
            default_factory=list,
            metadata={
                "name": "Branding",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        type_of_product_category: List[TypeOfProductCategory] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfProductCategory",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )

    @dataclass
    class Organisations:
        operator: List[Operator] = field(
            default_factory=list,
            metadata={
                "name": "Operator",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )
        organisation: List[Organisation] = field(
            default_factory=list,
            metadata={
                "name": "Organisation",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        authority: List[Authority] = field(
            default_factory=list,
            metadata={
                "name": "Authority",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class OperationalContexts:
        operational_context: List[OperationalContext] = field(
            default_factory=list,
            metadata={
                "name": "OperationalContext",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class VehicleTypes:
        vehicle_type: List[VehicleType] = field(
            default_factory=list,
            metadata={
                "name": "VehicleType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Zones:
        transport_administrative_zone: Optional[TransportAdministrativeZone] = field(
            default=None,
            metadata={
                "name": "TransportAdministrativeZone",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )


@dataclass
class ServiceFrame(VersionFrameVersionStructure):
    class Meta:
        name = "serviceFrame"

    type_of_frame_ref: Optional[TypeOfFrameRefStructureService] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    frame_defaults: Optional[VersionFrameDefaultsStructureService] = field(
        default=None,
        metadata={
            "name": "FrameDefaults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_points: Optional["ServiceFrame.RoutePoints"] = field(
        default=None,
        metadata={
            "name": "routePoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    route_links: Optional["ServiceFrame.RouteLinks"] = field(
        default=None,
        metadata={
            "name": "routeLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    routes: Optional["ServiceFrame.Routes"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    lines: Optional["ServiceFrame.Lines"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    groups_of_lines: Optional["ServiceFrame.GroupsOfLines"] = field(
        default=None,
        metadata={
            "name": "groupsOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_displays: Optional["ServiceFrame.DestinationDisplays"] = field(
        default=None,
        metadata={
            "name": "destinationDisplays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    scheduled_stop_points: Optional["ServiceFrame.ScheduledStopPoints"] = field(
        default=None,
        metadata={
            "name": "scheduledStopPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    stop_areas: Optional["ServiceFrame.StopAreas"] = field(
        default=None,
        metadata={
            "name": "stopAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_assignments: Optional["ServiceFrame.StopAssignments"] = field(
        default=None,
        metadata={
            "name": "stopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    timing_points: Optional["ServiceFrame.TimingPoints"] = field(
        default=None,
        metadata={
            "name": "timingPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_links: Optional["ServiceFrame.TimingLinks"] = field(
        default=None,
        metadata={
            "name": "timingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    journey_patterns: Optional["ServiceFrame.JourneyPatterns"] = field(
        default=None,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    time_demand_types: Optional["ServiceFrame.TimeDemandTypes"] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    notices: Optional["ServiceFrame.Notices"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional["ServiceFrame.NoticeAssignments"] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class RoutePoints:
        route_point: List[RoutePoint] = field(
            default_factory=list,
            metadata={
                "name": "RoutePoint",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class RouteLinks:
        route_link: List[RouteLink] = field(
            default_factory=list,
            metadata={
                "name": "RouteLink",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Routes:
        route: List[Route] = field(
            default_factory=list,
            metadata={
                "name": "Route",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Lines:
        line: List[Line] = field(
            default_factory=list,
            metadata={
                "name": "Line",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class GroupsOfLines:
        group_of_lines: List[GroupOfLines] = field(
            default_factory=list,
            metadata={
                "name": "GroupOfLines",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class DestinationDisplays:
        destination_display: List[DestinationDisplay] = field(
            default_factory=list,
            metadata={
                "name": "DestinationDisplay",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class ScheduledStopPoints:
        scheduled_stop_point: List[ScheduledStopPoint] = field(
            default_factory=list,
            metadata={
                "name": "ScheduledStopPoint",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class StopAreas:
        stop_area: List[StopArea] = field(
            default_factory=list,
            metadata={
                "name": "StopArea",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class StopAssignments:
        passenger_stop_assignment: List[PassengerStopAssignment] = field(
            default_factory=list,
            metadata={
                "name": "PassengerStopAssignment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class TimingPoints:
        timing_point: List[TimingPoint] = field(
            default_factory=list,
            metadata={
                "name": "TimingPoint",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class TimingLinks:
        timing_link: List[TimingLink] = field(
            default_factory=list,
            metadata={
                "name": "TimingLink",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class JourneyPatterns:
        service_journey_pattern: List[ServiceJourneyPattern] = field(
            default_factory=list,
            metadata={
                "name": "ServiceJourneyPattern",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )
        dead_run_journey_pattern: List[DeadRunJourneyPattern] = field(
            default_factory=list,
            metadata={
                "name": "DeadRunJourneyPattern",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )

    @dataclass
    class TimeDemandTypes:
        time_demand_type: List[TimeDemandType] = field(
            default_factory=list,
            metadata={
                "name": "TimeDemandType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Notices:
        notice: List[Notice] = field(
            default_factory=list,
            metadata={
                "name": "Notice",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class NoticeAssignments:
        notice_assignment: List[NoticeAssignment] = field(
            default_factory=list,
            metadata={
                "name": "NoticeAssignment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class CompositeFrame(VersionFrameVersionStructure):
    class Meta:
        name = "compositeFrame"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame_ref: Optional[TypeOfFrameRefStructureComposite] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    codespaces: Optional[Codespaces] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frame_defaults: Optional[VersionFrameDefaultsStructure] = field(
        default=None,
        metadata={
            "name": "FrameDefaults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    versions: Optional[Versions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frames: Optional["CompositeFrame.Frames"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class Frames:
        general_frame: List[GeneralFrame] = field(
            default_factory=list,
            metadata={
                "name": "GeneralFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        resource_frame: List[ResourceFrame] = field(
            default_factory=list,
            metadata={
                "name": "ResourceFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )
        infrastructure_frame: List[InfrastructureFrame] = field(
            default_factory=list,
            metadata={
                "name": "InfrastructureFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )
        service_frame: List[ServiceFrame] = field(
            default_factory=list,
            metadata={
                "name": "ServiceFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )
        timetable_frame: List[TimetableFrame] = field(
            default_factory=list,
            metadata={
                "name": "TimetableFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )
        service_calendar_frame: List[ServiceCalendarFrame] = field(
            default_factory=list,
            metadata={
                "name": "ServiceCalendarFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )
        vehicle_schedule_frame: List[VehicleScheduleFrame] = field(
            default_factory=list,
            metadata={
                "name": "VehicleScheduleFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequential": True,
            }
        )


@dataclass
class DataObjects:
    class Meta:
        name = "dataObjects"

    composite_frame: List[CompositeFrame] = field(
        default_factory=list,
        metadata={
            "name": "CompositeFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class PublicationDelivery:
    class Meta:
        name = "publicationDelivery"

    publication_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PublicationTimestamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_objects: Optional[DataObjects] = field(
        default=None,
        metadata={
            "name": "dataObjects",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    version: str = field(
        init=False,
        default="ntx:1.1",
        metadata={
            "type": "Attribute",
        }
    )
