#!/usr/bin/python3.3

from configparser import SafeConfigParser
import os
import subprocess

# Main Window
global mainWindowTitle
global btnMainScanTitle
global btnMainUpdateTitle
global btnMainStatusTitle
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
global mustSudo
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
global noProxyTitle
global yesProxyTitle
global dependsProxyTitle
global autoProxyAuthTitle
global basicProxyAuthTitle
global ntlmProxyAuthTitle
global needRestartTitle
global noPasswordInserted
global noEmailInserted
global noCorrectMailAddress
global passwordsDoNotMatch
global mustFillInAllFields
global historyLog

# Status Widget
global programInfo
global avgTitle
global lastUpdateTitle
global licenceTitle
global aviUsedTitle
global aviDateTitle
global serviceStatusTitle
global oadStatusTitle
global genericON
global genericOFF
global schedStatusTitle
global nextiAVIupdate
global nextProgramUpdate

# Show Scan Results Widget
global attentionMsg
global scanResultsDialogTitle

# Table Column Headers
global userTitle
global noOfResultsTitle
global scanDateTimeTitle
global virusDBTitle
global malwareFoundTitle
global updateDateTimeTitle
global coreAndVirusDBVersionsTitle
global threats
global filesInfected

# Real Time Messages
global translationDict

def setuplang():

	#Main Window
	global mainWindowTitle
	global btnMainScanTitle
	global btnMainUpdateTitle
	global btnMainStatusTitle
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
	
	# Informative / Warning / Error Messages
	global mustSudo
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
	global noProxyTitle
	global yesProxyTitle
	global dependsProxyTitle
	global autoProxyAuthTitle
	global basicProxyAuthTitle
	global ntlmProxyAuthTitle
	global needRestartTitle
	global noPasswordInserted
	global noEmailInserted
	global noCorrectMailAddress
	global passwordsDoNotMatch
	global mustFillInAllFields
	global historyLog
	
	# Scan Progress
	global dialogScanProgressTitle
	global dialogScanProgressStopTitle
	
	# Status Widget
	global programInfo
	global avgTitle
	global lastUpdateTitle
	global licenceTitle
	global aviUsedTitle
	global aviDateTitle
	global serviceStatusTitle
	global oadStatusTitle
	global genericON
	global genericOFF
	global schedStatusTitle
	global nextiAVIupdate
	global nextProgramUpdate
	
	# Show Scan Results Widget
	global attentionMsg
	global scanResultsDialogTitle
	
	# Table Column Headers
	global userTitle
	global noOfResultsTitle
	global scanDateTimeTitle
	global virusDBTitle
	global malwareFoundTitle
	global updateDateTimeTitle
	global coreAndVirusDBVersionsTitle
	global noAccessRightsInFolder
	global threats
	global filesInfected
	
	# Real Time Messages
	global translationDict


	#print(subprocess.check_output(["ls"]))
	confile = os.getcwd() + "/conf/config.ini"
	configparser = SafeConfigParser()
	f = open(confile, 'r')
	configparser.read(confile)
	#print("Length is: " + str(len(configparser.sections())))
	lang = configparser.get("Language", 'lang')
	#print(str(lang))
	
	if lang == "EL":
		import conf.language.greek as langpack
	elif lang == "EN":
		import conf.language.english as langpack
	
	# Main Window
	mainWindowTitle = langpack.mainWindowTitle
	btnMainScanTitle = langpack.btnMainScanTitle
	btnMainUpdateTitle = langpack.btnMainUpdateTitle
	btnMainStatusTitle = langpack.btnMainStatusTitle
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
	mustSudo = langpack.mustSudo
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
	noProxyTitle = langpack.noProxyTitle
	yesProxyTitle = langpack.yesProxyTitle
	dependsProxyTitle = langpack.dependsProxyTitle
	autoProxyAuthTitle = langpack.autoProxyAuthTitle
	basicProxyAuthTitle = langpack.basicProxyAuthTitle
	ntlmProxyAuthTitle = langpack.ntlmProxyAuthTitle
	needRestartTitle = langpack.needRestartTitle
	noPasswordInserted = langpack.noPasswordInserted
	noEmailInserted = langpack.noEmailInserted
	noCorrectMailAddress = langpack.noCorrectMailAddress
	passwordsDoNotMatch = langpack.passwordsDoNotMatch
	mustFillInAllFields = langpack.mustFillInAllFields
	historyLog = langpack.historyLog
	
	# Status Widget
	programInfo  = langpack.programInfo
	avgTitle = langpack.avgTitle
	lastUpdateTitle = langpack.lastUpdateTitle
	licenceTitle = langpack.licenceTitle
	aviUsedTitle = langpack.aviUsedTitle
	aviDateTitle = langpack.aviDateTitle
	serviceStatusTitle = langpack.serviceStatusTitle
	oadStatusTitle = langpack.oadStatusTitle
	genericON = langpack.genericON
	genericOFF = langpack.genericOFF
	schedStatusTitle = langpack.schedStatusTitle
	nextiAVIupdate = langpack.nextiAVIupdate
	nextProgramUpdate = langpack.nextProgramUpdate
	
	# Show Scan Results Widget
	attentionMsg = langpack.attentionMsg
	scanResultsDialogTitle = langpack.scanResultsDialogTitle
	
	# Table Column Labels
	userTitle  = langpack.userTitle
	noOfResultsTitle = langpack.noOfResultsTitle
	scanDateTimeTitle = langpack.scanDateTimeTitle
	virusDBTitle = langpack.virusDBTitle
	malwareFoundTitle = langpack.malwareFoundTitle
	updateDateTimeTitle = langpack.updateDateTimeTitle
	coreAndVirusDBVersionsTitle = langpack.coreAndVirusDBVersionsTitle
	threats = langpack.threats
	filesInfected = langpack.filesInfected
	
	# Real Time Messages
	translationDict = langpack.translationDict
