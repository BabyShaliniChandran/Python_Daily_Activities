#solution 1
invited={'Alice','Bob','Charlies'}
arrived={'Alice','Charlies','Diana'}
if invited ^ arrived:
	print("Unexpected guests arrived",*(invited ^ arrived))

if invited not in arrived:
	print("Unexpected guests arrived",*(invited ^ arrived))

if invited not in arrived:
	print("Unexpected guests arrived",*(arrived-invited))