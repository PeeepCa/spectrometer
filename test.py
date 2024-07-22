import Py_LcSpvis


path = 'C:\\Users\\pokorny\\OneDrive - APAG Elektronik s.r.o\\Documents\\GitHub\\spectrometer\\library'
license = ('C:\\Users\\pokorny\\OneDrive - APAG Elektronik s.r.o\\Documents\\GitHub\\spectrometer\\license\\LDA~G40090129_1.5.spt')
calibration = ('C:\\Users\\pokorny\\OneDrive - APAG Elektronik s.r.o\\Documents\\GitHub\\spectrometer\\license\\Sp_LDA~G40090129.txt')

# Initialization
Py_LcSpvis.BlockingFunctions.__init__(Py_LcSpvis, path)
print("Number of devices: ", Py_LcSpvis.BlockingFunctions.lc_init())
index, sn = Py_LcSpvis.BlockingFunctions.lc_getlist(0, '')
print('Index: ', index, 'SN: ', sn)
print('Activation: ', Py_LcSpvis.BlockingFunctions.lc_activate(0, license))
print('Calibration: ', Py_LcSpvis.BlockingFunctions.lc_readfbr(0, calibration))

# Sequence
input('Press Enter to calibration Auto dark...')
print('Auto dark: ', Py_LcSpvis.BlockingFunctions.lc_autodark(0, 100))
input('Press Enter to measure...')
print("Measure: ", Py_LcSpvis.BlockingFunctions.lc_measure(0, 100, 5, 0, False, 0))
print('CIEX: ', Py_LcSpvis.BlockingFunctions.lc_measuredate(0, 5, 0, [])[1])
print('CIEY: ', Py_LcSpvis.BlockingFunctions.lc_measuredate(0, 6, 0, [])[1])
print('Luminous flux: ',  Py_LcSpvis.BlockingFunctions.lc_measuredate(0, 1, 0, [])[1])

# data = Py_LcSpvis.BlockingFunctions.lc_measuredate(0, 1, 0, [])
# print(data[0], data[1], data[2])
# myData_list = []
# for row in data[2]:
#     myData_list.append(row)
# print(myData_list)

# Close
print('Done: ', Py_LcSpvis.BlockingFunctions.lc_done(0))