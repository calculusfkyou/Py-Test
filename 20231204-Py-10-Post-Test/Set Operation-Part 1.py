# (lambda a,b: print(' '.join(list(map(str, (sorted(a&b))))) + '\n' + ' '.join(list(map(str, (sorted(a|b)))))))(set(map(int,input().split())), set(map(int,input().split())))

a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(*(sorted(a & b))) # 求交集
print(*(sorted(a | b))) # 求聯集

set_a = set(map(int, input().split())) # Input two sets of values as space-separated strings and convert them to sets of integers
set_b = set(map(int, input().split()))
intersection_result = ' '.join(list(map(str, sorted(set_a & set_b)))) # Find the intersection and union of the two sets, convert to sorted lists, and join as strings
union_result = ' '.join(list(map(str, sorted(set_a | set_b))))
print(intersection_result + '\n' + union_result) # Print the results