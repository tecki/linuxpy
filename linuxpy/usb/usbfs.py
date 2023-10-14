#
# This file is part of the linuxpy project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

# This file has been generated by linuxpy.codegen.usbfs
# Date: 2023-10-14 09:25:59.728461
# System: Linux
# Release: 6.2.0-34-generic
# Version: #34~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 13:12:03 UTC 2

import enum

from linuxpy.ioctl import IO as _IO, IOR as _IOR, IOW as _IOW, IOWR as _IOWR
from linuxpy.ctypes import (
    u8,
    i8,
    u16,
    i16,
    u32,
    i32,
    u64,
    i64,
    cuint,
    cint,
    cchar,
    cvoidp,
)
from linuxpy.ctypes import Struct, Union, POINTER


class URBType(enum.IntEnum):
    ISO = 0x0
    INTERRUPT = 0x1
    CONTROL = 0x2
    BULK = 0x3


class URB(enum.IntFlag):
    SHORT_NOT_OK = 0x1
    ISO_ASAP = 0x2
    BULK_CONTINUATION = 0x4
    NO_FSBR = 0x20  # Not used
    ZERO_PACKET = 0x40
    NO_INTERRUPT = 0x80


class Capability(enum.IntFlag):
    ZERO_PACKET = 0x1
    BULK_CONTINUATION = 0x2
    NO_PACKET_SIZE_LIM = 0x4
    BULK_SCATTER_GATHER = 0x8
    REAP_AFTER_DISCONNECT = 0x10
    MMAP = 0x20
    DROP_PRIVILEGES = 0x40
    CONNINFO_EX = 0x80
    SUSPEND = 0x100


class DisconnectClaim(enum.IntFlag):
    IF_DRIVER = 0x1
    EXCEPT_DRIVER = 0x2


class Direction(enum.IntEnum):
    OUT = 0  # to device
    IN = 0x80  # to host


class RequestType(enum.IntEnum):
    MASK = 0x03 << 5
    STANDARD = 0x00 << 5
    CLASS = 0x01 << 5
    VENDOR = 0x02 << 5
    RESERVED = 0x03 << 5
    _USB_TYPE_C_BRIDGE = 0x12


class Recipient(enum.IntEnum):
    MASK = 0x1F
    DEVICE = 0x0
    INTERFACE = 0x1
    ENDPOINT = 0x2
    OTHER = 0x3
    PORT = 0x4
    RPIPE = 0x5


class Request(enum.IntEnum):
    GET_STATUS = 0x0
    CLEAR_FEATURE = 0x1
    SET_FEATURE = 0x3
    SET_ADDRESS = 0x5
    GET_DESCRIPTOR = 0x6
    SET_DESCRIPTOR = 0x7
    GET_CONFIGURATION = 0x8
    SET_CONFIGURATION = 0x9
    GET_INTERFACE = 0xA
    SET_INTERFACE = 0xB
    SYNCH_FRAME = 0xC
    SET_SEL = 0x30
    SET_ISOCH_DELAY = 0x31
    SET_ENCRYPTION = 0x0D  # Wireless USB
    GET_ENCRYPTION = 0xE
    RPIPE_ABORT = 0xE
    SET_HANDSHAKE = 0xF
    RPIPE_RESET = 0xF
    GET_HANDSHAKE = 0x10
    SET_CONNECTION = 0x11
    SET_SECURITY_DATA = 0x12
    GET_SECURITY_DATA = 0x13
    SET_WUSB_DATA = 0x14
    LOOPBACK_DATA_WRITE = 0x15
    LOOPBACK_DATA_READ = 0x16
    SET_INTERFACE_DS = 0x17
    GET_PARTNER_PDO = 0x14
    GET_BATTERY_STATUS = 0x15
    SET_PDO = 0x16
    GET_VDM = 0x17
    SEND_VDM = 0x18


class Device(enum.IntEnum):
    SELF_POWERED = 0  # (read only)
    REMOTE_WAKEUP = 1  # dev may initiate wakeup
    TEST_MODE = 2  # (wired high speed only)
    BATTERY = 2  # (wireless)
    B_HNP_ENABLE = 3  # (otg) dev may initiate HNP
    WUSB_DEVICE = 3  # (wireless)
    A_HNP_SUPPORT = 4  # (otg) RH port supports HNP
    A_ALT_HNP_SUPPORT = 5  # (otg) other RH port does
    DEBUG_MODE = 6  # (special devices only)
    U1_ENABLE = 48  # dev may initiate U1 transition
    U2_ENABLE = 49  # dev may initiate U2 transition
    LTM_ENABLE = 50  # dev may send LTM
    BATTERY_WAKE_MASK = 0x28
    OS_IS_PD_AWARE = 0x29
    POLICY_MODE = 0x2A
    CHARGING_POLICY = 0x36


class Test(enum.IntEnum):
    J = 0x1
    K = 0x2
    SE0_NAK = 0x3
    PACKET = 0x4
    FORCE_ENABLE = 0x5


class StatusType(enum.IntEnum):
    STANDARD = 0x0
    PTM = 0x1


class UsbipDeviceStatus(enum.IntEnum):
    SDEV_ST_AVAILABLE = 1
    SDEV_ST_USED = 2
    SDEV_ST_ERROR = 3
    VDEV_ST_NULL = 4
    VDEV_ST_NOTASSIGNED = 5
    VDEV_ST_USED = 6
    VDEV_ST_ERROR = 7


class UsbDeviceSpeed(enum.IntEnum):
    UNKNOWN = 0
    LOW = 1
    FULL = 2
    HIGH = 3
    WIRELESS = 4
    SUPER = 5
    SUPER_PLUS = 6


class UsbDeviceState(enum.IntEnum):
    NOTATTACHED = 0
    ATTACHED = 1
    POWERED = 2
    RECONNECTING = 3
    UNAUTHENTICATED = 4
    DEFAULT = 5
    ADDRESS = 6
    CONFIGURED = 7
    SUSPENDED = 8


class Usb3LinkState(enum.IntEnum):
    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3


class HubLedMode(enum.IntEnum):
    AUTO = 0
    CYCLE = 1
    GREEN_BLINK = 2
    GREEN_BLINK_OFF = 3
    AMBER_BLINK = 4
    AMBER_BLINK_OFF = 5
    ALT_BLINK = 6
    ALT_BLINK_OFF = 7


class usbdevfs_ctrltransfer(Struct):
    pass


usbdevfs_ctrltransfer._fields_ = [
    ("bRequestType", u8),
    ("bRequest", u8),
    ("wValue", u16),
    ("wIndex", u16),
    ("wLength", u16),
    ("timeout", cuint),
    ("data", POINTER(None)),
]


class usbdevfs_bulktransfer(Struct):
    pass


usbdevfs_bulktransfer._fields_ = [
    ("ep", cuint),
    ("len", cuint),
    ("timeout", cuint),
    ("data", POINTER(None)),
]


class usbdevfs_setinterface(Struct):
    pass


usbdevfs_setinterface._fields_ = [("interface", cuint), ("altsetting", cuint)]


class usbdevfs_disconnectsignal(Struct):
    pass


usbdevfs_disconnectsignal._fields_ = [("signr", cuint), ("context", POINTER(None))]


class usbdevfs_getdriver(Struct):
    pass


usbdevfs_getdriver._fields_ = [("interface", cuint), ("driver", cchar * 256)]


class usbdevfs_connectinfo(Struct):
    pass


usbdevfs_connectinfo._fields_ = [("devnum", cuint), ("slow", u8)]


class usbdevfs_conninfo_ex(Struct):
    pass


usbdevfs_conninfo_ex._fields_ = [
    ("size", cuint),
    ("busnum", cuint),
    ("devnum", cuint),
    ("speed", cuint),
    ("num_ports", u8),
    ("ports", cchar * 7),
]


class usbdevfs_iso_packet_desc(Struct):
    pass


usbdevfs_iso_packet_desc._fields_ = [
    ("length", cuint),
    ("actual_length", cuint),
    ("status", cuint),
]


class usbdevfs_urb(Struct):
    class M1(Union):
        pass

    M1._fields_ = [("number_of_packets", cint), ("stream_id", cuint)]

    _anonymous_ = ("m1",)


usbdevfs_urb._fields_ = [
    ("type", u8),
    ("endpoint", u8),
    ("status", cint),
    ("flags", cuint),
    ("buffer", POINTER(None)),
    ("buffer_length", cint),
    ("actual_length", cint),
    ("start_frame", cint),
    ("m1", usbdevfs_urb.M1),
    ("error_count", cint),
    ("signr", cuint),
    ("usercontext", POINTER(None)),
    ("iso_frame_desc", usbdevfs_iso_packet_desc * 0),
]


class usbdevfs_ioctl(Struct):
    pass


usbdevfs_ioctl._fields_ = [
    ("ifno", cint),
    ("ioctl_code", cint),
    ("data", POINTER(None)),
]


class usbdevfs_hub_portinfo(Struct):
    _pack_ = True
    pass


usbdevfs_hub_portinfo._fields_ = [("nports", cchar), ("port", cchar * 127)]


class usbdevfs_disconnect_claim(Struct):
    pass


usbdevfs_disconnect_claim._fields_ = [
    ("interface", cuint),
    ("flags", cuint),
    ("driver", cchar * 256),
]


class usbdevfs_streams(Struct):
    pass


usbdevfs_streams._fields_ = [
    ("num_streams", cuint),
    ("num_eps", cuint),
    ("eps", cchar * 0),
]


class usb_ctrlrequest(Struct):
    _pack_ = True
    pass


usb_ctrlrequest._fields_ = [
    ("bRequestType", u8),
    ("bRequest", u8),
    ("wValue", u16),
    ("wIndex", u16),
    ("wLength", u16),
]


class usb_descriptor_header(Struct):
    _pack_ = True
    pass


usb_descriptor_header._fields_ = [("bLength", u8), ("bDescriptorType", u8)]


class usb_device_descriptor(Struct):
    _pack_ = True
    pass


usb_device_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bcdUSB", u16),
    ("bDeviceClass", u8),
    ("bDeviceSubClass", u8),
    ("bDeviceProtocol", u8),
    ("bMaxPacketSize0", u8),
    ("idVendor", u16),
    ("idProduct", u16),
    ("bcdDevice", u16),
    ("iManufacturer", u8),
    ("iProduct", u8),
    ("iSerialNumber", u8),
    ("bNumConfigurations", u8),
]


class usb_config_descriptor(Struct):
    _pack_ = True
    pass


usb_config_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("wTotalLength", u16),
    ("bNumInterfaces", u8),
    ("bConfigurationValue", u8),
    ("iConfiguration", u8),
    ("bmAttributes", u8),
    ("bMaxPower", u8),
]


class usb_string_descriptor(Struct):
    _pack_ = True
    pass


usb_string_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("wData", u16 * 1),
]


class usb_interface_descriptor(Struct):
    _pack_ = True
    pass


usb_interface_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bInterfaceNumber", u8),
    ("bAlternateSetting", u8),
    ("bNumEndpoints", u8),
    ("bInterfaceClass", u8),
    ("bInterfaceSubClass", u8),
    ("bInterfaceProtocol", u8),
    ("iInterface", u8),
]


class usb_endpoint_descriptor(Struct):
    _pack_ = True
    pass


usb_endpoint_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bEndpointAddress", u8),
    ("bmAttributes", u8),
    ("wMaxPacketSize", u16),
    ("bInterval", u8),
    ("bRefresh", u8),
    ("bSynchAddress", u8),
]


class usb_ssp_isoc_ep_comp_descriptor(Struct):
    _pack_ = True
    pass


usb_ssp_isoc_ep_comp_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("wReseved", u16),
    ("dwBytesPerInterval", cuint),
]


class usb_ss_ep_comp_descriptor(Struct):
    _pack_ = True
    pass


usb_ss_ep_comp_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bMaxBurst", u8),
    ("bmAttributes", u8),
    ("wBytesPerInterval", u16),
]


class usb_qualifier_descriptor(Struct):
    _pack_ = True
    pass


usb_qualifier_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bcdUSB", u16),
    ("bDeviceClass", u8),
    ("bDeviceSubClass", u8),
    ("bDeviceProtocol", u8),
    ("bMaxPacketSize0", u8),
    ("bNumConfigurations", u8),
    ("bRESERVED", u8),
]


class usb_otg_descriptor(Struct):
    _pack_ = True
    pass


usb_otg_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bmAttributes", u8),
]


class usb_otg20_descriptor(Struct):
    _pack_ = True
    pass


usb_otg20_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bmAttributes", u8),
    ("bcdOTG", u16),
]


class usb_debug_descriptor(Struct):
    _pack_ = True
    pass


usb_debug_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDebugInEndpoint", u8),
    ("bDebugOutEndpoint", u8),
]


class usb_interface_assoc_descriptor(Struct):
    _pack_ = True
    pass


usb_interface_assoc_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bFirstInterface", u8),
    ("bInterfaceCount", u8),
    ("bFunctionClass", u8),
    ("bFunctionSubClass", u8),
    ("bFunctionProtocol", u8),
    ("iFunction", u8),
]


class usb_security_descriptor(Struct):
    _pack_ = True
    pass


usb_security_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("wTotalLength", u16),
    ("bNumEncryptionTypes", u8),
]


class usb_key_descriptor(Struct):
    _pack_ = True
    pass


usb_key_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("tTKID", cchar * 3),
    ("bReserved", u8),
    ("bKeyData", cchar * 0),
]


class usb_encryption_descriptor(Struct):
    _pack_ = True
    pass


usb_encryption_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bEncryptionType", u8),
    ("bEncryptionValue", u8),
    ("bAuthKeyIndex", u8),
]


class usb_bos_descriptor(Struct):
    _pack_ = True
    pass


usb_bos_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("wTotalLength", u16),
    ("bNumDeviceCaps", u8),
]


class usb_dev_cap_header(Struct):
    _pack_ = True
    pass


usb_dev_cap_header._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
]


class usb_wireless_cap_descriptor(Struct):
    _pack_ = True
    pass


usb_wireless_cap_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("bmAttributes", u8),
    ("wPHYRates", u16),
    ("bmTFITXPowerInfo", u8),
    ("bmFFITXPowerInfo", u8),
    ("bmBandGroup", u16),
    ("bReserved", u8),
]


class usb_ext_cap_descriptor(Struct):
    _pack_ = True
    pass


usb_ext_cap_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("bmAttributes", cuint),
]


class usb_ss_cap_descriptor(Struct):
    _pack_ = True
    pass


usb_ss_cap_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("bmAttributes", u8),
    ("wSpeedSupported", u16),
    ("bFunctionalitySupport", u8),
    ("bU1devExitLat", u8),
    ("bU2DevExitLat", u16),
]


class usb_ss_container_id_descriptor(Struct):
    _pack_ = True
    pass


usb_ss_container_id_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("bReserved", u8),
    ("ContainerID", cchar * 16),
]


class usb_ssp_cap_descriptor(Struct):
    _pack_ = True
    pass


usb_ssp_cap_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("bReserved", u8),
    ("bmAttributes", cuint),
    ("wFunctionalitySupport", u16),
    ("wReserved", u16),
    ("bmSublinkSpeedAttr", cuint * 1),
]


class usb_pd_cap_descriptor(Struct):
    _pack_ = True
    pass


usb_pd_cap_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("bReserved", u8),
    ("bmAttributes", cuint),
    ("bmProviderPorts", u16),
    ("bmConsumerPorts", u16),
    ("bcdBCVersion", u16),
    ("bcdPDVersion", u16),
    ("bcdUSBTypeCVersion", u16),
]


class usb_pd_cap_battery_info_descriptor(Struct):
    _pack_ = True
    pass


usb_pd_cap_battery_info_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("iBattery", u8),
    ("iSerial", u8),
    ("iManufacturer", u8),
    ("bBatteryId", u8),
    ("bReserved", u8),
    ("dwChargedThreshold", cuint),
    ("dwWeakThreshold", cuint),
    ("dwBatteryDesignCapacity", cuint),
    ("dwBatteryLastFullchargeCapacity", cuint),
]


class usb_pd_cap_consumer_port_descriptor(Struct):
    _pack_ = True
    pass


usb_pd_cap_consumer_port_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("bReserved", u8),
    ("bmCapabilities", u8),
    ("wMinVoltage", u16),
    ("wMaxVoltage", u16),
    ("wReserved", u16),
    ("dwMaxOperatingPower", cuint),
    ("dwMaxPeakPower", cuint),
    ("dwMaxPeakPowerTime", cuint),
]


class usb_pd_cap_provider_port_descriptor(Struct):
    _pack_ = True
    pass


usb_pd_cap_provider_port_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
    ("bReserved1", u8),
    ("bmCapabilities", u8),
    ("bNumOfPDObjects", u8),
    ("bReserved2", u8),
    ("wPowerDataObject", POINTER(cuint)),
]


class usb_ptm_cap_descriptor(Struct):
    _pack_ = True
    pass


usb_ptm_cap_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bDevCapabilityType", u8),
]


class usb_wireless_ep_comp_descriptor(Struct):
    _pack_ = True
    pass


usb_wireless_ep_comp_descriptor._fields_ = [
    ("bLength", u8),
    ("bDescriptorType", u8),
    ("bMaxBurst", u8),
    ("bMaxSequence", u8),
    ("wMaxStreamDelay", u16),
    ("wOverTheAirPacketSize", u16),
    ("bOverTheAirInterval", u8),
    ("bmCompAttributes", u8),
]


class usb_handshake(Struct):
    _pack_ = True
    pass


usb_handshake._fields_ = [
    ("bMessageNumber", u8),
    ("bStatus", u8),
    ("tTKID", cchar * 3),
    ("bReserved", u8),
    ("CDID", cchar * 16),
    ("nonce", cchar * 16),
    ("MIC", cchar * 8),
]


class usb_connection_context(Struct):
    _pack_ = True
    pass


usb_connection_context._fields_ = [
    ("CHID", cchar * 16),
    ("CDID", cchar * 16),
    ("CK", cchar * 16),
]


class usb_set_sel_req(Struct):
    _pack_ = True
    pass


usb_set_sel_req._fields_ = [
    ("u1_sel", u8),
    ("u1_pel", u8),
    ("u2_sel", u16),
    ("u2_pel", u16),
]


class usb_port_status(Struct):
    _pack_ = True
    pass


usb_port_status._fields_ = [
    ("wPortStatus", u16),
    ("wPortChange", u16),
    ("dwExtPortStatus", cuint),
]


class usb_hub_status(Struct):
    _pack_ = True
    pass


usb_hub_status._fields_ = [("wHubStatus", u16), ("wHubChange", u16)]


class usb_hub_descriptor(Struct):
    _pack_ = True

    class M1(Union):
        _pack_ = True

        class M1(Struct):
            _pack_ = True
            pass

        M1._fields_ = [("DeviceRemovable", cchar * 4), ("PortPwrCtrlMask", cchar * 4)]

        class M2(Struct):
            _pack_ = True
            pass

        M2._fields_ = [
            ("bHubHdrDecLat", u8),
            ("wHubDelay", u16),
            ("DeviceRemovable", u16),
        ]

    M1._fields_ = [("hs", M1.M1), ("ss", M1.M2)]


usb_hub_descriptor._fields_ = [
    ("bDescLength", u8),
    ("bDescriptorType", u8),
    ("bNbrPorts", u8),
    ("wHubCharacteristics", u16),
    ("bPwrOn2PwrGood", u8),
    ("bHubContrCurrent", u8),
    ("u", usb_hub_descriptor.M1),
]


# Extra structs not found on header files


class usb_hid_descriptor(Struct):
    _fields_ = [
        ("bLength", u8),
        ("bDescriptorType", u8),
        ("bcdHID", u16),
        ("bCountryCode", u8),
        ("bNumDescriptors", u8),
        ("bClassDescriptorType", u8),
        ("wClassDescriptorLength", u16),
    ]


class IOC(enum.IntEnum):
    CONTROL = _IOWR("U", 0, usbdevfs_ctrltransfer)
    BULK = _IOWR("U", 2, usbdevfs_bulktransfer)
    RESETEP = _IOR("U", 3, cuint)
    SETINTERFACE = _IOR("U", 4, usbdevfs_setinterface)
    SETCONFIGURATION = _IOR("U", 5, cuint)
    GETDRIVER = _IOW("U", 8, usbdevfs_getdriver)
    SUBMITURB = _IOR("U", 10, usbdevfs_urb)
    DISCARDURB = _IO("U", 11)
    REAPURB = _IOW("U", 12, cvoidp)
    REAPURBNDELAY = _IOW("U", 13, cvoidp)
    DISCSIGNAL = _IOR("U", 14, usbdevfs_disconnectsignal)
    CLAIMINTERFACE = _IOR("U", 15, cuint)
    RELEASEINTERFACE = _IOR("U", 16, cuint)
    CONNECTINFO = _IOW("U", 17, usbdevfs_connectinfo)
    IOCTL = _IOWR("U", 18, usbdevfs_ioctl)
    HUB_PORTINFO = _IOR("U", 19, usbdevfs_hub_portinfo)
    RESET = _IO("U", 20)
    CLEAR_HALT = _IOR("U", 21, cuint)
    DISCONNECT = _IO("U", 22)
    CONNECT = _IO("U", 23)
    CLAIM_PORT = _IOR("U", 24, cuint)
    RELEASE_PORT = _IOR("U", 25, cuint)
    GET_CAPABILITIES = _IOR("U", 26, u32)
    DISCONNECT_CLAIM = _IOR("U", 27, usbdevfs_disconnect_claim)
    ALLOC_STREAMS = _IOR("U", 28, usbdevfs_streams)
    FREE_STREAMS = _IOR("U", 29, usbdevfs_streams)
    DROP_PRIVILEGES = _IOW("U", 30, u32)
    GET_SPEED = _IO("U", 31)
    FORBID_SUSPEND = _IO("U", 33)
    ALLOW_SUSPEND = _IO("U", 34)
    WAIT_FOR_RESUME = _IO("U", 35)
