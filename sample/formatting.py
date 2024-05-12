name = 'Vishal'
balance = 12.4567

print(name +' has $' + str(balance))

print(name+ " has $",balance)

print("%s has $%.3f" %(name,balance))

print("%10s has %10.2f" %(name,balance))

print("%-10s has $ %-10f" %(name, balance))


print("{:10} has ${:15.3f}" .format(name,balance))


print("{:10} has ${:^15.3f}" .format(name,balance))


print("{:@^10} has ${:0^15.3f}" .format(name,balance))



print(f'{name:>} has dollar ${balance:>.1f}')