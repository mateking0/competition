with open('./input.txt', 'r') as f:
  input = f.read()
def remove_characters(text):
    allowed_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    cleaned_text = ''.join(char for char in text if char in allowed_chars)
    return cleaned_text

input = input.strip()
input = input.lower()
list = input.split('\n')
for x in list:
    c = True
    x = remove_characters(x)
    a = set(x)
    for y in range(int(len(x)/2)):
        if x[y] == x[len(x)-y-1]:
            continue
        else:
            print("NO, -1")
            c = False
            break
    if c:
        print(f"YES, {len(a)}")
