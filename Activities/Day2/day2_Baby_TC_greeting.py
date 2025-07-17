#declerating data
data="Luna42Kai3.14True#Knight"
Name=data[:4].upper()
add_nums=int(data[4:6])
multiply_num=float(data[9:13])*2
Reversed_title=data[-1:-7:-1]
print(f"Name:{Name}\n42+8={add_nums}\n3.14*2={multiply_num}\nReversed_title:{Reversed_title}")