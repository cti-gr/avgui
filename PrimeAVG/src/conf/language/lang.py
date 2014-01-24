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

# Scan Progress
global dialogScanProgressTitle
global dialogScanProgressStopTitle

# Update Process
global dialogUpdateProgTitle
global btnExitUpdateProgTitle

# Check Panel
global formCheckTitle
global btnExitFormCheckTitle

# Update Dialog
global dialogUpdateTitle
global btnUpdateTitle
global btnUpdateSetTitle
global btnUpdateCheckTitle
global btnExitUpdateDialogTitle

# Update Settings
global dialogUpdateSettingsTitle
global lblInterruptTitle
global lblMinSpeedTitle
global lblMaxTimeTitle
global lblProxyTitle
global lblProxyPassTitle
global lblProxyModeTitle
global lblProxyNameTitle
global lblProxyUsernameTitle
global lblUseLogInTitle
global lblProxyAuthTypeTitle
global lblProxyPortTitle
global btnOkUpdateSettingsTitle
global btnCancelUpdateSettingsTitle
global lblAutoUpdateProgTitle
global lblAutoUpdateVirTitle

# History Dialog
global dialogHistoryTitle
global lblToTitle
global lblFromTitle
global lblMalwareTitle
global lblDatabaseTable
global btnExecuteTitle
global historyTabWidgetScansTitle
global historyTabWidgetUpdatesTitle
global btnHistoryDBTitle
global btnExitHistoryTitle

# Scan History Results
global dialogHistoryScanResultsTitle
global extractToTextTitle
global btnDialogHistoryScanResultsTitle


# Count Down 
global formCountDownTitle
global lblCountDownTitle
global lblCountDownTimeToCompletionTitle

# Problem Submission
global dialogProblemTitle
global lblUserTitle
global lblAvgTitle
global lblKernelTitle
global lblUbuntuTitle
global lblAvguiTitle
global btnSubmitProblemSubmissionTitle
global btnCancelProblemSubmissionTitle
global lblProbDescTitle

# Informative / Warning / Error Messages
global dbHistoryMustSudo
global unableToCheckDirRights
global attention
global virusDBCmbInitError
global malwareCmbInitError
global noFilesChosen
global terminateScan
global noFileNameProvided
global noAccessRights
global scanFolderTitle
global scanFileTitle
global applicationError
global chooseFileToScan
global chooseFileToScan
global wrongDates1
global wrongDates2
global noResults
global noResultsCriteria
global chooseFolderToStoreText
global noAccessRightsInFolder
global errorStoringFile
global restartUpdate
global chooseFileToScan
global chooseFolderToScan

# Table Column Headers
global userTitle
global noOfResultsTitle
global scanDateTimeTitle
global virusDBTitle
global malwareFoundTitle
global updateDateTimeTitle
global coreAndVirusDBVersionsTitle

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

	# Update Process
	global dialogUpdateProgTitle
	global btnExitUpdateProgTitle
	
	# Check Panel
	global formCheckTitle
	global btnExitFormCheckTitle
	
	# Update Dialog
	global dialogUpdateTitle
	global btnUpdateTitle
	global btnUpdateSetTitle
	global btnUpdateCheckTitle
	global btnExitUpdateDialogTitle
	
	# Update Settings
	global dialogUpdateSettingsTitle
	global lblInterruptTitle
	global lblMinSpeedTitle
	global lblMaxTimeTitle
	global lblProxyTitle
	global lblProxyPassTitle
	global lblProxyModeTitle
	global lblProxyNameTitle
	global lblProxyUsernameTitle
	global lblUseLogInTitle
	global lblProxyAuthTypeTitle
	global lblProxyPortTitle
	global btnOkUpdateSettingsTitle
	global btnCancelUpdateSettingsTitle
	global lblAutoUpdateProgTitle
	global lblAutoUpdateVirTitle
	
	# History Dialog
	global dialogHistoryTitle
	global lblToTitle
	global lblFromTitle
	global lblMalwareTitle
	global lblDatabaseTable
	global btnExecuteTitle
	global historyTabWidgetScansTitle
	global historyTabWidgetUpdatesTitle
	global btnHistoryDBTitle
	global btnExitHistoryTitle
	
	# Scan History Results
	global dialogHistoryScanResultsTitle
	global extractToTextTitle
	global btnDialogHistoryScanResultsTitle
	
	# Count Down 
	global formCountDownTitle
	global lblCountDownTitle
	global lblCountDownTimeToCompletionTitle
	
	# Problem Submission
	global dialogProblemTitle
	global lblUserTitle
	global lblAvgTitle
	global lblKernelTitle
	global lblUbuntuTitle
	global lblAvguiTitle
	global btnSubmitProblemSubmissionTitle
	global btnCancelProblemSubmissionTitle
	global lblProbDescTitle
	
	# Warning / Error Messages
	global dbHistoryMustSudo
	global unableToCheckDirRights
	global attention
	global virusDBCmbInitError
	global malwareCmbInitError
	global errorQueringDB
	global noFilesChosen
	global terminateScan
	global noFileNameProvided
	global noAccessRights
	global scanFolderTitle
	global scanFileTitle
	global applicationError
	global chooseFileToScan
	global chooseFileToScan
	global wrongDates1
	global wrongDates2
	global noResults
	global noResultsCriteria
	global chooseFolderToStoreText
	global errorStoringFile
	global restartUpdate
	global chooseFileToScan
	global chooseFolderToScan
	
	# Scan Progress
	global dialogScanProgressTitle
	global dialogScanProgressStopTitle
	
	# Table Column Headers
	global userTitle
	global noOfResultsTitle
	global scanDateTimeTitle
	global virusDBTitle
	global malwareFoundTitle
	global updateDateTimeTitle
	global coreAndVirusDBVersionsTitle
	global noAccessRightsInFolder


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
	
	# Scan Progress
	dialogScanProgressTitle = langpack.dialogScanProgressTitle
	dialogScanProgressStopTitle = langpack.dialogScanProgressStopTitle
	
	# Update Process
	dialogUpdateProgTitle = langpack.dialogUpdateProgTitle
	btnExitUpdateProgTitle = langpack.btnExitUpdateProgTitle
	
	# Check Panel
	formCheckTitle = langpack.formCheckTitle
	btnExitFormCheckTitle = langpack.btnExitFormCheckTitle
	
	# Update Dialog
	dialogUpdateTitle = langpack.dialogUpdateTitle
	btnUpdateTitle = langpack.btnUpdateTitle
	btnUpdateSetTitle = langpack.btnUpdateSetTitle
	btnUpdateCheckTitle = langpack.btnUpdateCheckTitle
	btnExitUpdateDialogTitle = langpack.btnExitUpdateDialogTitle
	
	# Update Settings
	dialogUpdateSettingsTitle = langpack.dialogUpdateSettingsTitle
	lblInterruptTitle = langpack.lblInterruptTitle
	lblMinSpeedTitle = langpack.lblMinSpeedTitle 
	lblMaxTimeTitle = langpack.lblMaxTimeTitle
	lblProxyTitle = langpack.lblProxyTitle
	lblProxyPassTitle = langpack.lblProxyPassTitle
	lblProxyModeTitle = langpack.lblProxyModeTitle
	lblProxyNameTitle = langpack.lblProxyNameTitle
	lblProxyUsernameTitle = langpack.lblProxyUsernameTitle
	lblUseLogInTitle = langpack.lblUseLogInTitle
	lblProxyAuthTypeTitle = langpack.lblProxyAuthTypeTitle
	lblProxyPortTitle = langpack.lblProxyPortTitle
	btnOkUpdateSettingsTitle = langpack.btnOkUpdateSettingsTitle
	btnCancelUpdateSettingsTitle = langpack.btnCancelUpdateSettingsTitle
	lblAutoUpdateProgTitle = langpack.lblAutoUpdateProgTitle
	lblAutoUpdateVirTitle = langpack.lblAutoUpdateVirTitle
	
	# History Dialog
	dialogHistoryTitle = langpack.dialogHistoryTitle
	lblToTitle = langpack.lblToTitle
	lblFromTitle = langpack.lblFromTitle
	lblMalwareTitle = langpack.lblMalwareTitle
	lblDatabaseTable = langpack.lblDatabaseTable
	btnExecuteTitle = langpack.btnExecuteTitle
	historyTabWidgetScansTitle = langpack.historyTabWidgetScansTitle
	historyTabWidgetUpdatesTitle = langpack.historyTabWidgetUpdatesTitle
	btnHistoryDBTitle = langpack.btnHistoryDBTitle
	btnExitHistoryTitle = langpack.btnExitHistoryTitle
	
	# Scan History Results
	dialogHistoryScanResultsTitle = langpack.dialogHistoryScanResultsTitle
	extractToTextTitle = langpack.extractToTextTitle
	btnDialogHistoryScanResultsTitle = langpack.btnDialogHistoryScanResultsTitle

	
	# Count Down
	formCountDownTitle = langpack.formCountDownTitle
	lblCountDownTitle = langpack.lblCountDownTitle
	lblCountDownTimeToCompletionTitle = langpack.lblCountDownTimeToCompletionTitle
	
	# Problem Submission
	dialogProblemTitle = langpack.dialogProblemTitle
	lblUserTitle = langpack.lblUserTitle
	lblAvgTitle = langpack.lblAvgTitle
	lblKernelTitle = langpack.lblKernelTitle
	lblUbuntuTitle = langpack.lblUbuntuTitle
	lblAvguiTitle = langpack.lblAvguiTitle
	btnSubmitProblemSubmissionTitle = langpack.btnSubmitProblemSubmissionTitle
	btnCancelProblemSubmissionTitle = langpack.btnCancelProblemSubmissionTitle
	lblProbDescTitle = langpack.lblProbDescTitle
	
	# Informative / Warning / Error Messages
	dbHistoryMustSudo = langpack.dbHistoryMustSudo
	unableToCheckDirRights = langpack.unableToCheckDirRights
	attention = langpack.attention
	virusDBCmbInitError = langpack.virusDBCmbInitError
	malwareCmbInitError = langpack.malwareCmbInitError
	errorQueringDB = langpack.errorQueringDB
	noFilesChosen = langpack.noFilesChosen
	terminateScan = langpack.terminateScan
	noFileNameProvided = langpack.noFileNameProvided
	noAccessRights = langpack.noAccessRights
	scanFolderTitle = langpack.scanFolderTitle
	scanFileTitle = langpack.scanFileTitle
	applicationError = langpack.applicationError
	chooseFileToScan = langpack.chooseFileToScan
	chooseFolderToScan = langpack.chooseFileToScan
	wrongDates1 = langpack.wrongDates1
	wrongDates2 = langpack.wrongDates2
	noResults = langpack.noResults
	noResultsCriteria = langpack.noResultsCriteria
	chooseFolderToStoreText = langpack.chooseFolderToStoreText
	noAccessRightsInFolder = langpack.noAccessRightsInFolder
	errorStoringFile = langpack.errorStoringFile
	restartUpdate = langpack.restartUpdate

	# Table Column Labels
	userTitle  = langpack.userTitle
	noOfResultsTitle = langpack.noOfResultsTitle
	scanDateTimeTitle = langpack.scanDateTimeTitle
	virusDBTitle = langpack.virusDBTitle
	malwareFoundTitle = langpack.malwareFoundTitle
