x_list=['apple','orange','banana']
s='\n'.join(x_list)

with open('test3.txt','w') as f:
  f.write(s)