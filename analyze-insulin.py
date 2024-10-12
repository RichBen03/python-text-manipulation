import re
with open('preproinsulin.txt', 'r') as file:
    content = file.read()

new_content = re.sub(r'ORIGIN\s*\n','', content)
new_content = re.sub(r'[0-9]','', new_content)
new_content = re.sub(r'//','', new_content)
new_content = re.sub(r'\s+','', new_content)

total_length = len(new_content)
print(f"The cleaned sequence is: {new_content}")
print(f"The length of the cleaned sequence is: {total_length}")


with open('cleaned-preproinsulin.txt','w') as new_file:
    new_file.write(new_content)
print("File has been written to a new file")