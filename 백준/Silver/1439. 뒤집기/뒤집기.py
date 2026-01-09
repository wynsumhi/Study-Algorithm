code = input().strip()

zero_groups = 0
one_groups = 0

if code[0] == '0':
    zero_groups = 1
else:
    one_groups = 1

for i in range(1, len(code)):
   if code[i] != code[i-1]:
      if code[i] == '0':
         zero_groups += 1
      else:
         one_groups += 1

print(min(zero_groups, one_groups))
