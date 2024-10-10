import string
import struct
import platform
import os
from ctypes import *
from enum import Enum
from functools import wraps
import time

def pause():
    input("Press Enter to continue ...")

class OutputFunction(Enum):
    Output_Off = 0
    Output_Sine = 1
    Output_Triangle = 2
    Output_Square = 3
    Output_RectanglePulse = 4
    Output_TrianglePulse = 5
    Output_Exponential = 6
    Output_ECG2_27 = 7
    Output_IEC227W = 8
    Output_IEC251W = 9
    Output_JJG1041 = 10
    Output_JJG1041_HR = 11
    Output_JJG_Hysteresis = 12
    Output_ECG_File = 13
    Output_Custom_ECG = 14
    Output_YY1079_Ramp = 15
    Output_IEC247W = 16
    Output_ANE20000 = 17


class OutputLead(Enum):
    Lead_RA = 0
    Lead_LA = 1
    Lead_LL = 2
    Lead_V1 = 3
    Lead_V2 = 4
    Lead_V3 = 5
    Lead_V4 = 6
    Lead_V5 = 7
    Lead_V6 = 8


class SpecialWave227(Enum):
    IEC227W_3A_A1 = 0
    IEC227W_3B_A2 = 1
    IEC227W_3C_A3 = 2
    IEC227W_3D_A4 = 3
    IEC227W_4A_B1 = 4
    IEC227W_4A_B1x2 = 5
    IEC227W_4A_B1d2 = 6
    IEC227W_4B_B2 = 7
    IEC227W_4B_B2x2 = 8
    IEC227W_4B_B2d2 = 9


class SpecialWave251(Enum):
    CAL05000 = 0
    CAL10000 = 1
    CAL15000 = 2
    CAL20000 = 3
    CAL30000 = 4
    CAL50000 = 5
    CAL20002 = 6
    CAL20100 = 7
    CAL20110 = 8
    CAL20160 = 9
    CAL20200 = 10
    CAL20210 = 11
    CAL20260 = 12
    CAL20500 = 13
    CAL20502 = 14
    CAL40000 = 15


class SpecialWave247(Enum):
    test_pattern_1 = 0
    test_pattern_2 = 1
    test_pattern_3 = 2
    test_pattern_4 = 3
    test_pattern_5 = 4


class PacingPulse(Enum):
    SinglePulse = 0
    DoublePulse_150ms = 1
    DoublePulse_250ms = 2


class BaselineReset(Enum):
    Baseline_Off = 0
    Baseline_50Hz = 1
    Baseline_60Hz = 2
    Baseline_80Hz = 3
    Baseline_100Hz = 4


class ECG2_27_NoiseFreq(Enum):
    Noise_None = 0
    Noise_50Hz = 1
    Noise_60Hz = 2
    Noise_100Hz = 3
    Noise_120Hz = 4
    Noise_150Hz = 5
    Noise_180Hz = 6
    Noise_200Hz = 7
    Noise_240Hz = 8
    Noise_White = 9


class RespirationBaseline(Enum):
    Baseline_500 = 0
    Baseline_1000 = 1
    Baseline_1500 = 2
    Baseline_2000 = 3
    Baseline_2500 = 4


class LeadOffType(Enum):
    LeadOff_Short = 0
    LeadOff_10M = 1
    LeadOff_20M = 2
    LeadOff_Open = 3


class NST_Noise(Enum):
    NST_NONE = 0
    NST_EM = 1
    NST_BW = 2
    NST_MA = 3


class ECG2_27_NoiseFreq_E(Enum):
    Noise_None = 0
    Noise_50Hz = 1
    Noise_60Hz = 2
    Noise_White = 3


class LEDType(Enum):
    LEDTypeGreen = 0
    LEDTypeRed = 1
    LEDTypeIR = 2
    LEDTypeNone = 3


class PPGWaveformType(Enum):
    PPGWaveformTypeSine = 0
    PPGWaveformTypeTriangle = 1
    PPGWaveformTypeSquare = 2
    PPGWaveformTypePPG = 3


class SyncPulse(Enum):
    SyncPulseLEDOff = 0,
    SyncPulseSync = 1
    SyncPulseSyncOff = 2


class PPGInverted(Enum):
    PPGInvertedOff = 0
    PPGInvertedOn = 1


class PPGAmbientLightMode(Enum):
    PPGAmbientLightOff = 0
    PPGAmbientLight50Hz = 1
    PPGAmbientLight60Hz = 2
    PPGAmbientLight1KHz = 3
    PPGAmbientLight2KHz = 4
    PPGAmbientLight3KHz = 5
    PPGAmbientLight4KHz = 6
    PPGAmbientLight5KHz = 7
    PPGAmbientLight6KHz = 8
    PPGAmbientLight7KHz = 9
    PPGAmbientLight8KHz = 10
    PPGAmbientLight9KHz = 11
    PPGAmbientLight10KHz = 12
    PPGAmbientLightDirectCurrent = 13
    PPGAmbientLightSunLight = 14


class PPGSampling(Enum):
    Channel1PD = 0
    Channel2PD = 1
    Channel1Switch = 2
    Channel2Switch = 3


class HW_INFORMATION(Structure):
    _fields_ = [
        ('FWMajorVersion', c_int),
        ('FWMinorVersion', c_int),
        ('FWBuildVersion', c_int),
        ('FWBuildDate', c_int),
        ('HWMajorVersion', c_int),
        ('HWMinorVersion', c_int)
    ]


class MODEL_INFORMATION(Structure):
    _fields_ = [
        ('ProductName', c_char * 2),
        ('GenerationNumber', c_char),
        ('ModelNumber', c_char),
        ('SerialNumber', c_int),
        ('Year', c_int),
        ('LEDType1', c_int),
        ('LEDType2', c_int),
        ('LEDType3', c_int)
    ]

#
# SECG SDK Callback Type Definition
#
ConnectedCallback = CFUNCTYPE(None, c_bool)
OutputSignalCallback = CFUNCTYPE(None, c_double, c_double)
SyncFrequencyCallback = CFUNCTYPE(None, c_double)
SyncDCOffsetCallback = CFUNCTYPE(None, c_int)
SyncMainFunctionCallback = CFUNCTYPE(None, c_int)
SamplingCallback = CFUNCTYPE(None, c_int, c_int, c_int)

# SDK function decorator
def sdk_fn(api_name, args_type=None, return_type=None):
    def decorator_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cfn = getattr(args[0].sdk, api_name)
            cfn.argtypes = args_type
            cfn.restype = return_type

            if return_type == c_char_p:
                return cfn(*args[1:], **kwargs).decode('utf-8')
            else:
                return cfn(*args[1:], **kwargs)

        return wrapper
    return decorator_function


class SECG50:
    def __init__(self):
        self.path = self.get_lib_path()
        self.sdk = cdll.LoadLibrary(self.path)

    @staticmethod
    def get_lib_path():
        if platform.system() == 'Windows':
            if struct.calcsize("P") == 4:
                path = "./SDK_secg50/SECG50x86.dll"
            else:
                path = "./SDK_secg50/SECG50x64.dll"
        else:
            raise Exception("Unsupported System")

        return path

    #
    # Initialization & Cleanup
    #
    @sdk_fn("SECGInit", [ConnectedCallback], c_bool)
    def init(self, cb) -> c_bool:
        pass

    @sdk_fn("SECGConnect", [c_uint, c_uint], c_bool)
    def connect(self, port_number, milliseconds_timeout) -> c_bool:
        pass

    @sdk_fn("SECGFree", [], None)
    def free(self) -> None:
        pass

    @sdk_fn("SECGGetSDKVersion", [], c_char_p)
    def get_sdk_version(self) -> string:
        pass

    @sdk_fn("SECGReset", [], None)
    def reset(self) -> None:
        pass

    @sdk_fn("SECGIsConnected", [], c_bool)
    def is_connected(self) -> c_bool:
        pass

    @sdk_fn("SECGIsPPGConnected", [], c_bool)
    def is_ppg_connected(self) -> c_bool:
        pass

    #
    # Device Configurations
    #
    @sdk_fn("SECGGetDeviceInformation", [c_void_p], c_bool)   # other
    def get_device_information(self, model_info_p) -> c_bool:
        """
        :param model_info_p: [Out] the pointer of structure "MODEL_INFORMATION"
        :return: True if success
        """
        pass

    @sdk_fn("SECGGetPPGDeviceInformation", [c_void_p], c_bool)
    def get_ppg_information(self, model_info_p) -> c_bool:
        """
        :param model_info_p: [Out] the pointer of structure "MODEL_INFORMATION"
        :return: True if success
        """
        pass

    @sdk_fn("SECGGetHWInformation", [c_void_p], c_bool)
    def get_hw_information(self, hw_info_p) -> c_bool:
        """
        :param hw_info_p: [Out] the pointer of structure "HW_INFORMATION"
        :return: True if success
        """
        pass

    @sdk_fn("SECGGetSerialNumber", [], c_char_p)
    def get_serial_number(self):
        pass

    @sdk_fn("SECGGetPPGSerialNumber", [], c_char_p)
    def get_ppg_serial_number(self):
        pass

    @sdk_fn("SECGGetFWVersion", [], c_char_p)
    def get_fw_version(self):
        pass

    @sdk_fn("SECGGetHWVersion", [], c_char_p)
    def get_hw_version(self):
        pass

    @sdk_fn("SECGIsPlaying", [], c_bool)
    def is_playing(self) -> c_bool:
        pass

    #
    # Register callback functions
    #
    @sdk_fn("SECGRegisterOutputSignalCallback", [OutputSignalCallback, c_int], None)
    def register_output_signal_callback(self, cb, divider) -> None:
        pass

    @sdk_fn("SECGRegisterOutputPPGCallback", [c_int, OutputSignalCallback], None)
    def register_output_ppg_callback(self, led_type, cb) -> None:
        pass

    @sdk_fn("SECGRegisterSyncFrequencyCB", [SyncFrequencyCallback], c_void_p)
    def register_sync_frequency_callback(self, cb) -> c_void_p:
        pass

    @sdk_fn("SECGRegisterSyncDCOffsetCB", [SyncDCOffsetCallback], c_void_p)
    def register_sync_dc_offset_callback(self, cb) -> c_void_p:
        pass

    @sdk_fn("SECGRegisterSyncMainFunctionCB", [SyncMainFunctionCallback], c_void_p)
    def register_sync_main_function_callback(self, cb) -> c_void_p:
        pass

    #
    # waveform
    #
    @sdk_fn("SECGSetOutputFunction", [c_int], c_int)
    def set_output_function(self, func) -> c_int:
        pass

    @sdk_fn("SECGSetFrequency", [c_double], c_int)
    def set_frequency(self, freq) -> c_int:
        pass

    @sdk_fn("SECGSetAmplitude", [c_double], c_int)
    def set_amplitude(self, amp) -> c_int:
        pass

    @sdk_fn("SECGSetOutputLead", [c_int, c_bool], c_int)
    def set_output_lead(self, lead, on_off) -> c_int:
        pass

    @sdk_fn("SECGSetPulseWidth", [c_double], c_int)
    def set_pulse_width(self, width) -> c_int:
        pass

    @sdk_fn("SECGSetDCOffset", [c_int], c_int)
    def set_dc_offset(self, setting) -> c_int:
        pass

    @sdk_fn("SECGSetDCOffsetVariableMode", [c_bool], c_int)
    def set_dc_offset_variable_mode(self, on_off) -> c_int:
        pass

    #
    # customized ECG waveform
    #

    @sdk_fn("SECGSetPRInterval", [c_double], c_int)
    def set_pr_interval(self, time) -> c_int:
        pass

    @sdk_fn("SECGSetQTInterval", [c_double], c_int)
    def set_qt_interval(self, time) -> c_int:
        pass

    @sdk_fn("SECGSetPDuration", [c_double], c_int)
    def set_p_duration(self, time) -> c_int:
        pass

    @sdk_fn("SECGSetPWave", [c_double], c_int)
    def set_pwave(self, amp) -> c_int:
        pass

    @sdk_fn("SECGSetQRSDuration", [c_double], c_int)
    def set_qrs_duration(self, time) -> c_int:
        pass

    @sdk_fn("SECGSetSTDeviation", [c_double], c_int)
    def set_st_deviation(self, amp) -> c_int:
        pass

    @sdk_fn("SECGSetTWave", [c_double], c_int)
    def set_twave(self, amp) -> c_int:
        pass

    @sdk_fn("SECGSetECG2_27_Noise", [c_int, c_double], c_int)
    def set_ecg2_27_noise(self, freq, amp) -> c_int:
        pass

    #
    # pacing pulse
    #
    @sdk_fn("SECGSetPacingPulseMode", [c_int], c_int)
    def set_pacing_pulse_mode(self, mode) -> c_int:
        pass

    @sdk_fn("SECGSetPacingAmplitude", [c_double], c_int)
    def set_pacing_amplitude(self, amp) -> c_int:
        pass

    @sdk_fn("SECGSetPacingDuration", [c_double], c_int)
    def set_pacing_duration(self, time) -> time:
        pass

    @sdk_fn("SECGSetPacingRate", [c_uint], c_int)
    def set_pacing_rate(self, bpm) -> c_int:
        pass

    @sdk_fn("SECGSetOvershootAmplitude", [c_double], c_int)
    def set_pacing_overshoot_amplitude(self, amp) -> c_int:
        pass

    @sdk_fn("SECGSetOvershootTimeConstant", [c_uint], c_int)
    def set_pacing_overshoot_time_constant(self, time_constant) -> c_int:
        pass

    #
    # Respiration
    #
    @sdk_fn("SECGEnableRespiration", [c_bool], c_bool)
    def enable_respiration(self, on_off) -> c_bool:
        pass

    @sdk_fn("SECGSetRespiration", [c_int, c_int, c_int, c_int, c_int], c_bool)
    def set_respiration(self, variation, freq, ratio, baseline, apnea) -> c_bool:
        pass

    @sdk_fn("SECGSetRespirationAlgorithm", [c_int, c_int, c_int, c_int, c_int, c_int], c_bool)
    def set_respiration_modulation(self, freq, ratio, apnea, baseline, amp_mod, freq_mod) -> c_bool:
        pass

    @sdk_fn("SECGDisableRespireAlgorithm", [], None)
    def disable_respiration_modulation(self):
        pass

    #
    # Special waveforms
    #
    @sdk_fn("SECGSetSpecialWave227", [c_int], c_int)
    def set_special_waveform_227(self, spec) -> c_int:
        pass

    @sdk_fn("SECGSetSpecialWave251", [c_int], c_int)
    def set_special_waveform_251(self, spec) -> c_int:
        pass

    @sdk_fn("SECGSetSpecialWave247", [c_int], c_int)
    def set_special_waveform_247(self, spec) -> c_int:
        pass

    @sdk_fn("SECGSetSpecialWaveformLoop", [c_bool], c_void_p)
    def set_special_waveform_loop(self, loop) -> c_void_p:
        pass

    #
    # Load files
    #
    @sdk_fn("SECGLoadECGtxt", [c_char_p, c_int], c_int)
    def load_ecg_txt(self, file, channel) -> c_int:
        pass

    @sdk_fn("SECGLoadECGedf", [c_char_p, c_int], c_int)
    def load_ecg_edf(self, file, channel) -> c_int:
        pass

    @sdk_fn("SECGLoadECGdat", [c_char_p, c_char_p, c_int], c_int)
    def load_ecg_dat(self, header_file, signal_file, channel) -> c_int:
        pass

    #
    # Advanced features
    #
    @sdk_fn("SECGSetNSTNoise", [c_int, c_double], c_int)
    def set_nst_noise(self, type, gain) -> c_int:
        pass

    @sdk_fn("SECGSetFrequencyScanSine", [c_bool, c_double, c_double, c_int], c_int)
    def set_frequency_scan_sine(self, on_off, start_freq, stop_freq, duration) -> c_int:
        pass

    @sdk_fn("SECGSetFrequencyScanECG", [c_bool], c_int)
    def set_frequency_scan_ecg(self, on_off) -> c_int:
        pass

    @sdk_fn("SECGSetLeadOff", [c_int], c_bool)
    def set_lead_off(self, lead_off_type) -> c_bool:
        pass

    #
    # PPG Output
    #

    @sdk_fn("SECGEnablePPGOutput", [c_int, c_bool], c_int)
    def enable_ppg_output(self, type, onoff) -> c_int:
        pass

    @sdk_fn("SECGEnableECGOutput", [c_bool], c_int)
    def enable_ecg_output(self, onoff) -> c_int:
        pass

    @sdk_fn("SECGSetPPGStandardWaveform", [c_int, c_int, c_int, c_int, c_double, c_double, c_double], c_int)
    def set_ppg_standard_waveform(self, led_type, waveform_type, sync, inverted, freq, dc, ac) -> c_int:
        pass

    @sdk_fn("SECGSetPPGRawData", [c_int, c_int, c_int, c_int, POINTER(c_double), POINTER(c_double), c_double], c_int)
    def set_ppg_raw_data(self, led_type, sync, inverted, size, dc_array, ac_array, sample_rate) -> c_int:
        pass

    @sdk_fn("SECGClearPPGWaveform", [c_int], None)
    def clear_ppg_raw_data(self, led_type) -> None:
        pass

    @sdk_fn("SECGSetPTTp", [c_int], None)
    def set_pttp(self, pttp) -> None:
        pass

    @sdk_fn("SECGSetPPGRespirationAlgorithm", [c_int, c_int, c_int], c_int)
    def set_ppg_respiration_modulation(self, baseline, amplitude, frequency) -> c_int:
        pass

    @sdk_fn("SECGSetLEDAmbientLightMode", [c_int], c_int)
    def set_led_ambient_light_mode(self, mode) -> c_int:
        pass

    @sdk_fn("SECGEnablePPGSampling", [c_int, SamplingCallback], c_int)
    def enabled_ppg_sampling(self, channel, callback) -> c_int:
        pass

    @sdk_fn("SECGDisablePPGSampling", [], c_int)
    def disable_ppg_sampling(self) -> c_int:
        pass

    @sdk_fn("SECGStartPPGSampling", [], c_int)
    def start_ppg_sampling(self) -> c_int:
        pass

    @sdk_fn("SECGStopPPGSampling", [], None)
    def stop_ppg_sampling(self):
        pass


