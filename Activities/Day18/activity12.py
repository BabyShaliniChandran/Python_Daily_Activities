raw_guests=[" alice ","Bob","ALICE"," bob "," Eve ","eve","  ANAND"]

raw_guests=[(x.strip()).title() for x in raw_guests]
len_string=[len(x) for x in raw_guests]
print({k:v for k,v in zip(raw_guests,len_string)})
