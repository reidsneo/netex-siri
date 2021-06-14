from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod, XmlTime

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class AccessFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    LIFT = "lift"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    STAIRS = "stairs"
    SHUTTLE = "shuttle"
    NARROW_ENTRANCE = "narrowEntrance"
    BARRIER = "barrier"
    PALLET_ACCESS_LOW_FLOOR = "palletAccess_lowFloor"
    VALIDATOR = "validator"
    MANUAL_RAMP = "manualRamp"
    AUTOMATIC_RAMP = "automaticRamp"
    WHEELCHAIR_LIFT = "wheelchairLift"
    SLIDING_STEP = "slidingStep"
    OTHER = "other"


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


class MetroSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    METRO = "metro"
    TUBE = "tube"
    URBAN_RAILWAY = "urbanRailway"


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


class TypeOfFuelEnumeration(Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    NATURAL_GAS = "naturalGas"
    BIODIESEL = "biodiesel"
    ELECTRICITY = "electricity"
    OTHER = "other"


class TypeOfVersionEnumeration(Enum):
    POINT = "point"
    BASELINE = "baseline"
    DELTA = "delta"


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
class AccessibilityAssessment:
    class Meta:
        name = "accessibilityAssessment"

    mobility_impaired_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    comment: Optional[object] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class IdentifiedObject:
    class Meta:
        name = "identifiedObject_"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class KeyList:
    class Meta:
        name = "keyList"

    key_value: List["KeyList.KeyValue"] = field(
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
        type_of_key: Optional[str] = field(
            default=None,
            metadata={
                "name": "typeOfKey",
                "type": "Attribute",
                "namespace": "http://www.netex.org.uk/netex",
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
class Location:
    class Meta:
        name = "location"

    pos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


class Modification(Enum):
    NEW = "new"
    DELETE = "delete"
    REVISE = "revise"
    UNCHANGED = "unchanged"
    DELTA = "delta"


@dataclass
class PredefinedObject:
    class Meta:
        name = "predefinedObject_"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PrivateCode:
    class Meta:
        name = "privateCode"

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


@dataclass
class Ref:
    class Meta:
        name = "ref"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RefClass:
    class Meta:
        name = "refClass"

    name_of_ref_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfRefClass",
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


@dataclass
class RefClassVersion:
    class Meta:
        name = "refClassVersion"

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


@dataclass
class RefType:
    class Meta:
        name = "refType"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


@dataclass
class RefVersion:
    class Meta:
        name = "refVersion"

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
class TypeOfActivation:
    class Meta:
        name = "typeOfActivation"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TypeOfEquipment:
    class Meta:
        name = "typeOfEquipment"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TypeOfService:
    class Meta:
        name = "typeOfService"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TypedString:
    class Meta:
        name = "typedString"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    text_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "textIdType",
            "type": "Attribute",
        }
    )


@dataclass
class VersionedFrame:
    class Meta:
        name = "versionedFrame_"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
class VersionedObject:
    class Meta:
        name = "versionedObject_"

    id: Optional[str] = field(
        default=None,
        metadata={
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
class PtSubmodeChoice:
    bus_submode: Optional[BusSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "BusSubmode",
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
class AdministrativeZone(PredefinedObject):
    class Meta:
        name = "administrativeZone"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class Authority(PredefinedObject):
    class Meta:
        name = "authority"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ExtensionPrivateCode:
    class Meta:
        name = "extensionPrivateCode"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class JourneyDayTypes:
    class Meta:
        name = "journeyDayTypes"

    day_type_ref: List[RefVersion] = field(
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

    availability_condition_ref: List[RefVersion] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class LocaleStructure:
    class Meta:
        name = "localeStructure"

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
            }
        )


@dataclass
class ModifiedFrame:
    class Meta:
        name = "modifiedFrame_"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: Optional[Modification] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
class ModifiedObject:
    class Meta:
        name = "modifiedObject_"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: Optional[Modification] = field(
        default=None,
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
class ModifiedVersion:
    class Meta:
        name = "modifiedVersion_"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: Optional[Modification] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
class OrderedObject:
    class Meta:
        name = "orderedObject_"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modification: Optional[Modification] = field(
        default=None,
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
class Presentation:
    class Meta:
        name = "presentation"

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
    info_links: Optional["Presentation.InfoLinks"] = field(
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
    days_event: Optional[DayEventEnumeration] = field(
        default=None,
        metadata={
            "name": "DaysEvent",
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

    name: Optional[TypedString] = field(
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
class ActivationPoint(ModifiedObject):
    class Meta:
        name = "activationPoint"

    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_activation_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class AvailabilityCondition(ModifiedObject):
    class Meta:
        name = "availabilityCondition"

    name: Optional[str] = field(
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
class Block(ModifiedObject):
    class Meta:
        name = "block"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_type_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class Branding(ModifiedObject):
    class Meta:
        name = "branding"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[str] = field(
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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[Presentation] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class DataSource(ModifiedObject):
    class Meta:
        name = "dataSource"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
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
class DayType(ModifiedObject):
    class Meta:
        name = "dayType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[str] = field(
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
        property_of_day: Optional[PropertyOfDay] = field(
            default=None,
            metadata={
                "name": "PropertyOfDay",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )


@dataclass
class DayTypeAssignment(ModifiedObject):
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
    day_type_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class DeadRun(ModifiedObject):
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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    dead_run_journey_pattern_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    time_demand_type_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_type_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "BlockRef",
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
    data_source_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        }
    )


@dataclass
class DestinationDisplayVariant(ModifiedObject):
    class Meta:
        name = "destinationDisplayVariant"

    front_text: Optional[TypedString] = field(
        default=None,
        metadata={
            "name": "FrontText",
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
class FrameDefaults:
    class Meta:
        name = "frameDefaults"

    default_data_source_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "DefaultDataSourceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    default_responsibility_set_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "DefaultResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    default_locale: Optional[LocaleStructure] = field(
        default=None,
        metadata={
            "name": "DefaultLocale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    default_location_system: str = field(
        init=False,
        default="EPSG:28992",
        metadata={
            "name": "DefaultLocationSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_system_of_units: str = field(
        init=False,
        default="SiMetres",
        metadata={
            "name": "DefaultSystemOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_currency: str = field(
        init=False,
        default="EUR",
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class JourneyLayover(ModifiedObject):
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
    scheduled_stop_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class JourneyRunTime(ModifiedObject):
    class Meta:
        name = "journeyRunTime"

    timing_link_ref: Optional[RefVersion] = field(
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
class JourneyWaitTime(ModifiedObject):
    class Meta:
        name = "journeyWaitTime"

    scheduled_stop_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_ref: Optional[RefVersion] = field(
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
class Line(ModifiedObject):
    class Meta:
        name = "line"

    branding_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    name: Optional[str] = field(
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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_line_ref: Optional[RefType] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    additional_transport_organisations: Optional["Line.AdditionalTransportOrganisations"] = field(
        default=None,
        metadata={
            "name": "additionalTransportOrganisations",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_product_category_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_ref: Optional[Ref] = field(
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
    presentation: Optional[Presentation] = field(
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

    @dataclass
    class AdditionalTransportOrganisations:
        transport_organisation_ref: List[RefClassVersion] = field(
            default_factory=list,
            metadata={
                "name": "TransportOrganisationRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class Notice(ModifiedObject):
    class Meta:
        name = "notice"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class NoticeAssignment(ModifiedObject):
    class Meta:
        name = "noticeAssignment"

    notice_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    noticed_object_ref: Optional[RefClassVersion] = field(
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
        }
    )


@dataclass
class OperationalContext(ModifiedObject):
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
class Operator(ModifiedObject):
    class Meta:
        name = "operator"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
class PassengerStopAssignment(ModifiedObject):
    class Meta:
        name = "passengerStopAssignment"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    stop_place_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class PointOnLink(OrderedObject):
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
    activation_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "ActivationPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class PointOnRoute(OrderedObject):
    class Meta:
        name = "pointOnRoute"

    route_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "RoutePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    onward_route_link_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "OnwardRouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class PointProjection(ModifiedObject):
    class Meta:
        name = "pointProjection"

    project_to_point_ref: Optional[RefClassVersion] = field(
        default=None,
        metadata={
            "name": "ProjectToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ResponsibilityRoleAssignment(ModifiedObject):
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
    responsible_organisation_ref: Optional[RefClassVersion] = field(
        default=None,
        metadata={
            "name": "ResponsibleOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    responsible_area_ref: Optional[RefClassVersion] = field(
        default=None,
        metadata={
            "name": "ResponsibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class RoutePoint(ModifiedObject):
    class Meta:
        name = "routePoint"

    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class ServiceFacilitySet(ModifiedObject):
    class Meta:
        name = "serviceFacilitySet"

    extensions: Optional["ServiceFacilitySet.Extensions"] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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

    @dataclass
    class Extensions:
        access_facility_list: List[AccessFacilityEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "AccessFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "tokens": True,
            }
        )


@dataclass
class ServiceJourney(ModifiedObject):
    class Meta:
        name = "serviceJourney"

    validity_conditions: Optional[JourneyValidityConditions] = field(
        default=None,
        metadata={
            "name": "validityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    service_journey_pattern_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    time_demand_type_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_type_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[RefVersion] = field(
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
    data_source_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        }
    )


@dataclass
class StopArea(ModifiedObject):
    class Meta:
        name = "stopArea"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    private_code: Optional[PrivateCode] = field(
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
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )


@dataclass
class StopPointInJourneyPattern(OrderedObject):
    class Meta:
        name = "stopPointInJourneyPattern"

    scheduled_stop_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    onward_timing_link_ref: Optional[RefVersion] = field(
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
    destination_display_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TimingLink(ModifiedObject):
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
    from_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    operational_context_ref: Optional[RefVersion] = field(
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
class TimingPointInJourneyPattern(OrderedObject):
    class Meta:
        name = "timingPointInJourneyPattern"

    timing_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    onward_timing_link_ref: Optional[RefVersion] = field(
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
class TypeOfProductCategory(ModifiedObject):
    class Meta:
        name = "typeOfProductCategory"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[str] = field(
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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[Presentation] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class Vehicle(ModifiedObject):
    class Meta:
        name = "vehicle"

    branding_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )


@dataclass
class Version(ModifiedVersion):
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
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_type: Optional[TypeOfVersionEnumeration] = field(
        default=None,
        metadata={
            "name": "VersionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    derived_from_version_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "DerivedFromVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class DeadRunJourneyPattern(ModifiedObject):
    class Meta:
        name = "deadRunJourneyPattern"

    name: Optional[str] = field(
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
class DestinationDisplay(ModifiedObject):
    class Meta:
        name = "destinationDisplay"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    side_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "SideText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    front_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrontText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[Presentation] = field(
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
                "min_occurs": 1,
            }
        )


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
class InfrastructureFrame(VersionedFrame):
    class Meta:
        name = "infrastructureFrame"

    activation_points: Optional["InfrastructureFrame.ActivationPoints"] = field(
        default=None,
        metadata={
            "name": "activationPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
class ResponsibilitySet(ModifiedObject):
    class Meta:
        name = "responsibilitySet"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
class Route(ModifiedObject):
    class Meta:
        name = "route"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_ref: Optional[RefVersion] = field(
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
        }
    )
    points_in_sequence: Optional["Route.PointsInSequence"] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
class RouteLink(ModifiedObject):
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
    from_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    operational_context_ref: Optional[RefVersion] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
class ServiceCalendarFrame(VersionedFrame):
    class Meta:
        name = "serviceCalendarFrame"

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
class ServiceJourneyPattern(ModifiedObject):
    class Meta:
        name = "serviceJourneyPattern"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_ref: Optional[RefVersion] = field(
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
    destination_display_ref: Optional[RefVersion] = field(
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
class TimeDemandType(ModifiedObject):
    class Meta:
        name = "timeDemandType"

    name: Optional[str] = field(
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
class TimetableFrame(VersionedFrame):
    class Meta:
        name = "timetableFrame"

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
        operator_ref: Optional[RefVersion] = field(
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
class VehicleScheduleFrame(VersionedFrame):
    class Meta:
        name = "vehicleScheduleFrame"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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

    version: List[Version] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class ScheduledStopPoint(ModifiedObject):
    class Meta:
        name = "scheduledStopPoint"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    location: Optional[Location] = field(
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
            "required": True,
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
        stop_area_ref: Optional[RefVersion] = field(
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
        tariff_zone_ref: List[RefVersion] = field(
            default_factory=list,
            metadata={
                "name": "TariffZoneRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class TimingPoint(ModifiedObject):
    class Meta:
        name = "timingPoint"

    key_list: Optional[KeyList] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    location: Optional[Location] = field(
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
class VehicleType(ModifiedObject):
    class Meta:
        name = "vehicleType"

    extensions: Optional["VehicleType.Extensions"] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortName",
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
        }
    )
    private_code: Optional[PrivateCode] = field(
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
        }
    )
    passenger_capacity: Optional["VehicleType.PassengerCapacity"] = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_lift_or_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
        }
    )

    @dataclass
    class Extensions:
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

    @dataclass
    class PassengerCapacity:
        seating_capacity: Optional[int] = field(
            default=None,
            metadata={
                "name": "SeatingCapacity",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        standing_capacity: Optional[int] = field(
            default=None,
            metadata={
                "name": "StandingCapacity",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        special_place_capacity: Optional[int] = field(
            default=None,
            metadata={
                "name": "SpecialPlaceCapacity",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )


@dataclass
class ResourceFrame(VersionedFrame):
    class Meta:
        name = "resourceFrame"

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
            "required": True,
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
        }
    )
    vehicles: Optional["ResourceFrame.Vehicles"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
            default_factory=list,
            metadata={
                "name": "DataSource",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
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
                "min_occurs": 1,
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
        type_of_service: List[TypeOfService] = field(
            default_factory=list,
            metadata={
                "name": "TypeOfService",
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
    class Vehicles:
        vehicle: List[Vehicle] = field(
            default_factory=list,
            metadata={
                "name": "Vehicle",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Zones:
        administrative_zone: List[AdministrativeZone] = field(
            default_factory=list,
            metadata={
                "name": "AdministrativeZone",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )


@dataclass
class ServiceFrame(VersionedFrame):
    class Meta:
        name = "serviceFrame"

    route_points: Optional["ServiceFrame.RoutePoints"] = field(
        default=None,
        metadata={
            "name": "routePoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_links: Optional["ServiceFrame.RouteLinks"] = field(
        default=None,
        metadata={
            "name": "routeLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routes: Optional["ServiceFrame.Routes"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
class Frames:
    class Meta:
        name = "frames"

    resource_frame: List[ResourceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_frame: List[InfrastructureFrame] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_frame: List[ServiceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timetable_frame: List[TimetableFrame] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_frame: List[ServiceCalendarFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_schedule_frame: List[VehicleScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class CompositeFrame(ModifiedFrame):
    class Meta:
        name = "compositeFrame"

    frame_defaults: Optional[FrameDefaults] = field(
        default=None,
        metadata={
            "name": "FrameDefaults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    versions: Optional[Versions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    frames: Optional[Frames] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
        namespace = "http://www.netex.org.uk/netex"

    publication_timestamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicationTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "required": True,
        }
    )
    data_objects: Optional[DataObjects] = field(
        default=None,
        metadata={
            "name": "dataObjects",
            "type": "Element",
            "required": True,
        }
    )
    version: str = field(
        init=False,
        default="9.1.0",
        metadata={
            "type": "Attribute",
        }
    )
