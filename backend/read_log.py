
encoding = 'utf-16'
try:
    with open('registry_log.txt', encoding=encoding) as f:
        content = f.read()
except:
    try:
        with open('registry_log.txt', encoding='utf-8') as f:
            content = f.read()
    except:
        print("Could not read file with utf-16 or utf-8")
        exit(1)

lines = content.splitlines()
for line in lines:
    if 'detected' in line or 'Error' in line or 'Processing' in line:
        print(line)
