from ctypes import *
from enum import Enum
import ctypes
import os
import sys

if (os.name == 'nt' and sys.version_info[:2] >= (3,8)):
  lib = ctypes.CDLL('mdName.dll', winmode=0)
elif (os.name == 'nt'):
  lib = ctypes.CDLL('mdName.dll')
else:
  lib = ctypes.CDLL('libmdName.so')

lib.mdNameCreate.argtypes = []
lib.mdNameCreate.restype = c_void_p
lib.mdNameDestroy.argtypes = [c_void_p]
lib.mdNameDestroy.restype = None
lib.mdNameSetPathToNameFiles.argtypes = [c_void_p, c_char_p]
lib.mdNameSetPathToNameFiles.restype = None
lib.mdNameInitializeDataFiles.argtypes = [c_void_p]
lib.mdNameInitializeDataFiles.restype = c_int
lib.mdNameGetInitializeErrorString.argtypes = [c_void_p]
lib.mdNameGetInitializeErrorString.restype = c_char_p
lib.mdNameSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdNameSetLicenseString.restype = c_int
lib.mdNameGetBuildNumber.argtypes = [c_void_p]
lib.mdNameGetBuildNumber.restype = c_char_p
lib.mdNameGetDatabaseDate.argtypes = [c_void_p]
lib.mdNameGetDatabaseDate.restype = c_char_p
lib.mdNameGetDatabaseExpirationDate.argtypes = [c_void_p]
lib.mdNameGetDatabaseExpirationDate.restype = c_char_p
lib.mdNameGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdNameGetLicenseExpirationDate.restype = c_char_p
lib.mdNameSetPrimaryNameHint.argtypes = [c_void_p, c_int]
lib.mdNameSetPrimaryNameHint.restype = c_int
lib.mdNameSetSecondaryNameHint.argtypes = [c_void_p, c_int]
lib.mdNameSetSecondaryNameHint.restype = c_int
lib.mdNameSetFirstNameSpellingCorrection.argtypes = [c_void_p, c_int]
lib.mdNameSetFirstNameSpellingCorrection.restype = c_int
lib.mdNameSetMiddleNameLogic.argtypes = [c_void_p, c_int]
lib.mdNameSetMiddleNameLogic.restype = c_int
lib.mdNameSetGenderPopulation.argtypes = [c_void_p, c_int]
lib.mdNameSetGenderPopulation.restype = c_int
lib.mdNameSetGenderAggression.argtypes = [c_void_p, c_int]
lib.mdNameSetGenderAggression.restype = c_int
lib.mdNameAddSalutation.argtypes = [c_void_p, c_int]
lib.mdNameAddSalutation.restype = c_int
lib.mdNameSetSalutationPrefix.argtypes = [c_void_p, c_char_p]
lib.mdNameSetSalutationPrefix.restype = None
lib.mdNameSetSalutationSuffix.argtypes = [c_void_p, c_char_p]
lib.mdNameSetSalutationSuffix.restype = None
lib.mdNameSetSalutationSlug.argtypes = [c_void_p, c_char_p]
lib.mdNameSetSalutationSlug.restype = None
lib.mdNameClearProperties.argtypes = [c_void_p]
lib.mdNameClearProperties.restype = None
lib.mdNameSetFullName.argtypes = [c_void_p, c_char_p]
lib.mdNameSetFullName.restype = None
lib.mdNameSetPrefix.argtypes = [c_void_p, c_char_p]
lib.mdNameSetPrefix.restype = None
lib.mdNameSetPrefix2.argtypes = [c_void_p, c_char_p]
lib.mdNameSetPrefix2.restype = None
lib.mdNameSetFirstName.argtypes = [c_void_p, c_char_p]
lib.mdNameSetFirstName.restype = None
lib.mdNameSetFirstName2.argtypes = [c_void_p, c_char_p]
lib.mdNameSetFirstName2.restype = None
lib.mdNameSetMiddleName.argtypes = [c_void_p, c_char_p]
lib.mdNameSetMiddleName.restype = None
lib.mdNameSetMiddleName2.argtypes = [c_void_p, c_char_p]
lib.mdNameSetMiddleName2.restype = None
lib.mdNameSetSuffix.argtypes = [c_void_p, c_char_p]
lib.mdNameSetSuffix.restype = None
lib.mdNameSetSuffix2.argtypes = [c_void_p, c_char_p]
lib.mdNameSetSuffix2.restype = None
lib.mdNameSetLastName.argtypes = [c_void_p, c_char_p]
lib.mdNameSetLastName.restype = None
lib.mdNameSetLastName2.argtypes = [c_void_p, c_char_p]
lib.mdNameSetLastName2.restype = None
lib.mdNameParse.argtypes = [c_void_p]
lib.mdNameParse.restype = c_int
lib.mdNameGenderize.argtypes = [c_void_p]
lib.mdNameGenderize.restype = c_int
lib.mdNameSalutate.argtypes = [c_void_p]
lib.mdNameSalutate.restype = c_int
lib.mdNameGetStatusCode.argtypes = [c_void_p]
lib.mdNameGetStatusCode.restype = c_char_p
lib.mdNameGetErrorCode.argtypes = [c_void_p]
lib.mdNameGetErrorCode.restype = c_char_p
lib.mdNameGetChangeCode.argtypes = [c_void_p]
lib.mdNameGetChangeCode.restype = c_char_p
lib.mdNameGetResults.argtypes = [c_void_p]
lib.mdNameGetResults.restype = c_char_p
lib.mdNameGetResultCodeDescription.argtypes = [c_void_p, c_char_p, c_int]
lib.mdNameGetResultCodeDescription.restype = c_char_p
lib.mdNameGetPrefix.argtypes = [c_void_p]
lib.mdNameGetPrefix.restype = c_char_p
lib.mdNameGetPrefix2.argtypes = [c_void_p]
lib.mdNameGetPrefix2.restype = c_char_p
lib.mdNameGetFirstName.argtypes = [c_void_p]
lib.mdNameGetFirstName.restype = c_char_p
lib.mdNameGetFirstName2.argtypes = [c_void_p]
lib.mdNameGetFirstName2.restype = c_char_p
lib.mdNameGetMiddleName.argtypes = [c_void_p]
lib.mdNameGetMiddleName.restype = c_char_p
lib.mdNameGetMiddleName2.argtypes = [c_void_p]
lib.mdNameGetMiddleName2.restype = c_char_p
lib.mdNameGetLastName.argtypes = [c_void_p]
lib.mdNameGetLastName.restype = c_char_p
lib.mdNameGetLastName2.argtypes = [c_void_p]
lib.mdNameGetLastName2.restype = c_char_p
lib.mdNameGetSuffix.argtypes = [c_void_p]
lib.mdNameGetSuffix.restype = c_char_p
lib.mdNameGetSuffix2.argtypes = [c_void_p]
lib.mdNameGetSuffix2.restype = c_char_p
lib.mdNameGetGender.argtypes = [c_void_p]
lib.mdNameGetGender.restype = c_char_p
lib.mdNameGetGender2.argtypes = [c_void_p]
lib.mdNameGetGender2.restype = c_char_p
lib.mdNameGetSalutation.argtypes = [c_void_p]
lib.mdNameGetSalutation.restype = c_char_p
lib.mdNameStandardizeCompany.argtypes = [c_void_p, c_char_p]
lib.mdNameStandardizeCompany.restype = c_char_p
lib.mdNameSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdNameSetReserved.restype = None
lib.mdNameGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdNameGetReserved.restype = c_char_p

# mdName Enumerations
class ProgramStatus(Enum):
	NoError = 0
	ConfigFile = 1
	LicenseExpired = 2
	DatabaseExpired = 3
	Unknown = 4

class NameHints(Enum):
	DefinitelyFull = 1
	VeryLikelyFull = 2
	ProbablyFull = 3
	Varying = 4
	ProbablyInverse = 5
	VeryLikelyInverse = 6
	DefinitelyInverse = 7
	MixedFirstName = 8
	MixedLastName = 9

class Population(Enum):
	Male = 1
	Mixed = 2
	Female = 3

class Aggression(Enum):
	Aggressive = 1
	Neutral = 2
	Conservative = 3

class Salutations(Enum):
	Formal = 0
	Informal = 1
	FirstLast = 2
	Slug = 3
	Blank = 4

class MiddleNameLogic(Enum):
	ParseLogic = 0
	HyphenatedLast = 1
	MiddleName = 2

class ResultCdDescOpt(Enum):
	ResultCodeDescriptionLong = 0
	ResultCodeDescriptionShort = 1

class mdName(object):
	def __init__(self):
		self.I = lib.mdNameCreate()

	def __del__(self):
		lib.mdNameDestroy(self.I)

	def SetPathToNameFiles(self, p1):
		lib.mdNameSetPathToNameFiles(self.I, p1.encode('utf-8'))

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdNameInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdNameGetInitializeErrorString(self.I).decode('utf-8')

	def SetLicenseString(self, p1):
		return lib.mdNameSetLicenseString(self.I, p1.encode('utf-8'))

	def GetBuildNumber(self):
		return lib.mdNameGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		return lib.mdNameGetDatabaseDate(self.I).decode('utf-8')

	def GetDatabaseExpirationDate(self):
		return lib.mdNameGetDatabaseExpirationDate(self.I).decode('utf-8')

	def GetLicenseExpirationDate(self):
		return lib.mdNameGetLicenseExpirationDate(self.I).decode('utf-8')

	def SetPrimaryNameHint(self, p1):
		return lib.mdNameSetPrimaryNameHint(self.I, NameHints(p1).value)

	def SetSecondaryNameHint(self, p1):
		return lib.mdNameSetSecondaryNameHint(self.I, NameHints(p1).value)

	def SetFirstNameSpellingCorrection(self, p1):
		return lib.mdNameSetFirstNameSpellingCorrection(self.I, p1)

	def SetMiddleNameLogic(self, p1):
		return lib.mdNameSetMiddleNameLogic(self.I, MiddleNameLogic(p1).value)

	def SetGenderPopulation(self, p1):
		return lib.mdNameSetGenderPopulation(self.I, Population(p1).value)

	def SetGenderAggression(self, p1):
		return lib.mdNameSetGenderAggression(self.I, Aggression(p1).value)

	def AddSalutation(self, p1):
		return lib.mdNameAddSalutation(self.I, Salutations(p1).value)

	def SetSalutationPrefix(self, p1):
		lib.mdNameSetSalutationPrefix(self.I, p1.encode('utf-8'))

	def SetSalutationSuffix(self, p1):
		lib.mdNameSetSalutationSuffix(self.I, p1.encode('utf-8'))

	def SetSalutationSlug(self, p1):
		lib.mdNameSetSalutationSlug(self.I, p1.encode('utf-8'))

	def ClearProperties(self):
		lib.mdNameClearProperties(self.I)

	def SetFullName(self, p1):
		lib.mdNameSetFullName(self.I, p1.encode('utf-8'))

	def SetPrefix(self, p1):
		lib.mdNameSetPrefix(self.I, p1.encode('utf-8'))

	def SetPrefix2(self, p1):
		lib.mdNameSetPrefix2(self.I, p1.encode('utf-8'))

	def SetFirstName(self, p1):
		lib.mdNameSetFirstName(self.I, p1.encode('utf-8'))

	def SetFirstName2(self, p1):
		lib.mdNameSetFirstName2(self.I, p1.encode('utf-8'))

	def SetMiddleName(self, p1):
		lib.mdNameSetMiddleName(self.I, p1.encode('utf-8'))

	def SetMiddleName2(self, p1):
		lib.mdNameSetMiddleName2(self.I, p1.encode('utf-8'))

	def SetSuffix(self, p1):
		lib.mdNameSetSuffix(self.I, p1.encode('utf-8'))

	def SetSuffix2(self, p1):
		lib.mdNameSetSuffix2(self.I, p1.encode('utf-8'))

	def SetLastName(self, p1):
		lib.mdNameSetLastName(self.I, p1.encode('utf-8'))

	def SetLastName2(self, p1):
		lib.mdNameSetLastName2(self.I, p1.encode('utf-8'))

	def Parse(self):
		return lib.mdNameParse(self.I)

	def Genderize(self):
		return lib.mdNameGenderize(self.I)

	def Salutate(self):
		return lib.mdNameSalutate(self.I)

	def GetStatusCode(self):
		return lib.mdNameGetStatusCode(self.I).decode('utf-8')

	def GetErrorCode(self):
		return lib.mdNameGetErrorCode(self.I).decode('utf-8')

	def GetChangeCode(self):
		return lib.mdNameGetChangeCode(self.I).decode('utf-8')

	def GetResults(self):
		return lib.mdNameGetResults(self.I).decode('utf-8')

	def GetResultCodeDescription(self, p1, opt):
		return lib.mdNameGetResultCodeDescription(self.I, p1.encode('utf-8'), ResultCdDescOpt(opt).value).decode('utf-8')

	def GetPrefix(self):
		return lib.mdNameGetPrefix(self.I).decode('utf-8')

	def GetPrefix2(self):
		return lib.mdNameGetPrefix2(self.I).decode('utf-8')

	def GetFirstName(self):
		return lib.mdNameGetFirstName(self.I).decode('utf-8')

	def GetFirstName2(self):
		return lib.mdNameGetFirstName2(self.I).decode('utf-8')

	def GetMiddleName(self):
		return lib.mdNameGetMiddleName(self.I).decode('utf-8')

	def GetMiddleName2(self):
		return lib.mdNameGetMiddleName2(self.I).decode('utf-8')

	def GetLastName(self):
		return lib.mdNameGetLastName(self.I).decode('utf-8')

	def GetLastName2(self):
		return lib.mdNameGetLastName2(self.I).decode('utf-8')

	def GetSuffix(self):
		return lib.mdNameGetSuffix(self.I).decode('utf-8')

	def GetSuffix2(self):
		return lib.mdNameGetSuffix2(self.I).decode('utf-8')

	def GetGender(self):
		return lib.mdNameGetGender(self.I).decode('utf-8')

	def GetGender2(self):
		return lib.mdNameGetGender2(self.I).decode('utf-8')

	def GetSalutation(self):
		return lib.mdNameGetSalutation(self.I).decode('utf-8')

	def StandardizeCompany(self, p1):
		return lib.mdNameStandardizeCompany(self.I, p1.encode('utf-8')).decode('utf-8')

	def SetReserved(self, p1, p2):
		lib.mdNameSetReserved(self.I, p1.encode('utf-8'), p2.encode('utf-8'))

	def GetReserved(self, p1):
		return lib.mdNameGetReserved(self.I, p1.encode('utf-8')).decode('utf-8')
