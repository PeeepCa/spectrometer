#region 程序集 LcSpvis_XS, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
// C:\A-Work\App\Spvis光谱仪\二次开发包及示例程序\LC Spvis Demo v2.0\LC Spvis Demo v2.0\bin\Debug\LcSpvis_XS.dll
#endregion

namespace LcSpvis
{
    public class LC_SpFunc_XS
    {
        public LC_SpFunc_XS();

        public int CheckCASError(int l_Index, out string l_ErrorInformation);
        public int LC_Activate(int l_Index, string l_File);
        public int LC_Almp(int l_Index, int l_DarkModul, double l_Integration, int l_Averaging, double[] l_AlmpSp, double[] l_AlmpWave);
        public int LC_AutoDark(int l_Index, double l_Integration);
        public int LC_AutoIntegration(int l_Index, double l_Saturation, ref double l_Integration, ref int l_Averaging, int l_Fck, int l_Period, int l_M, int l_N);
        public int LC_AutoIntegration(int l_Index, double l_Saturation, ref double l_Integration, ref int l_Averaging);
        public int LC_AutoIntegrationSTD(int l_Index, double l_Saturation, ref double l_Integration, ref int l_Averaging);
        public int LC_CCT(int l_Index, int l_DarkModul, double l_Integration, int l_Averaging, double l_CCT, double l_Flux);
        public int LC_DarkCompensation(int l_Index, int l_UsageMode, double l_Integration = 1000);
        public int LC_Done(int l_Index);
        public int LC_DoneAll();
        public int LC_GetAuxSpectrum(int l_Index, double[] l_AuxLmp, double[] l_AuxTest);
        public int LC_GetList(int l_Index, ref string l_SerialNumber);
        public int LC_GetParameters(int l_Index, int l_mpiParametersNo, ref double[] l_Parameters);
        public int LC_GetParameters(int l_Index, int l_mpiParametersNo, ref string l_Parameters);
        public int LC_GetSaturation(int l_Index, double l_Integration, int l_Averaging, ref double l_Saturation);
        public int LC_GetSpectrum(int l_Index, int l_DarkMode, double l_Integration, int l_Averaging, ref double[] l_Spectrum);
        public int LC_GetXYZFactor(int l_Index, ref double[] l_FactorXYZ);
        public int LC_GetZoomFactor(int l_Index, ref double l_Factor);
        public int LC_Init();
        public int LC_Measure(int l_Index, double l_Integration, int l_Averaging, int l_DarkMode, bool l_Aux, int l_Smooth);
        public int LC_MeasureDate(int l_Index, int l_mpiTestDataItem, ref double l_Data, ref double[] l_DateArray);
        public int LC_MeasureDate(int l_Index, ref StdSpectralData l_TestData);
        public int LC_OnceDark(int l_Index, double l_Integration, int l_Averaging);
        public int LC_ReadAux(int l_Index, string l_File);
        public int LC_ReadFbr(int l_Index, string l_File);
        public int LC_SaveAux(int l_Index, string l_Path);
        public int LC_SaveFbr(int l_Index, int l_UsageMode, string l_Path);
        public int LC_SetAutoMaxIntegration(int l_Index, ref double l_MaxIntegration, ref int l_MaxAveraging);
        public int LC_SetIntegration(int l_Index, double l_Integration, int l_Averaging);
        public int LC_SetXYZFactor(int l_Index, double[] l_FactorXYZ);
        public int LC_SetZoomFactor(int l_Index, double l_Factor);
        public int LC_Shutter(int l_Index, bool l_TrueIsOpen);
    }
}