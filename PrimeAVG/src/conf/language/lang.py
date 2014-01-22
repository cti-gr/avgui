#!/usr/bin/python3.3

from configparser import SafeConfigParser
import os
import subprocess

# Main Window
global mainWindowTitle
global btnMainScanTitle
global btnMainUpdateTitle
global btnMainIssueTitle
global btnMainHistoryTitle
global btnExitTitle
global lblAboutTitle
global lblAvgProtectionTitle
global lblGraphicFrameworkTitle

# Scan Dialog
global dialogScanTitle
global btnBeginScanTitle
global btnScanSettingsTitle
global btnChooseFolderTitle
global lblFoldersSelectedTitle
global btnExitScanTitle

# Scan Settings
global dialogScanSettingsTitle
global chkbIfTypeTitle
global chkbFileStoreTitle
global btnSelectFolderTitle
global chkbBackUpFilesTitle
global chkbArchiveTitle
global chkbBootSecTitle
global chkbCookiesTitle
global chkbMultimediaTitle
global lblHandleTitle
global radioDeleteTitle
global radioHealTitle
global radioVaultTitle
global btnScanSettingsCancelTitle

# Scan Select
global dialogScanSelectTitle
global lblScanSelectTitle
global radioFileTitle
global radioFolderTitle
global btnExitScanSelectTitle

def setuplang():

	#Main Window
	global mainWindowTitle
	global btnMainScanTitle
	global btnMainUpdateTitle
	global btnMainIssueTitle
	global btnMainHistoryTitle
	global lblAboutTitle
	global lblAvgProtectionTitle
	global lblGraphicFrameworkTitle
	global btnExitTitle
	
	# Scan Dialog
	global dialogScanTitle
	global btnBeginScanTitle
	global btnScanSettingsTitle
	global btnChooseFolderTitle
	global lblFoldersSelectedTitle
	global btnExitScanTitle
	
	# Scan Settings
	global dialogScanSettingsTitle
	global chkbIfTypeTitle
	global chkbFileStoreTitle
	global btnSelectFolderTitle
	global chkbBackUpFilesTitle
	global chkbArchiveTitle
	global chkbBootSecTitle
	global chkbCookiesTitle
	global chkbMultimediaTitle
	global lblHandleTitle
	global radioDeleteTitle
	global radioHealTitle
	global radioVaultTitle
	global btnScanSettingsCancelTitle
	
	# Scan Select
	global dialogScanSelectTitle
	global lblScanSelectTitle
	global radioFileTitle
	global radioFolderTitle
	global btnExitScanSelectTitle

	
	print(subprocess.check_output(["ls"]))
	confile = os.getcwd() + "/conf/config.ini"
	configparser = SafeConfigParser()
	f = open(confile, 'r')
	configparser.read(confile)
	print("Length is: " + str(len(configparser.sections())))
	lang = configparser.get("Language", 'lang')
	print(str(lang))
	
	if lang == "el-gr":
		import conf.language.greek as langpack
	elif lang == "en-gb":
		import conf.language.english as langpack
	
	# Main Window
	mainWindowTitle = langpack.mainWindowTitle
	btnMainScanTitle = langpack.btnMainScanTitle
	btnMainUpdateTitle = langpack.btnMainUpdateTitle
	btnMainIssueTitle = langpack.btnMainIssueTitle
	btnMainHistoryTitle = langpack.btnMainHistoryTitle
	btnExitTitle = langpack.btnExitTitle
	lblAboutTitle = langpack.lblAboutTitle
	lblAvgProtectionTitle = langpack.lblAvgProtectionTitle
	lblGraphicFrameworkTitle = langpack.lblGraphicFrameworkTitle
	
	# Scan Dialog
	dialogScanTitle = langpack.dialogScanTitle
	btnBeginScanTitle = langpack.btnBeginScanTitle
	btnScanSettingsTitle = langpack.btnScanSettingsTitle
	btnChooseFolderTitle = langpack.btnChooseFolderTitle
	lblFoldersSelectedTitle = langpack.lblFoldersSelectedTitle
	btnExitScanTitle = langpack.btnExitScanTitle
	
	# Scan Settings
	dialogScanSettingsTitle  = langpack.dialogScanSettingsTitle
	chkbIfTypeTitle  = langpack.chkbIfTypeTitle
	chkbFileStoreTitle  = langpack.chkbFileStoreTitle
	btnSelectFolderTitle  = langpack.btnSelectFolderTitle
	chkbBackUpFilesTitle  = langpack.chkbBackUpFilesTitle
	chkbArchiveTitle  = langpack.chkbArchiveTitle
	chkbBootSecTitle  = langpack.chkbBootSecTitle
	chkbCookiesTitle  = langpack.chkbCookiesTitle
	chkbMultimediaTitle  = langpack.chkbMultimediaTitle
	lblHandleTitle  = langpack.lblHandleTitle
	radioDeleteTitle  = langpack.radioDeleteTitle
	radioHealTitle  = langpack.radioHealTitle
	radioVaultTitle  = langpack.radioVaultTitle
	btnScanSettingsCancelTitle = langpack.btnScanSettingsCancelTitle
	
	# Scan Select
	dialogScanSelectTitle = langpack.dialogScanSelectTitle
	lblScanSelectTitle = langpack.lblScanSelectTitle
	radioFileTitle = langpack.radioFileTitle
	radioFolderTitle = langpack.radioFolderTitle
	btnExitScanSelectTitle = langpack.btnExitScanSelectTitle
