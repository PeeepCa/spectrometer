import sys
import clr


class BlockingFunctions:
    """
    Py_LcSpvis library for Spvis Spectrometer based on Lumichrome .net library.
    All descriptions are used as docstrings.
    Bellow is .net library description.

    Provides an interface from the PC to the dynamic library, which is developed based on
    the .NET platform. This interface allows the application to configure the spectrometer and receive
    and send data from the spectrometer.
    A dynamic library uses a pair of open and close functions (LC_Init() and LC_Done()) that must
    be called using the program. As long as the open function is not called, all other functions will
    return an error code. The open function (LC_Init()) attempts to open a communication interface
    for all linked devices. The close function (LC_Done()) closes the communication interface and
    releases all internal data.
    The interface between the application program and the dynamic library can be divided into
    four functional groups:
    ⚫ Internal data read functions
    -These functions are used to read device configuration data from the internal storage of the
    device.
    ⚫ Blocking control functions
    -These functions control the blocking behavior of sending requests to the device and
    waiting for a response. They can either block until a reply is received or send a timeout
    notification before returning control to the application program.
    ⚫ Non-blocking data read functions
    - These functions send requests to the device and then return control to the application
    program. After receiving a reply from the device or experiencing a timeout, they send a
    notification to the application program.
    ⚫ Data send functions
    - These functions are used to send device configuration data to the device. After the
    application program is initialized, it should select the spectrometer to be used.
    """
    def __init__(self, path):
        sys.path.append(path)
        clr.AddReference("LcSpvis_XS")

        from LcSpvis import LC_SpFunc_XS

        global LC
        LC = LC_SpFunc_XS()

    @staticmethod
    def lc_init():
        """
        The communication interface for initializing the spectrometer and internal
        data structures.
        Once the LC_Init() function is called, the software internally instantiates
        the required number of spectrometers. There is no need to instantiate
        them multiple times.
        :return: Success: the return value will be the number of connected or discovered
        devices. If no devices are connected, the return value will be 0.
        Failure: When encountering a failure, the return value will be
        ERR_UNKNOWN=-99.
        """
        return LC.LC_Init()

    @staticmethod
    def lc_done(i_index):
        """
        To close the communication with a specific spectrometer, identified by its
        operation index, and release the internal storage.
        :param i_index: An integer representing the selected spectrometer index.
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT= -19
        ERR_UNKNOWN = -99
        """
        return LC.LC_Done(i_index)

    @staticmethod
    def lc_doneall():
        """
        This function will close the communication interface with all
        spectrometers and release the internal storage.
        :return: Success:：ERR_SUCCESS = 0
        Failure：ERR_UNKNOWN = -99
        """
        return LC.LC_DoneAll()

    @staticmethod
    def lc_activate(i_index, i_file):
        """
        Activate the selected spectrometer for communication purposes.
        :param i_index: An integer representing the selected spectrometer index.
        :param i_file: licenseFilePath: A string representing the full path of the license file
        (.spt file) for the selected spectrometer.
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT= -19
        ERR_FILE_NO_EXIST = -24
        ERR_INVALID_DEVICE_TYPE = -7
        ERR_INVALID_DEVICE_ID = -4
        ERR_UNKNOWN = -99
        """
        return LC.LC_Activate(i_index, i_file)

    @staticmethod
    def lc_getlist(i_index, i_serialnumber):
        """
        This function will return the device information associated with the
        spectrometer connected to the specified port.
        :param i_index: An integer representing the selected spectrometer index.
        :param i_serialnumber: A string representing the serial number of the selected
        spectrometer.
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT= -19
        ERR_UNKNOWN = -99
        """
        return LC.LC_GetList(i_index, i_serialnumber)

    @staticmethod
    def lc_getparameters(i_index, i_mpiparametersno, i_parameter):
        """
        This function will return a data structure specific to the spectrometer.
        :param i_index: An integer representing the selected spectrometer index.
        :param i_mpiparametersno: An integer representing the mode selection for
        retrieving spectrometer device parameters.
        0: Get the spectrometer model.
        1: Get the total number of pixels of the spectrometer.
        2: Get the starting wavelength of the spectrometer.
        3: Get the ending wavelength of the spectrometer.
        :param i_parameter: A string representing the parameter value for the selected
        mode.
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_INVALID_PARAMETER = -1
        ERR_UNKNOWN = -99
        """
        return LC.LC_GetParameters(i_index, i_mpiparametersno, i_parameter)

    @staticmethod
    def lc_autodark(i_index, i_integration):
        """
        To retrieve the auto dark spectrum data for the selected spectrometer.
        :param i_index:  An integer representing the selected spectrometer index.
        :param i_integration:  A double precision floating-point number representing the
        upper limit of integration time for the dark spectrum.
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_INVALID_INT_TIME = -11
        ERR_UNKNOWN = -99
        """
        return LC.LC_AutoDark(i_index, i_integration)

    @staticmethod
    def lc_oncedark(i_index, i_integration, i_averaging):
        """
        This function will perform a single measurement to capture the dark
        spectrum data from the spectrometer. The dark spectrum represents the
        background noise or dark signal of the spectrometer without any light
        source.
        :param i_index:  An integer representing the selected spectrometer index.
        :param i_integration:  A double precision floating-point number representing the
        upper limit of integration time for the dark spectrum.
        :param i_averaging:  An integer representing the number of times the dark
        spectrum data is averaged.
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_UNKNOWN = -99
        """
        return LC.LC_OneDark(i_index, i_integration, i_averaging)

    @staticmethod
    def lc_autointegration(i_index, i_saturation, i_integration, i_averaging):
        """
        To obtain the automatic integration time and automatic averaging count
        of a spectrometer under different light conditions.
        :param i_index:  An integer representing the selected spectrometer index.
        :param i_saturation:  A double precision floating-point number representing the
        target saturation level for automatic integration.
        :param i_integration:  A double precision floating-point number representing the
        automatic integration time obtained.
        :param i_averaging:  An integer representing the automatic averaging count
        obtained.
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_INVALID_SATURATION = -13
        ERR_INVALID_AUTO_INT= -22
        ERR_UNKNOWN = -99
        """
        return LC.LC_AutoIntegration(i_index, i_saturation, i_integration, i_averaging)

    @staticmethod
    def lc_setintegration(i_index, i_integration, i_averaging):
        """
        To set the integration time and averaging count for the selected
        spectrometer.
        :param i_index:  An integer representing the selected spectrometer index.
        :param i_integration:  A double precision floating-point number representing the
        integration time for the selected spectrometer.
        :param i_averaging:  An integer representing the averaging count for the selected
        spectrometer
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_INVALID_INT_TIME = -11
        ERR_INVALID_AVERAGING= -12
        ERR_UNKNOWN = -99
        """
        return LC.LC_SetIntegration(i_index, i_integration, i_averaging)

    @staticmethod
    def lc_getsaturation(i_ndex, i_integration, i_averaging, i_saturation):
        """
        To obtain the saturation level of a spectrometer's response at a specific
        integration time
        :param i_ndex:  An integer representing the selected spectrometer index.
        :param i_integration:  A double precision floating-point number representing the
        integration time for the selected spectrometer
        :param i_averaging:  An integer representing the averaging count for the selected
        spectrometer.
        :param i_saturation:  A double precision floating-point number representing
        saturation level of the spectrometer
        :return: Success：ERR_SUCCESS = 0
        Failure: ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_UNKNOWN = -99
        """
        return LC.LC_GetSaturation(i_ndex, i_integration, i_averaging, i_saturation)

    @staticmethod
    def lc_setautomaxintegration(i_index, i_maxintegration, i_maxaveraging):
        """
        To set the maximum integration time and maximum number of averages
        for the selected spectrometer
        :param i_index:  An integer representing the selected spectrometer index.
        :param i_maxintegration:   A double precision floating-point number representing
        the Maximum integration time for the selected spectrometer.
        :param i_maxaveraging:   An integer representing the Maximum averaging count
        for the selected spectrometer.
        :return: Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_UNKNOWN = -99
        """
        return LC.LC_SetAutoMaxIntegration(i_index, i_maxintegration, i_maxaveraging)

    @staticmethod
    def lc_getspectrum(i_index, i_darkmode, i_integration, i_averaging, i_spectrum):
        """
        To obtain the response data of the selected spectrometer in a specified
        mode.
        :param i_index:  Integer, the selected spectrometer's index
        :param i_darkmode:  Integer, mode selection
        0 - Obtain raw response data from the spectrometer
        1 - Obtain raw response data from the spectrometer with automatic dark
        spectrum subtraction
        2 - Obtain raw response data from the spectrometer with single dark
        spectrum subtraction
        :param i_integration:  Double precision floating-point, integration time
        :param i_averaging:  Integer, number of averages
        :param i_spectrum:  One-dimensional array of double precision floating-point, the
        obtained spectral response values.
        :return:  Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_INVALID_PARAMETER = -1
        ERR_UNKNOWN = -99
        """
        return LC.LC_GetSpectrum(i_index, i_darkmode, i_integration, i_averaging, i_spectrum)

    @staticmethod
    def lc_almp(i_index, i_darkmode, i_integration, i_averaging, i_almpsp, i_almpwave):
        """
        To calibrate the spectrometer system, you can use the spectral radiance
        data from a standard lamp.
        :param i_index:  Integer, the selected spectrometer's index
        :param i_darkmode:  Integer, mode selection
        1 - Obtain raw response data from the spectrometer with automatic dark
        spectrum subtraction
        2 - Obtain raw response data from the spectrometer with single dark
        spectrum subtraction
        :param i_integration:  Double precision floating-point, integration time
        :param i_averaging:  Integer, number of averages
        :param i_almpsp:  One-dimensional array of double precision floating-point,
        spectral radiance values of the standard lamp
        :param i_almpwave:  One-dimensional array of double precision floating-point,
        wavelength values of the standard lamp's spectral radiance
        :return:  Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_INVALID_ARRAY = -14
        ERR_UNKNOWN = -99
        """
        return LC.LC_ALMP(i_index, i_darkmode, i_integration, i_averaging, i_almpsp, i_almpwave)

    @staticmethod
    def lc_readfbr(i_index, i_file):
        """
        To import the calibration file for the spectrometer's standard lamp
        :param i_index:  Integer, the selected spectrometer's index
        :param i_file:  String, the complete path of the calibration file (.txt) for the selected
        spectrometer's standard lamp
        :return:  Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_FILE_NO_EXIST = -24
        ERR_INVALID_DEVICE_TYPE = -7
        ERR_INVALID_DEVICE_ID = -4
        ERR_UNKNOWN = -99
        """
        return LC.LC_ReadFbr(i_index, i_file)

    @staticmethod
    def lc_savefbr(i_index, i_usagemode, i_path):
        """
        To save the calibration file for the spectrometer's standard lamp.
        :param i_index:  Integer, the selected spectrometer's index
        :param i_usagemode:   Integer, the measurement usage mode of the spectrometer
        :param i_path:  String, the save path for the calibration file (.txt) of the
        spectrometer's standard lamp (automatically set filename as:
        Sp_spectrometer_serial_number.txt)
        :return:  Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_FILE_NO_EXIST = -24
        ERR_INVALID_PARAMETER = -1
        ERR_UNKNOWN = -99
        """
        return LC.LC_SaveFbr(i_index, i_usagemode, i_path)

    @staticmethod
    def lc_setzoomfactor(i_index, i_factor):
        """
        To set the overall scaling factor for a spectrum.
        :param i_index:  Integer, the selected spectrometer's index
        :param i_factor:   Double precision floating-point number, the overall scaling
        factor for the spectrum
        :return:  Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_INVALID_OPTICAL_PARAMETER = -10
        ERR_UNKNOWN = -99
        """
        return LC.LC_SetZoomFactor(i_index, i_factor)

    @staticmethod
    def lc_measure(i_index, i_integration, i_averaging, i_darkmode, i_aux, i_smooth):
        """
        To perform a spectral measurement with the spectrometer.
        :param i_index:  Integer, the selected spectrometer's index
        :param i_integration:  Double precision floating-point number, the integration time
        :param i_averaging:  Integer, the number of measurements to average
        :param i_darkmode:  Integer, the selection of dark spectrum mode to use:
        1 - Obtain the spectrometer's original response data after subtracting the
        automatically acquired dark spectrum
        2 - Obtain the spectrometer's original response data after subtracting a
        single acquired dark spectrum
        :param i_aux:  Boolean, whether to use auxiliary lamp compensation factors for
        correction
        :param i_smooth:  Integer, the number of pixels for rolling smoothing of the
        spectral response values
        :return:  Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_UNKNOWN = -99
        """
        return LC.LC_Measure(i_index, i_integration, i_averaging, i_darkmode, i_aux, i_smooth)

    @staticmethod
    def lc_measuredate(i_index, i_mpitestdataitem, i_data, i_datearray):
        """
        To perform a spectral measurement with the spectrometer.
        :param i_index:  Integer, the selected spectrometer's index
        :param i_mpitestdataitem:  Integer, mode selection:
        0 - Spectral total energy
        1 - Luminous flux (different modes represent different parameters)
        2 - CIE 1931 tristimulus value - X
        3 - CIE 1931 tristimulus value - Y
        4 - CIE 1931 tristimulus value - Z
        5 - CIE 1931 chromaticity coordinate - Cx
        6 - CIE 1931 chromaticity coordinate - Cy
        7 - CIE 1960 chromaticity coordinate - u
        8 - CIE 1960 chromaticity coordinate - v
        9 - CIE 1976 chromaticity coordinate - u'
        10 - CIE 1976 chromaticity coordinate - v'
        11 - Correlated color temperature (in Kelvin)
        12 - Color difference level between Duv and blackbody radiation color
        temperature
        13 - Peak wavelength (in nm)
        14 - Full width at half maximum (in nm)
        15 - Energy at peak wavelength
        16 - Pixel value at peak wavelength
        17 - Wavelength at pixel value peak (in nm)
        18 - Energy at pixel value peak
        19 - Existence of dominant wavelength
        20 - Dominant wavelength/complementary dominant wavelength (in nm)
        21 - Purity
        31 - Color rendering index Ra
        32~46 - Color rendering index R1~R15
        801 - Spectral wavelength
        802 - Spectral response value
        901 - Integration time for this test (in ms)
        902 - Number of averages for this test
        903 - Spectral response saturation for this test
        904 - Time taken for this test (in ms)
        905 - Spectrometer mode used for this test
        :param i_data:  Double precision floating-point number, the value returned for the
        selected mode
        :param i_datearray:  One-dimensional array of double precision floating-point
        numbers, the values returned for the selected mode (valid for 801/802)
        :return:  Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_INVALID_ACTIVATE = -2
        ERR_UNKNOWN = -99
        """
        return LC.LC_MeasureDate(i_index, i_mpitestdataitem, i_data, i_datearray)

    @staticmethod
    def checkcaserror(i_index, i_errorinformation):
        """
        To retrieve error information from a spectrometer.
        :param i_index:  Integer, the selected spectrometer's index
        :param i_errorinformation:  String, the obtained error content information from
        the current spectrometer
        :return:  Success：ERR_SUCCESS = 0
        Failure：ERR_INDEX_EXCEED_LIMIT = -19
        ERR_UNKNOWN = -99
        """
        return LC.LC_CheckCaSerror(i_index, i_errorinformation)
