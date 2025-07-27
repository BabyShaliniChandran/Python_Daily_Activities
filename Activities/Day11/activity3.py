guset_list_email={"Alice","bob","charlies"}
guset_list_Phone={"bob","charlies"}
guset_blocked_list={"Alice","Tom","charlies"}

#invited people (email & phone)
guest_inivited=(guset_list_email.intersection(guset_list_Phone))-guset_blocked_list

#guest in only block lsit
only_block_list=guset_blocked_list-(guset_list_email.union(guset_list_Phone))

#output
guest_list=guest_inivited.union(only_block_list)

print(guest_list)


print(((guset_list_email.intersection(guset_list_Phone))-guset_blocked_list).union(guset_blocked_list-(guset_list_email.union(guset_list_Phone))))

