with open('data.json', 'rb') as f:
    content = f.read()

# Try to decode ignoring BOM
if content.startswith(b'\xef\xbb\xbf'):
    content = content[3:]  # strip UTF-8 BOM
elif content.startswith(b'\xff\xfe') or content.startswith(b'\xfe\xff'):
    # UTF-16 BOM, convert to UTF-8
    content = content.decode('utf-16').encode('utf-8')

with open('data_fixed.json', 'wb') as f:
    f.write(content)
