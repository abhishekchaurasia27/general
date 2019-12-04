import json

input_file = input("Enter the full file path to find the domain count.\nfor ex: "
                    "C:\\Users\\<username>\\<actuall path>\\<filename>: ")
try:
    with open(input_file, errors='ignore') as f:
        data = f.readlines()
except IOError:
    print(f"Failed to read the input file {input_file}")
    exit(1)

try:
    domain_counter = {}
    for email in data:
        if all(ord(char) < 128 for char in email) and '@' in email:
            domain = email.rstrip().split('@')[1]
            if domain in domain_counter:
                domain_counter[domain] += 1
            else:
                domain_counter[domain] = 1

    unique_domain_count = 0
    for k, v in domain_counter.items():
        if v == 1:
            unique_domain_count += 1
except IndexError as ie:
    print(f"Index out of scope error occured: {ie}")
    exit(1)
except Exception as e:
    print(f"Some error occured: {e}")
    exit(1)

output_path = '\\'.join(input_file.split('\\')[:-1])
output_file = output_path + '\\output_' + input_file.split('\\').pop()
try:
    with open(output_file, 'w') as f:
        f.write(f'Total number of unique domains found in {input_file} are {unique_domain_count}')
        f.write('\n\nList of each domain with its count in the input file are:')
        f.write(json.dumps(domain_counter, indent=2, sort_keys=True))
except IOError:
    print(f"Failed to create the output file {output_file}")
    exit(1)

print(f'Output file created as:- {output_file}')