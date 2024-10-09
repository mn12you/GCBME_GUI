// WhaleTeqSECG5_SDK.h
#pragma once

/*! @mainpage WhaleTeq SECG5.0 API Documentation
 *  @version 2.0.8
 */


///@cond
#ifndef WHALETEQ_API
#  if defined(LINUX_GCC) || defined(ANDROID) || defined(__APPLE__)
#    define WHALETEQ_API
#  else
#    define WHALETEQ_API extern "C" __declspec(dllimport)
#  endif
#endif
///@endcond


enum OutputFunction_E {
    Output_Off = 0,         //!< Stop output
    Output_Sine,            //!< Sine
    Output_Triangle,        //!< Triangle
    Output_Square,          //!< Square
    Output_RectanglePulse,  //!< Rectangle Pulse
    Output_TrianglePulse,   //!< Triangle Pulse
    Output_Exponential,     //!< Exponential
    Output_ECG2_27,         //!< ECG 2-27 waveform
    Output_IEC227W,         //!< IEC60601-2-27 standard ECG waveform @see SECGSetSpecialWave227
    Output_IEC251W,         //!< IEC60601-2-25 standard ECG waveform @see SECGSetSpecialWave251
    Output_JJG1041,
    Output_JJG1041_HR,
    Output_JJG_Hysteresis,
    Output_ECG_File,        //!< ECG raw data file @see SECGLoadECGtxt
    Output_Custom_ECG,      //!< ECG customized waveform
    Output_YY1079_Ramp,
    Output_IEC247W,         //!< IEC60601-2-47 HRV pattern @see SECGSetSpecialWave247
    Output_ANE20000
};

enum SpecialWave227_E {
    IEC227W_3A_A1 = 0,      //!< AAMI 3A / IEC A1
    IEC227W_3B_A2,          //!< AAMI 3B / IEC A2
    IEC227W_3C_A3,          //!< AAMI 3C / IEC A3
    IEC227W_3D_A4,          //!< AAMI 3D / IEC A4
    IEC227W_4A_B1,          //!< AAMI 4A / IEC B1
    IEC227W_4A_B1x2,        //!< AAMI 4A / IEC B1 x 2
    IEC227W_4A_B1d2,        //!< AAMI 4A / IEC B1 / 2
    IEC227W_4B_B2,          //!< AAMI 4B / IEC B2
    IEC227W_4B_B2x2,        //!< AAMI 4B / IEC B2 x 2
    IEC227W_4B_B2d2,        //!< AAMI 4B / IEC B2 / 2
};

enum SpecialWave251_E {
    CAL05000 = 0,           //!< CAL05000
    CAL10000,               //!< CAL10000
    CAL15000,               //!< CAL15000
    CAL20000,               //!< CAL20000
    CAL30000,               //!< CAL30000
    CAL50000,               //!< CAL50000
    CAL20002,               //!< CAL20002
    CAL20100,               //!< CAL20100
    CAL20110,               //!< CAL20110
    CAL20160,               //!< CAL20160
    CAL20200,               //!< CAL20200
    CAL20210,               //!< CAL20210
    CAL20260,               //!< CAL20260
    CAL20500,               //!< CAL20500
    CAL20502,               //!< CAL20502
    CAL40000                //!< CAL40000
};

enum SpecialWave247_E {
    TEST_PATTERN_1 = 0,     //!< Test Pattern 1 @details Triangle pulse 1Hz, 1.0mV, pulse width 100ms, total 1 minute
    TEST_PATTERN_2,         //!< Test Pattern 2 @details RRI average 0.8s, RRI variation 35ms, frequency variation 0.25Hz, total 1 minute
    TEST_PATTERN_3,         //!< Test Pattern 3 @details RRI average 1.0s, RRI variation 70ms, frequency variation 0.10Hz, total 1 minute
    TEST_PATTERN_4,         //!< Test Pattern 4 @details RRI average 3.0s, RRI variation 280ms, frequency variation 0.03333Hz, total 1 minute
    TEST_PATTERN_5          //!< Test Pattern 5 @details RRI average 1.5s, RRI variation 140ms, frequency variation 0.000278Hz, total 1 hour
};

enum OutputLead_E {
    Lead_RA = 0,            //!< RA
    Lead_LA,                //!< LA
    Lead_LL,                //!< LL
    Lead_V1,                //!< V1
    Lead_V2,                //!< V2
    Lead_V3,                //!< V3
    Lead_V4,                //!< V4
    Lead_V5,                //!< V5
    Lead_V6                 //!< V6
};

/// <summary>
/// CopyRight: physionet.org
/// Source: https://physionet.org/content/nstdb/1.0.0/
/// </summary>
enum NST_NOISE_E {
    NST_NONE = 0,           //!< No NST noise
    NST_EM = 1,             //!< Electrode Motion Artifact
    NST_BW = 2,             //!< Baseline Wander
    NST_MA = 3              //!< Muscle Noise
};

enum PacingPulse_E {
    SinglePulse = 0,        //!< Single Pulse
    DoublePulse_150ms,      //!< Double Pulse with interval 150ms
    DoublePulse_250ms       //!< Double Pulse with interval 250ms
};

enum BaselineReset_E {
    Baseline_Off = 0,       //!< Baseline reset test off
    Baseline_50Hz,          //!< Baseline reset test in 50Hz
    Baseline_60Hz,          //!< Baseline reset test in 60Hz
    Baseline_80Hz,          //!< Baseline reset test in 80Hz
    Baseline_100Hz          //!< Baseline reset test in 100Hz
};

enum ECG2_27_NoiseFreq_E {
    Noise_None = 0,         //!< No Noise
    Noise_50Hz,             //!< 50Hz Noise
    Noise_60Hz,             //!< 60Hz Noise
    Noise_100Hz,            //!< 100Hz Noise
    Noise_120Hz,            //!< 120Hz Noise
    Noise_150Hz,            //!< 150Hz Noise
    Noise_180Hz,            //!< 180Hz Noise
    Noise_200Hz,            //!< 200Hz Noise
    Noise_240Hz,            //!< 240Hz Noise
    Noise_White             //!< White Noise
};

enum LeadOff_Type_E {
    LeadOff_Short = 0,      //!< <tt>default</tt>
    LeadOff_10M = 1,        //!< with 10M ohm output resistor
    LeadOff_20M = 2,        //!< with 20M ohm output resistor
    LeadOff_Open = 3        //!< output lead open
};

/// @anchor struct MODEL_INFORMATION
/// @brief Define a structure of the device model; for C code, you can get the serial number by the format:
///        ("W%c%c%02X%02X-%02d%04d", ProductName[0], ProductName[1], GenerationNumber, ModelNumber, Year, SerialNumber)
typedef struct {
    char            ProductName[2];
    unsigned char   GenerationNumber;
    unsigned char   ModelNumber;
    int             SerialNumber;       //!< device serial number
    int             Year;               //!< 0x11 = 2017
    int             LEDType1;           //!< enum ::LEDType of channel-1
    int             LEDType2;           //!< enum ::LEDType of channel-2
    int             LEDType3;           //!< enum ::LEDType of channel-3
} MODEL_INFORMATION;

/// @anchor struct HW_INFORMATION
/// @brief Define a structure of device hw and fw information
/// @details
/// * FW version: major.minor.build.day (ex: version 1.3.12.04)
/// * HW version: major.minor (ex: version 4.1)
typedef struct {
    int FWMajorVersion;     //!< FW major version
    int FWMinorVersion;     //!< FW minor version
    int FWBuildVersion;     //!< FW build version
    int FWBuildDate;        //!< FW build date
    int HWMajorVersion;     //!< HW major version
    int HWMinorVersion;     //!< HW minor version
} HW_INFORMATION;

/// @fn ConnectedCallback
/// @brief Called when the device is connected or disconnected
///
/// @param connected  true if connected; otherwise, it's false
typedef void (*ConnectedCallback) (bool connected);


/// @fn OutputSignalCallback
/// @brief Callback the time and amplitude of every sampling points
///
/// @param time       from the output signal changed, in second
/// @param amplitude  of the output voltage, in mV
///
typedef void (*OutputSignalCallback) (double time, double amplitude);

/// @fn SyncDCOffsetCallback
/// @brief Callback dc offset value during "Ramp"
///
/// @param dcOffset  to callback in mV
///
/// @see ::SECGRegisterSyncDCOffsetCB
/// @see ::Output_YY1079_Ramp
typedef void (*SyncDCOffsetCallback) (int dcOffset);

/// @fn SyncMainFuncCallback
/// @brief Callback main function during frequency scanning
///
/// @param func  to callback current main function in type ::OutputFunction_E
///
/// @see ::SECGRegisterSyncMainFunctionCB
typedef void (*SyncMainFunctionCallback) (OutputFunction_E func);

/// @fn SyncFrequencyCallback
/// @brief Callback frequency value during "Baseline Reset Test" or "Frequency Scanning"
///
/// @param frequency  to callback in Hz
///
/// @see ::SECGRegisterSyncFrequencyCB
typedef void (*SyncFrequencyCallback) (double frequency);

/// @fn SamplingCallback
/// @brief Called back with sampling data; the PD sampling data is [0, 1023]
///
/// @param[in] channel    ::PPGSampling
/// @param[in] data       PD sampling data
/// @param[in] number     the number of the sampling data with the value
typedef void (*SamplingCallback) (int channel, int data, int number);

///
/// Initialize connection
///
/// During initialization, it will try to connect a device asynchronously.
/// If a device is found, the cb function will be called. After then,
/// if the device get disconnected, the cb will be called again to notify the disconnection event.
/// @param cb  a callback function to notify connection event
///
WHALETEQ_API
bool
SECGInit (
    ConnectedCallback cb
);

///
/// Connect the device
///
/// @param[in] portNumber            Device COM port number; -1 means the port number is automatically selected
/// @param[in] millisecondsTimeout   Connection timeout; the number of milliseconds to connect, or -1 to wait indefinitely.
///
/// @return true if the device is connected,
///         or false if the time-out interval elapsed and the device is still disconnected
///
WHALETEQ_API
bool
SECGConnect (
    unsigned int portNumber,
    unsigned int millisecondsTimeout
);

///
/// Clean up library resource and connection
///
WHALETEQ_API
void
SECGFree (
    void
);


///
/// Check if SECG is connected
///
/// @return true if the device is connected
///
WHALETEQ_API
bool
SECGIsConnected (
    void
);

///
/// Check if a PPG model is connected
///
/// @return true if the device is connected
///
WHALETEQ_API
bool
SECGIsPPGConnected (
    void
);

///
/// Reset all parameters to default value, with only RA lead on
///
WHALETEQ_API
void
SECGReset (
    void
);

///
/// Reset all parameters to default value, and close all leads
///
WHALETEQ_API
void
SECGResetAllLeadOff (
    void
);


//
// Device Configurations
//


///
/// Get serial number of the connected device
///
/// @return serial number of the connected device, or nullptr if no device is connected
///
WHALETEQ_API
const char*
SECGGetSerialNumber (
    void
);

///
/// Get serial number of the connected PPG module
///
/// @return serial number of the connected PPG module, or empty string if no PPG device is connected
///
WHALETEQ_API
const char*
SECGGetPPGSerialNumber (
    void
);

///
/// Get firmware version of the connected device
///
/// @return firmware code text of the connected device, or nullptr if no device is connected
///
WHALETEQ_API
const char*
SECGGetFWVersion (
    void
);

///
/// Get hardware version code of the connected device
///
/// @return hardware code text of the connected device, or nullptr if no device is connected
///
WHALETEQ_API
const char*
SECGGetHWVersion (
    void
);

///
/// Get device information
///
/// @param[out] modelInfo  pointer to a ::MODEL_INFORMATION structure
///
/// @return true if success
///
WHALETEQ_API
bool
SECGGetDeviceInformation (
    MODEL_INFORMATION *modelInfo
);

///
/// Get PPG module information
/// @param[out] modelInfo   pointer to a ::MODEL_INFORMATION structure
///
/// @return true if success
///
WHALETEQ_API
bool
SECGGetPPGDeviceInformation (
    MODEL_INFORMATION *modelInfo
);


///
/// Get device FW/HW information
/// @param[out] hwInfo  pointer to a ::HW_INFORMATION structure
///
/// @return true if success
///
WHALETEQ_API
bool
SECGGetHWInformation (
    HW_INFORMATION *hwInfo
);

///
/// Get PPG module FW/HW information
/// @param[out] hwInfo  pointer to a ::HW_INFORMATION structure
///
/// @return true if success
///
WHALETEQ_API
bool
SECGGetPPGHWInformation (
    HW_INFORMATION *hwInfo
);


///
/// Check if the SECG is playing
///
/// @return true if output is on, or false otherwise
///
WHALETEQ_API
bool
SECGIsPlaying (
    void
);

#define DefaultDivider 1

///
/// Register a AC output callback
///
/// The callback function will be called with every AC sampling points when playing
/// @note the divider is synchronized with the one in DC callback, and if the value is invalid, it will be set to default.
///
/// @param cb the function to callback AC output
/// @param freqDivider the frequency divider for the callback. e.g., if the sample rate is 40000, and the divider is 100,
///                    and the callback sample rate will be 400Hz.
///
WHALETEQ_API
void
SECGRegisterOutputSignalCallback (
    OutputSignalCallback cb,
    int freqDivider = DefaultDivider
);

///
/// Register a pacing signal callback
///
/// The callback function will be called at the start of a pacing pulse
/// @param cb the function to callback pacing pulse
///
WHALETEQ_API
void
SECGRegisterPacingOutputSignalCallback (
    OutputSignalCallback cb
);

///
/// Register a callback function to receive frequency value during "Baseline Reset Test" or "Frequency Scanning"
/// @param cb a callback function in type ::SyncFrequencyCallback
///
/// @see SECGSetBaselineResetTest
/// @see SECGSetFrequencyScanSine
/// @see SECGSetFrequencyScanECG
///
WHALETEQ_API
void
SECGRegisterSyncFrequencyCB (
    SyncFrequencyCallback cb
);

///
/// Register a callback function to receive DC offset value during using ::Output_YY1079_Ramp
/// @param cb a callback function in type ::SyncDCOffsetCallback
///
/// @see ::Output_YY1079_Ramp
///
WHALETEQ_API
void
SECGRegisterSyncDCOffsetCB (
    SyncDCOffsetCallback cb
);

///
/// Register a callback function to get main function during frequency scanning
/// @param cb callback function in type ::SyncMainFunctionCallback
///
WHALETEQ_API
void
SECGRegisterSyncMainFunctionCB (
    SyncMainFunctionCallback cb
);

///
/// Enable to measure RLD
/// @param onOff true enable measure RLD
///
WHALETEQ_API
bool
SECGMeasureRLD (
    bool onOff
);

///
/// Get the measured value from RLD
/// @param[out] pN1 the voltage on N1 in **mV**
/// @param[out] pN2 the voltage on N1 in **mV**
///
/// @return true if success
///
WHALETEQ_API
bool
SECGReadRLD (
    double *pN1,
    double *pN2
);

///
/// Set IEC60601-2-27 Standard waveform type
/// @param spec waveform type of enum ::SpecialWave227_E
///
/// @return 0 if success, otherwise fail
/// @see ::Output_IEC227W
///
WHALETEQ_API
int
SECGSetSpecialWave227 (
    SpecialWave227_E spec
);

///
/// Get current IEC60601-2-27 Standard waveform type setting
///
/// @return enum ::SpecialWave227_E as current setting of IEC60601-2-27 Standard waveform
/// @see ::SECGSetSpecialWave227
///
WHALETEQ_API
SpecialWave227_E
SECGGetSpecialWave227 (
    void
);

///
/// Set IEC60601-2-25 Standard waveform type
/// @param spec waveform type of enum ::SpecialWave251_E
///
/// @return 0 if success, otherwise fail
/// @see ::Output_IEC251W
///
WHALETEQ_API
int
SECGSetSpecialWave251 (
    SpecialWave251_E spec
);

///
/// Get current IEC60601-2-25 Standard waveform type setting
///
/// @return enum ::SpecialWave251_E as current setting of IEC60601-2-25 Standard waveform
/// @see ::SECGSetSpecialWave251
///
WHALETEQ_API
SpecialWave251_E
SECGGetSpecialWave251 (
    void
);

///
/// Set IEC60601-2-47 HRV pattern type
/// @param spec waveform type of enum ::SpecialWave247_E
///
/// @return 0 if success, otherwise fail
/// @see ::Output_IEC247W
///
WHALETEQ_API
int
SECGSetSpecialWave247 (
    SpecialWave247_E spec
);

///
/// Get current IEC60601-2-47 HRV pattern type
///
/// @return enum ::SpecialWave247_E as current setting of IEC60601-2-47 HRV pattern type
/// @see ::SECGSetSpecialWave247
///
WHALETEQ_API
SpecialWave247_E
SECGGetSpecialWave247 (
    void
);

///
/// Set ANE20000 lead
/// @param lead value (0~2: LeadI/II/III; 3~8: Lead V1~V6)
///
/// @return 0 if success, or -1 if the parameter is invalid
///
WHALETEQ_API
int
SECGSetANE20000Lead (
    int lead
);

///
/// Get ANE20000 lead setting
///
/// @return current lead value setting
/// @see ::SECGSetANE20000Lead
///
WHALETEQ_API
int
SECGGetANE20000Lead (
    void
);

///
/// Set output function
/// @note if the parameter is not ::Output_Off, the device will start outputting
/// @param func output function type
///
/// @return 0 if success, or -1 if fail
///
WHALETEQ_API
int
SECGSetOutputFunction (
    OutputFunction_E func
);

///
/// Get current output function
///
/// @return a value of enum ::OutputFunction_E as the current output function
/// @see ::SECGSetOutputFunction
///
WHALETEQ_API
OutputFunction_E
SECGGetOutputFunction (
    void
);

///
/// Set AC output voltage amplitude
/// @param amplitude	amplitude of AC output in **mV**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
///	@return -2: value out of range
///	@return -3: "Baseline Reset Test" is working
///
/// @see ::DefaultAmplitude
/// @see ::MaxAmplitude
/// @see ::MinAmplitude
/// @see ::MaxAmplitudePulse
/// @see ::MinAmplitudePulse
/// @see ::MaxAmplitudeECG
/// @see ::MinAmplitudeECG
///
WHALETEQ_API
int
SECGSetAmplitude (
    double amplitude
);

///
/// Get current AC output voltage amplitude
///
/// @return amplitude of AC output in **mV**
/// @see ::SECGSetAmplitude
///
WHALETEQ_API
double
SECGGetAmplitude (
    void
);

#define DefaultAmplitude    1.0			 //!< mV
#define MaxAmplitude        40.0		 //!< mV
#define MinAmplitude        -40.0		 //!< mV
#define MaxAmplitudePulse   20.0		 //!< mV
#define MinAmplitudePulse   -20.0		 //!< mV
#define MaxAmplitudeECG     20.0		 //!< mV
#define MinAmplitudeECG     -20.0		 //!< mV

///
/// Set frequency of waveform
///
/// @param frequency	frequency of output function in **Hz**
/// @note If failed, try to ::SECGSetOutputFunction first
///
///	@return  0: success
///	@return -1: SECG isn't initialized
///	@return -2: value out of range
///	@return -3: "Frequency Scan" is working
///	@return -4: "Baseline Reset Test" is working
///
/// @see ::DefaultFrequency
/// @see ::MaxFrequency
/// @see ::MinFrequency
/// @see ::MaxFrequencyECG
/// @see ::MinFrequencyECG
/// @see ::MaxFrequencyPulseWave
///
WHALETEQ_API
int
SECGSetFrequency (
    double frequency
);

///
/// Get current frequency setting
///
/// @return frequency of AC output in **mV**
/// @see SECGSetFrequency
///
WHALETEQ_API
double
SECGGetFrequency (
    void
);

#define DefaultFrequency        1.0			//!< Hz
#define MaxFrequency            500.0		//!< Hz
#define MinFrequency			0.05		//!< Hz
#define MaxFrequencyECG			6.0			//!< Hz, for ::Output_ECG2_27 and ::Output_Custom_ECG
#define MinFrequencyECG			0.017		//!< Hz, for ::Output_ECG2_27 and ::Output_Custom_ECG
#define MaxFrequencyPulseWave	5.0			//!< Hz, for ::Output_RectanglePulse and ::Output_TrianglePulse

///
/// Set DC offset
/// @param dcOffset	DC offset on output function in **mV**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
///	@return -2: value out of range
///
/// @see ::DefaultDCOffset
/// @see ::MaxDCOffset
/// @see ::MinDCOffset
/// @see ::MaxDCOffsetVarMode
/// @see ::MinDCOffsetVarMode
///
WHALETEQ_API
int
SECGSetDCOffset (
    int dcOffset
);

///
/// Get current DC offset setting
///
/// @return current DC offset setting in **mV**
/// @see ::SECGSetDCOffset
///
WHALETEQ_API
int
SECGGetDCOffset (
    void
);

#define DefaultDCOffset			0			//!< mV
#define MaxDCOffset				300			//!< mV, fixed mode
#define MinDCOffset				-300		//!< mV, fixed mode
#define MaxDCOffsetVarMode		1000		//!< mV
#define MinDCOffsetVarMode		-1000		//!< mV

///
/// Set DC offset variable mode
/// @brief Default: true
///
/// @param onOff	true to set DC offset variable mode, otherwise fixed mode
/// @note The fixed mode is valid only when DC offset is ::MaxDCOffset or ::MinDCOffset
///
/// @return 0 if success, or -1 if SECG isn't initialized
///
/// @see ::MaxDCOffset
/// @see ::MinDCOffset
/// @see ::MaxDCOffsetVarMode
/// @see ::MinDCOffsetVarMode
///
WHALETEQ_API
int
SECGSetDCOffsetVariableMode (
    bool onOff
);

///
/// Get current DC offset variable mode setting
///
/// @return true if the setting is on variable mode, or false if on fixed mode
/// @see ::SECGSetDCOffsetVariableMode
///
WHALETEQ_API
bool
SECGGetDCOffsetVariableMode (
    void
);

///
/// Set DC offset common mode,
/// @brief default *false*
/// @note It works only if DC Offset variable mode is off
///
/// @param onOff true to set DC offset common mode
///
/// @return 0 if success, or -1 if SECG isn't initialized
/// @see SECGSetDCOffsetVariableMode
///
WHALETEQ_API
int
SECGSetDCOffsetCommonMode (
    bool onOff
);

///
/// Get current DC offset common mode setting
///
/// @return true if the setting is on common mode
/// @see ::SECGSetDCOffsetCommonMode
///
WHALETEQ_API
bool
SECGGetDCOffsetCommonMode (
    void
);

///
/// Change the state of leads
/// @brief Default: only ::Lead_RA on
///
/// @param lead     the lead to control
/// @param OnOff    true to open the lead, or false to close it
///
/// @return 0 if success, or -1 if SECG isn't initialized
///
WHALETEQ_API
int
SECGSetOutputLead (
    OutputLead_E lead,
    bool OnOff
);

///
/// Get state of the lead
/// @param lead the lead to check
///
/// @return  true if the lead is on
/// @see ::SECGSetOutputLead
///
WHALETEQ_API
bool
SECGGetOutputLead (
    OutputLead_E lead
);

///
/// Set the pulse width of pulse function
///
/// @param width the pulse width to set in **ms**
/// 
/// @return  0: success
/// @return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultPulseWidth
/// @see ::MaxPulseWidth
/// @see ::MinPulseWidth
///
WHALETEQ_API
int
SECGSetPulseWidth (
    double width
);

///
/// Get current pulse width setting
///
/// @return the current pulse width setting in **ms**
///
WHALETEQ_API
double
SECGGetPulseWidth (
    void
);

#define DefaultPulseWidth    100            //!< ms
#define MaxPulseWidth        300            //!< ms
#define MinPulseWidth        1              //!< ms

///
/// Set PR interval of customized ECG waveform
/// @param time PR interval in **ms**
///
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultPRInterval
/// @see ::MaxPRInterval
/// @see ::MinPRInterval
/// @see ::Output_Custom_ECG
///
WHALETEQ_API
int
SECGSetPRInterval (
    double time
);

///
/// Get current PR interval setting of customized ECG waveform
///
/// @return current PR interval setting in **ms**
/// @see ::SECGSetPRInterval
///
WHALETEQ_API
double
SECGGetPRInterval (
    void
);

#define DefaultPRInterval    160            //!< ms
#define MaxPRInterval        200            //!< ms
#define MinPRInterval        0              //!< ms

///
/// Set QT interval of customized ECG waveform
/// @param time QT interval in **ms**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultQTInterval
/// @see ::MaxQTInterval
/// @see ::MinQTInterval
/// @see ::Output_Custom_ECG
///
WHALETEQ_API
int
SECGSetQTInterval (
    double time
);

///
/// Get current QT interval setting of customized ECG waveform
///
/// @return current QT interval setting in **ms**
/// @see ::SECGSetQTInterval
///
WHALETEQ_API
double
SECGGetQTInterval (
    void
);

#define DefaultQTInterval    350			//!< ms
#define MaxQTInterval        900			//!< ms
#define MinQTInterval        100			//!< ms

///
/// Set P duration of customized ECG waveform
/// @param time P duration in **ms**
///
/// @return	 0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultPDuration
/// @see ::MaxPDuration
/// @see ::MinPDuration
/// @see ::Output_Custom_ECG
///
WHALETEQ_API
int
SECGSetPDuration (
    double time
);

///
/// Get current P duration setting of customized ECG waveform
///
/// @return current P duration setting in **ms**
/// @see ::SECGSetPDuration
///
WHALETEQ_API
double
SECGGetPDuration (
    void
);

#define DefaultPDuration    100         //!< ms
#define MaxPDuration        100         //!< ms
#define MinPDuration        50          //!< ms

///
/// Set P wave of customized ECG waveform
/// @param amplitude	amplitude of P wave in **mV**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultPWave
/// @see ::MaxPWave
/// @see ::MinPWave
/// @see ::Output_Custom_ECG
///
WHALETEQ_API
int
SECGSetPWave (
    double amplitude
);

///
/// Get current P wave setting of customized ECG waveform
///
/// @return current P wave setting in **mV**
/// @see ::SECGSetPWave
///
WHALETEQ_API
double
SECGGetPWave (
    void
);

#define DefaultPWave    0.2         //!< mV
#define MaxPWave        2.0         //!< mV
#define MinPWave        0           //!< mV

///
/// Set QRS duration of ECG waveform
/// @param time QRS duration in **ms**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultQRSDuration
/// @see ::MaxQRSDuration
/// @see ::MinQRSDuration
///
WHALETEQ_API
int
SECGSetQRSDuration (
    double time
);

///
/// Get current QRS duration setting of ECG waveform
///
/// @return current QRS duration setting in **ms**
/// @see ::SECGSetQRSDuration
///
WHALETEQ_API
double
SECGGetQRSDuration (
    void
);

#define DefaultQRSDuration  100         //!< ms
#define MaxQRSDuration      200         //!< ms
#define MinQRSDuration      5           //!< ms

///
/// Set ST deviation of customized ECG waveform
/// @param amplitude	amplitude of ST deviation in **mV**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultSTDeviation
/// @see ::MaxSTDeviation
/// @see ::MinSTDeviation
/// @see ::Output_Custom_ECG
///
WHALETEQ_API
int
SECGSetSTDeviation (
    double amplitude
);

///
/// Get current ST deviation setting of customized ECG waveform
///
/// @return current ST deviation setting in **mV**
/// @see ::SECGSetSTDeviation
///
WHALETEQ_API
double
SECGGetSTDeviation (
    void
);

#define DefaultSTDeviation    0             //!< mV
#define MaxSTDeviation        2.00          //!< mV
#define MinSTDeviation        -2.00         //!< mV

///
/// Set T wave of ECG waveform
/// @param amplitude	amplitude of T wave in **mV**
///
/// @return 0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultTWave
/// @see ::MaxTWave
/// @see ::MinTWave
///
WHALETEQ_API
int
SECGSetTWave (
    double amplitude
);

///
/// Get current T wave setting of ECG waveform
///
/// @return current T wave setting in **mV**
/// @see ::SECGSetTWave
///
WHALETEQ_API
double
SECGGetTWave (
    void
);

#define DefaultTWave        0.2         //!< mV
#define MaxTWave            5.0         //!< mV
#define MinTWave            0           //!< mV

#define DefaultTDuration    180			//!< ms

///
/// Short the 620kΩ/4.7nF impedance
/// @param onOff true to short the impedance, or false to shunt with it
///
/// @return 0 if success, or -1 if SECG isn't initialized
///
WHALETEQ_API
int
SECGSetInputImpedanceMode (
    bool onOff
);

///
/// Get the state of the 620kΩ/4.7nF impedance
///
/// @return true if the impedance is shorted, otherwise open
/// @see ::SECGSetInputImpedanceMode
///
WHALETEQ_API
bool
SECGGetInputImpedanceMode (
    void
);

///
/// Set the mode of pacing pulse.
/// @brief Default: ::SinglePulse
///
/// @param mode pulse mode in type ::PacingPulse_E
///
/// @return 0 if success, or -1 if SECG isn't initialized
///
WHALETEQ_API
int
SECGSetPacingPulseMode (
    PacingPulse_E mode
);

///
/// Get current pulse mode
///
/// @return current pulse mode setting
/// @see ::SECGSetPacingPulseMode
///
WHALETEQ_API
PacingPulse_E
SECGGetPacingPulseMode (
    void
);

///
/// Set amplitude of pacing pulse
/// @param amplitude amplitude of pacing pulse in **mV**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
WHALETEQ_API
int
SECGSetPacingAmplitude (
    double amplitude
);

///
/// Get current amplitude of pacing pulse
/// @return current amplitude setting of pacing pulse
/// @see ::SECGSetPacingAmplitude
///
WHALETEQ_API
double
SECGGetPacingAmplitude (
    void
);

#define DefaultPacingAmplitude    0			//!< mV
#define MaxPacingAmplitude        700		//!< mV
#define MinPacingAmplitude       -700		//!< mV

///
/// Set duration of pacing pulse
/// @param time pulse duration in **ms**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultPacingDuration
/// @see ::MaxPacingDuration
/// @see ::MinPacingDuration
///
WHALETEQ_API
int
SECGSetPacingDuration (
    double time
);

///
/// Get current duration setting of pacing pulse
///
/// @return current duration of pacing pulse in **ms**
/// @see ::SECGSetPacingDuration
///
WHALETEQ_API
double
SECGGetPacingDuration (
    void
);

#define DefaultPacingDuration    2.0			//!< ms
#define MaxPacingDuration        3.0			//!< ms
#define MinPacingDuration        0.03			//!< ms

///
/// Set pacing rate
/// @note If success, the synchronized state of pacing will be off
///
/// @param bpm pacing rate
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::DefaultPacingRate
/// @see ::MaxPacingRate
/// @see ::MinPacingRate
/// @see ::SECGSetPacingRateSynchronized
///
WHALETEQ_API
int
SECGSetPacingRate (
    unsigned int bpm
);

///
/// Get current pacing rate setting
///
/// @return current pacing rate in **BPM**
///
WHALETEQ_API
unsigned int
SECGGetPacingRate (
    void
);

#define DefaultPacingRate    60				//!< BPM
#define MaxPacingRate        360			//!< BPM
#define MinPacingRate        10				//!< BPM

///
/// Make pacing rate synchronized with the frequency of main function <br>
/// @brief Default: *true*
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see SECGSetPacingRate
/// @see SECGSetFrequency
///
WHALETEQ_API
int
SECGSetPacingRateSynchronized (
    void
);

///
/// Set time constant of pacing overshooting
/// @param time time constant in **ms**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::SECGSetOvershootAmplitude
///
WHALETEQ_API
int
SECGSetOvershootTimeConstant (
    unsigned int time
);

///
/// Get time constant of pacing overshooting
///
/// @return time constant in **ms**
/// @see ::SECGSetOvershootTimeConstant
///
WHALETEQ_API
unsigned int
SECGGetOvershootTimeConstant (
    void
);

#define DefaultOvershootTimeConstant    0           //!< ms
#define MaxOvershootTimeConstant        100         //!< ms
#define MinOvershootTimeConstant        0           //!< ms

///
/// Set amplitude of pacing overshooting
/// @param amplitude amplitude of pacing overshooting in **mV**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
/// @return -2: value out of range
///
/// @see ::SECGSetOvershootTimeConstant
///
WHALETEQ_API
int
SECGSetOvershootAmplitude (
    double amplitude
);

///
/// Get amplitude of pacing overshooting
///
/// @return amplitude of pacing overshooting in **mV**
/// @see ::SECGSetOvershootAmplitude
///
WHALETEQ_API
double
SECGGetOvershootAmplitude (
    void
);

#define DefaultOvershootAmplitude        0          //!< mV
#define MaxOvershootAmplitude            5.00       //!< mV
#define MinOvershootAmplitude            0          //!< mV

///
/// Set baseline reset test mode and start
///
/// @details If the mode is set to any valid value except ::Baseline_Off, SECG will start to output sine wave,
/// which the amplitude is 500mV and the frequency is 50/60/80/100 Hz
/// @note Set the mode to ::Baseline_Off will not stop outputting sine wave
///
/// @param mode mode in ::BaselineReset_E to use
///
/// @return 0 if success, or -1 if SECG isn't initialized
///
/// @see SECGRegisterSyncFrequencyCB
///
WHALETEQ_API
int
SECGSetBaselineResetTest (
    BaselineReset_E mode
);

///
/// Get current mode of baseline reset test
///
/// @return current mode of baseline reset test
///
WHALETEQ_API
BaselineReset_E
SECGGetBaselineResetTest (
    void
);

///
/// Set noise of ECG waveform
///
/// @param frequency	noise type in ::ECG2_27_NoiseFreq_E
/// @param amplitude	noise amplitude in **mV**
///
///	@return  0: success
/// @return -1: SECG isn't initialized
/// @return -2: amplitude out of range
///
/// @see ::DefaultECG2_27_NoiseAmp
/// @see ::MaxECG2_27_NoiseAmp
/// @see ::MinECG2_27_NoiseAmp
///
WHALETEQ_API
int
SECGSetECG2_27_Noise (
    ECG2_27_NoiseFreq_E frequency,
    double amplitude
);

///
/// Get current noise type of ECG waveform
///
/// @return current noise type in ::ECG2_27_NoiseFreq_E
///
WHALETEQ_API
ECG2_27_NoiseFreq_E
SECGGetECG2_27_NoiseFreq (
    void
);

///
/// Get current noise amplitude of ECG waveform
///
/// @return current noise amplitude in **mV**
///
WHALETEQ_API
double
SECGGetECG2_27_NoiseAmp (
    void
);

#define DefaultECG2_27_NoiseAmp    0.1			//!< mV
#define MaxECG2_27_NoiseAmp        5.0   		//!< mV
#define MinECG2_27_NoiseAmp        0.01			//!< mV

///
/// Enable ECG AAMI drift test
/// @param enable	true to enable, or false to disable it
///
/// @return 0 if success, or -1 if SECG isn't initialized
///
WHALETEQ_API
int
SECGSetECG2_27_AAMIDriftTest (
    bool enable
);

///
/// Get current setting of ECG AAMI drift test
///
/// @return true if enabled
///
WHALETEQ_API
bool
SECGGetECG2_27_AAMIDriftTest (
    void
);

///
/// Set amplitude of ECG AAMI drift test
/// @param amplitude amplitude of the triangle wave in **mV**
///
///	@return  0: success
///	@return -1: SECG isn't initialized
///	@return -2: amplitude out of range
///
/// @see ::DefaultAAMIDriftTestAmp
/// @see ::MaxAAMIDriftTestAmp
/// @see ::MinAAMIDriftTestAmp
///
WHALETEQ_API
int
SECGSetECG2_27_AAMIDriftTestAmplitude (
    double amplitude
);

///
/// Get amplitude of ECG AAMI drift test
///
/// @return amplitude of triangle wave in **mV**
/// @see SECGSetECG2_27_AAMIDriftTestAmplitude
///
WHALETEQ_API
double
SECGGetECG2_27_AAMIDriftTestAmplitude (
    void
);

#define DefaultAAMIDriftTestAmp    4.0			//!< mV
#define MaxAAMIDriftTestAmp        8.0			//!< mV
#define MinAAMIDriftTestAmp        1.0			//!< mV

///
/// Set frequency of ECG AAMI drift test
///
/// @param frequency	frequency of the triangle wave in **Hz**
///
/// @return  0: success
///	@return -1: SECG isn't initialized
///	@return -2: frequency out of range
///
/// @see ::DefaultAAMIDriftTestFreq
/// @see ::MaxAAMIDriftTestFreq
/// @see ::MinAAMIDriftTestFreq
///
WHALETEQ_API
int
SECGSetECG2_27_AAMIDriftTestFrequency (
    double frequency
);

///
/// Get frequency of ECG AAMI drift test
/// @return frequency of triangle wave in **Hz**
/// @see SECGSetECG2_27_AAMIDriftTestFrequency
///
WHALETEQ_API
double
SECGGetECG2_27_AAMIDriftTestFrequency (
    void
);

#define DefaultAAMIDriftTestFreq    0.1			//!< Hz
#define MaxAAMIDriftTestFreq        2.0			//!< Hz
#define MinAAMIDriftTestFreq        0.05		//!< Hz

///
/// Set dynamic range test
///
/// @param OnOff		true to start test; otherwise, stop test
/// @param useTriangle	true to use Triangle Wave as main function;
/// 					otherwise, use Square Wave instead
/// @param amplitude	amplitude of the waveform in mV
/// @param frequency	frequency of the waveform in Hz
///
/// @return  0: success
///	@return -1: SECG isn't initialized
///	@return -2: amplitude out of range
///	@return -3: frequency out of range
///
/// @see ::DefaultDynamicRangeTestAmp
/// @see ::MaxDynamicRangeTestAmp
/// @see ::MinDynamicRangeTestAmp
/// @see ::DefaultDynamicRangeTestFreq
/// @see ::MaxDynamicRangeTestFreq
/// @see ::MinDynamicRangeTestFreq
///
WHALETEQ_API
int
SECGSetDynamicRangeTest (
    bool OnOff,
    bool useTriangle,
    double amplitude,
    double frequency
);

///
/// Check if dynamic range test is enabled
///
/// @return true if dynamic range test is enabled
///
WHALETEQ_API
bool
SECGGetDynamicRangeTest (
    void
);

///
/// Get amplitude of the sine wave in dynamic range test
///
/// @return amplitude of the sine wave in **mV**
///
WHALETEQ_API
double
SECGGetDynamicRangeTestAmplitude (
    void
);

///
/// Get frequency of the sine wave in dynamic range test
///
/// @return frequency of the sine wave in **Hz**
///
WHALETEQ_API
double
SECGGetDynamicRangeTestFrequency (
    void
);

#define DefaultDynamicRangeTestAmp    1.0			//!< mV
#define MaxDynamicRangeTestAmp       10.0			//!< mV
#define MinDynamicRangeTestAmp        	0			//!< mV
#define DefaultDynamicRangeTestFreq    40			//!< Hz
#define MaxDynamicRangeTestFreq        60			//!< Hz
#define MinDynamicRangeTestFreq         1			//!< Hz

///
/// Start or stop sine wave frequency scan
///
/// @param onOff        true to start, false to stop
/// @param startFreq    the first value of frequency in **Hz**
/// @param stopFreq     the last value of frequency in **Hz**
/// @param duration     total duration of frequency scan
///
///	@return  0: success
///	@return -1: SECG isn't initialized
///	@return -2: start frequency out of range
///	@return -3: stop frequency out of range
/// @return -4: duration out of range
///
/// @see ::DefaultScanSineStartFreq
/// @see ::DefaultScanSineStopFreq
/// @see ::MaxScanSineFreq
/// @see ::MinScanSineFreq
/// @see ::DefaultScanSineDuration
/// @see ::MaxScanSineDuration
/// @see ::MinScanSineDuration
/// @see SECGRegisterSyncFrequencyCB
///
WHALETEQ_API
int
SECGSetFrequencyScanSine (
    bool onOff,
    double startFreq,
    double stopFreq,
    int duration
);

///
/// Check if sine frequency scan is running
///
/// @return true if sine frequency scan is running
///
WHALETEQ_API
bool
SECGGetFrequencyScanSine (
    void
);

///
/// Get current start frequency of sine frequency scan
///
/// @return current start frequency in **Hz**
///
WHALETEQ_API
double
SECGGetFrequencyScanSineStartFrequency (
    void
);

///
/// Get current stop frequency of sine frequency scan
///
/// @return current stop frequency in **Hz**
///
WHALETEQ_API
double
SECGGetFrequencyScanSineStopFrequency (
    void
);

///
/// Get current stop duration of sine frequency scan
///
/// @return current duration in *second*
///
WHALETEQ_API
int
SECGGetFrequencyScanSineDuration (
    void
);

#define DefaultScanSineStartFreq    0.67            //!< Hz
#define DefaultScanSineStopFreq     150             //!< Hz
#define MaxScanSineFreq             500.0           //!< Hz
#define MinScanSineFreq             0.67            //!< Hz
#define DefaultScanSineDuration     30              //!< second
#define MaxScanSineDuration         180             //!< second
#define MinScanSineDuration         10              //!< second

///
/// Start or stop ECG frequency scan
/// @details from 3 to 30 BPM, in 30 seconds
///
/// @param OnOff true to start ECG frequency scan, or false to stop
///
///	@return  0: success
///	@return -1: SECG isn't initialized
///	@return -2: start frequency out of range
///	@return -3: stop frequency out of range
/// @return -4: duration out of range
///
WHALETEQ_API
int
SECGSetFrequencyScanECG (
    bool OnOff
);

///
/// Check if ECG frequency scan is running
///
/// @return true if ECG frequency scan is running
///
WHALETEQ_API
bool
SECGGetFrequencyScanECG (
    void
);

///
/// Load a ECG raw data file in Whaleteq format to play
///
/// @param filePath path of the file to load in UTF-8 encoding
/// @param channel		the index of the channel to load, start from 0
///
///	@return >0: Success, the number of sample data loaded
/// @return -1: Open file failed
/// @return -2: Invalid sample rate in Line 1
/// @return -3: Invalid sample number in Line 2
/// @return -4: Invalid channel number in Line 3
/// @return -5: Invalid description in Line 4
/// @return -6: Raw data file is too large to fit the memory
/// @return -7: No such channel
///
/// @see ::Output_ECG_File
///
WHALETEQ_API
int
SECGLoadECGtxt (
    const char* filePath,
    int channel = 0
);


///
/// Load a ECG raw data file in EDF format to play
///
/// @param filePath     path of the file to load in UTF-8 encoding
/// @param channel      the index of the channel to load, start from 0
///
///	@return >0: Success, the length of sample data
/// @return -1: Open file failed
/// @return -2: Invalid format
/// @return -3: No such channel
/// @return -4: Too large to load
/// @return -5: Invalid sample size
///
/// @see ::Output_ECG_File
///
WHALETEQ_API
int
SECGLoadECGedf (
    const char* filePath,
    int channel = 0
);


///
/// Load ECG raw data files in WFDB format to play
///
/// @param headerFile   path of the header file(.hea) to load in UTF-8 encoding
/// @param signalFile   path of the data file(.dat) to load in UTF-8 encoding
/// @param channel      the index of the channel to load, start from 0
///
///	@return >0: Success, the number of sample data loaded
/// @return -1: Open the header file failed
/// @return -2: Open the signal file failed
/// @return -3: No such channel
/// @return -4: Load raw data failed
/// @return -5: Invalid sample rate
///
/// @see ::Output_ECG_File
///
WHALETEQ_API
int
SECGLoadECGdat (
    const char* headerFile,
    const char* signalFile,
    int channel = 0
);


///
/// Set lead-off sate
/// @param type value of enum ::LeadOff_Type_E
///
/// @return true if success
///
/// @see ::LeadOff_Type_E
///
WHALETEQ_API
bool
SECGSetLeadOff (
    int type
);

#define MaxRespirationVariation 10000    //!< 1 milli-ohm
#define MinRespirationVariation  50    //!< 1 milli-ohm
#define MaxRespirationBrPM      200     //!< BrPM
#define MinRespirationBrPM        0     //!< BrPM
#define MaxRespirationRatio       5
#define MinRespirationRatio       1
#define MaxRespirationApnea      60     //!< second
#define MinRespirationApnea       0     //!< second

///
/// Enable respiration impedance mode
///
/// @param onOff true to enable respiration, or false to disable it
///
WHALETEQ_API
bool
SECGEnableRespiration (
    bool onOff
);

///
/// Set respiration parameters (Impedance mode)
/// @note Don't forget to call ::SECGEnableRespiration to enable respiration first
///
/// @param variation    the max variation impedance; Unit: milli-ohm; range of internal module: 1000~5000, external module: 50~10000
/// @param freq			the rate of respiration in BrPM
/// @param ratio		the ratio of inhale:exhale(1 : ratio), range: 1 ~ 5
/// @param baseline     the baseline impedance setting; Unit: ohm
/// @param apnea        apnea time in one minute , in second
///
/// @return             true if success
///
/// @see ::SECGEnableRespiration
/// @see ::SECGSetRespirationAlgorithm
///
WHALETEQ_API
bool
SECGSetRespiration (
    int variation,
    int freq,
    int ratio,
    int baseline,
    int apnea
);

///
/// Set respiration parameters (Modulation mode)
///
/// @param freq     the rate of respiration in **BrPM**
/// @param ratio    the ratio between inhale and exhale
/// @param apnea    the apnea time in one minute
/// @param baseline ECG baseline modulation ratio in %
/// @param ampMod   ECG amplitude modulation ratio in %
/// @param freqMod  ECG frequency modulation ratio in %
///
/// @return true if success, or false if any parameters is out of range
///
/// @see MaxRespirationBrPM
/// @see MaxRespirationBrPM
/// @see MaxRespirationRatio
/// @see MinRespirationRatio
/// @see MaxRespirationApnea
/// @see MinRespirationApnea
///
WHALETEQ_API
bool
SECGSetRespirationAlgorithm (
    int freq,
    int ratio,
    int apnea,
    int baseline,
    int ampMod,
    int freqMod
);

///
/// Disable respiration modulation
///
/// @see ::SECGSetRespireAlgorithmParam
///
WHALETEQ_API
void
SECGDisableRespireAlgorithm (
    void
);

#define DEFAULT_NST_NOISE_GAIN  1.0
#define MIN_NST_NOISE_GAIN      0.1
#define MAX_NST_NOISE_GAIN      10.0

///
/// Set NST Noise type
///
///	@return  0: Success
/// @return -1: Running, please stop it first
/// @return -2: The gain exceed the limit
///
/// @see NST_NOISE_E
/// @see DEFAULT_NST_NOISE_GAIN
/// @see MIN_NST_NOISE_GAIN
/// @see MAX_NST_NOISE_GAIN
///
WHALETEQ_API
int
SECGSetNSTNoise (
    NST_NOISE_E type,
    double gain
);

///
/// Set special waveform to loop
///
/// @param loop true to loop special waveform
///
/// @see ::Output_IEC227W
/// @see ::Output_IEC251W
/// @see ::Output_IEC247W
///
WHALETEQ_API
void
SECGSetSpecialWaveformLoop (
    bool loop
);

///
/// Set loaded raw file to loop
///
/// @param loop true to loop ::Output_ECG_File
///
/// @see ::Output_ECG_File
WHALETEQ_API
void
SECGSetFileLoop (
    bool loop
);

#define DefaultSampleRate   20000
#define MaxSampleRate       40000
#define MinSampleRate       100

///
/// Set the sample rate
///
/// @param rate sample rate in **Hz**
///
///	@return  0: succeed
///	@return -1: SECG is not initialized
///	@return -2: value out of range
///	@return -3: SECG is playing
///
/// @see DefaultSampleRate
/// @see MaxSampleRate
/// @see MinSampleRate
///
WHALETEQ_API
int
SECGSetSampleRate (
    int rate
);

///
/// Get the current sample rate
///
/// @return the current sample rate in **Hz**
///
WHALETEQ_API
int
SECGGetSampleRate (
    void
);

///
/// Get the version of SDK
///
/// @return the version name of SDK
///
WHALETEQ_API
const char*
SECGGetSDKVersion (
    void
);


//==============================================
// PPG Module (Require Firmware version 1.3+)
//=============================================

typedef enum {
    LEDTypeGreen = 0,             //!< Green light
    LEDTypeRed,                   //!< Red light
    LEDTypeIR,                    //!< Infrared light
    LEDTypeNone                   //!< No LED
} LEDType;

typedef enum {
    PPGWaveformTypeSine = 0,      //!< Sine wave
    PPGWaveformTypeTriangle,      //!< Triangle wave
    PPGWaveformTypeSquare,        //!< Square wave
    PPGWaveformTypePPG            //!< PPG waveform
} PPGWaveformType;

typedef enum {
    SyncPulseLEDOff = 0,          //!< LED off
    SyncPulseSync,                //!< LED static bright
    SyncPulseSyncOff              //!< LED sync with PD
} SyncPulse;

typedef enum {
    PPGInvertedOff = 0,           //!< Normal output
    PPGInvertedOn                 //!< Upside down output
} PPGInverted;

typedef enum {
    PPGAmbientLightOff = 0,
    PPGAmbientLight50Hz,
    PPGAmbientLight60Hz,
    PPGAmbientLight1KHz,
    PPGAmbientLight2KHz,
    PPGAmbientLight3KHz,
    PPGAmbientLight4KHz,
    PPGAmbientLight5KHz,
    PPGAmbientLight6KHz,
    PPGAmbientLight7KHz,
    PPGAmbientLight8KHz,
    PPGAmbientLight9KHz,
    PPGAmbientLight10KHz,
    PPGAmbientLightDirectCurrent,
    PPGAmbientLightSunLight
} PPGAmbientLightMode;

typedef enum {
    Channel1PD = 0,
    Channel2PD,
    Channel1Switch,
    Channel2Switch
} PPGSampling;

#define MaxFrequencyPPG     5.0		//!< Hz
#define MinFrequencyPPG		0.16	//!< Hz

#define DefaultPPGDC        625     //!< mV
#define MaxPPGDC            3000    //!< mV
#define MinPPGDC            30      //!< mV

#define DefaultPPGAC        12.50   //!< mV
#define MaxPPGAC            30.00   //!< mV
#define MinPPGAC            0.75    //!< mV

#define DefaultPPGSampleRate   10000 //!< Hz

///
/// Switch the PPG channel output
///
/// @param type  the LED type of channel to config
/// @param onOff true to enabled the PPG channel, or false to disable it
///
/// @return  0: Success
/// @return -1: SECG is playing
/// @return -2: Invalid LED type
///
WHALETEQ_API
int
SECGEnablePPGOutput (
    LEDType type,
    bool onOff
);

///
/// Switch the ECG channel output
/// @brief Default: *On*
/// @param onOff  true to enabled the ECG channel, or false to disable it
///
/// @return 0 if success
///
WHALETEQ_API
int
SECGEnableECGOutput (
    bool onOff
);

///
/// Set PPG standard waveform on the specified LED channel
/// @details It will output a default PPG waveform with the static AC (amplitude) and DC
/// @note The crest time (period of Systolic Peak) is 15% of the total waveform period
///
/// @param type         the LED channel to output
/// @param waveformType the waveform type to use
/// @param syncPulse    LED sync mode
/// @param inverted     upside down output or not
/// @param frequency    waveform frequency in **Hz**
/// @param dc           fixed DC value of output in **mV**
/// @param ac           waveform amplitude in **mV**
///
/// @return >0: Success, the length of loaded data
/// @return -1: SECG is playing
/// @return -2: Invalid LED type
/// @return -3: Invalid waveform type
/// @return -4: Invalid frequency
/// @return -5: Invalid dc value
/// @return -6: Invalid ac value
///
/// @see ::MODEL_INFORMATION
///
WHALETEQ_API
int
SECGSetPPGStandardWaveform (
    LEDType type,
    PPGWaveformType waveformType,
    SyncPulse syncPulse,
    PPGInverted inverted,
    double frequency,
    double dc,
    double ac
);

///
/// Set PPG output with customized raw data on the specified LED channel
///
/// @param type         the LED channel to output
/// @param syncPulse    LED sync mode
/// @param inverted     Upside down output or not
/// @param size         the size of pAC and pDC
/// @param [in] pDc     raw data array of DC in **mV**
/// @param [in] pAc     raw data array of AC in **mV**
/// @param sampleRate   sample rate of the input raw data in Hz
///
/// @return  0: Success
/// @return -1: SECG is playing
/// @return -2: Invalid LED type
/// @return -3: Invalid size
/// @return -4: Invalid input pDC
/// @return -5: Invalid input pAC
/// @return -6: Invalid sampleRate
///
/// @see SECGClearPPGWaveform
///
WHALETEQ_API
int
SECGSetPPGRawData (
    LEDType type,
    SyncPulse syncPulse,
    PPGInverted inverted,
    int size,
    const double* pDc,
    const double* pAc,
    double sampleRate
);


///
/// Clear the data on the specified LED channel loaded by ::SECGSetPPGRawData
///
/// @param type the LED channel to clear
///
WHALETEQ_API
void
SECGClearPPGWaveform (
    LEDType type
);


///
/// Register a PPG output callback
///
/// @param type the LED channel to register the callback on
/// @param cb a callback function in type ::OutputSignalCallback
///
WHALETEQ_API
void
SECGRegisterOutputPPGCallback (
    LEDType type,
    OutputSignalCallback cb
);

///
/// Set PPG pulse transit times to peak (PTTp)
/// @note It only works on standard PPG waveform and the frequency of ECG and PPG is the same.
///
/// @param pttp  the PTTp value in **ms**; set negative value to disable it
///
///
WHALETEQ_API
void
SECGSetPTTp(
    int pttp
);

///
/// Set PPG modulation parameters
/// @note please use ::SECGSetRespirationAlgorithm to set the respiration parameters
///
/// @param baseline PPG baseline modulation ratio in %
/// @param ampMod   PPG amplitude modulation ratio in %
/// @param freqMod  PPG frequency modulation ratio in %
///
/// @return true if success, or false if any parameters is out of range
///
/// @see SECGSetRespirationAlgorithm
/// @see SECGDisableRespireAlgorithm
///
WHALETEQ_API
bool
SECGSetPPGRespirationAlgorithm (
    int baseline,
    int ampMod,
    int freqMod
);

///
/// Set LED ambient light mode
/// @note It only works on PPG module WAP2012 (transmittance module)
/// @param mode  the ambient light mode, a value in ::PPGAmbientLightMode
///
/// @return  0: Success
/// @return -1: No connected PPG module
/// @return -2: Invalid mode value
/// @return -3: I/O error
///
/// @see ::PPGAmbientLightMode
///
WHALETEQ_API
int
SECGSetLEDAmbientLightMode (
    int mode
);

///
/// Get current LED ambient light mode setting
///
/// @return >= 0: the current mode value in ::PPGAmbientLightMode
/// @return   -1: No connected PPG module
/// @return   -2: I/O error
/// @return   -3: Fail to get the setting
///
/// @see ::PPGAmbientLightMode
///
WHALETEQ_API
int
SECGGetLEDAmbientLightMode (
    void
);

///
/// Enable a PPG sampling channel
/// @note if the callback is a null pointer, the sampling channel will be disabled
///
/// @param channel     the channel value in ::PPGSampling
/// @param callback    a callback function to pass the sampling data
///
///	@return  0: Success
///	@return -1: SECG isn't initialized
/// @return -2: No connected PPG module
/// @return -3: SECG is playing
///
WHALETEQ_API
int
SECGEnablePPGSampling (
    PPGSampling channel,
    SamplingCallback callback
);

///
/// Disable all PPG sampling channels
///
///	@return 0 if success, or -1 if fail
///
WHALETEQ_API
int
SECGDisablePPGSampling (
    void
);

///
/// Start PPG Sampling
///
///	@return  0: Success
///	@return -1: SECG isn't initialized
///	@return -2: No connected PPG module
/// @return -3: SECG is playing
/// @return -4: PPG sampling is disabled
/// @return -4: Fail to start sampling (I/O error)
///
WHALETEQ_API
int
SECGStartPPGSampling (
    void
);

///
/// Stop PPG sampling and reset all sampling mode
///
WHALETEQ_API
void
SECGStopPPGSampling (
    void
);

//
// External Respiratory
//
WHALETEQ_API
bool
SECGExternalRespiratoryIsAvailable (
    void
);
