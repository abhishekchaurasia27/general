I used ‘@’ as a separator to find the domain name.
I read entire file by ignoring any errors coming due to any encoding type and I later filtered this by checking each character in that string is having ascii less than 128.
I created a dictionary which contains domain name and the number of times it is occurring in the input file as key and value respectively.
Finally, I iterated over that dictionary to count all the domains which occurred exactly once so as to find the count of unique domains. 


Output of this domain_counter.py after running it with all the four file attached in,

Total number of unique domains found in easylist.txt are 160
Total number of unique domains found in mediumlist.txt are 179
Total number of unique domains found in hardlist.txt are 339
Total number of unique domains found in hardestlist.txt are 528
