data=[[1,2,None],[],[3,'',4],[0,5,5],[None,6]]

cleaned_data={y for x in data for y in x if y}
print([*cleaned_data])