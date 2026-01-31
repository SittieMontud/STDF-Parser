from pywinauto.application import Application
import time

def OpenSTDFReader(stdFileName, appPath):
	#stdfexe = Application().start(appPath + "\StdfReader.exe", timeout = 10)
	stdfexe = Application().start("D:\PYTHON\STDF_TO_ASCII_CONVERTER\StdfReader.exe", timeout = 10)
	maindlg = stdfexe.window(title = "StdfReader")
	maindlg.print_control_identifiers()
	maindlg.Properties.child_window(class_name="Edit")

	maindlg.STDF_FILENAME_Edit.set_text(stdFileName)
	maindlg.OKButton.click()

	#stdfexe.kill()
	time.sleep(1)