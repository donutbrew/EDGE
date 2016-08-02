import sys
import uc
import die
import fasta

FileName = sys.argv[1]

def GetSampleId(Label):
	SampleID = Label.split()[0].split('_')[0] 
	return SampleID

def OnRec():
	global OTUs, Samples, OTUTable
	if uc.Type != 'H':
		return

	OTUId = uc.TargetLabel
	if OTUId not in OTUIds:
		OTUIds.append(OTUId)
		OTUTable[OTUId] = {}

	SampleId = GetSampleId(uc.QueryLabel)
	if SampleId not in SampleIds:
		SampleIds.append(SampleId)

	N = fasta.GetSizeFromLabel(uc.QueryLabel, 1)
	try:
		OTUTable[OTUId][SampleId] += N
	except:
		OTUTable[OTUId][SampleId] = N

OTUIds = []
SampleIds = []
OTUTable = {}

uc.ReadRecs(FileName, OnRec)

s = "OTUId"
for SampleId in SampleIds:
	s += "\t" + SampleId
print s

for OTUId in OTUIds:
	s = OTUId
	for SampleId in SampleIds:
		try:
			n = OTUTable[OTUId][SampleId]
		except:
			n = 0
		s += "\t" + str(n)
	print s