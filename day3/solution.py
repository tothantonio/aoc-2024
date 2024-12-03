import re

def extract_and_mul(file):
    with open(file, 'r') as f:
        data = f.read()
    
    pattern = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')

    total = 0
    enabled = True
    pos = 0

    while pos < len(data):
        do_match = do_pattern.search(data, pos)
        dont_match = dont_pattern.search(data, pos)
        mul_match = pattern.search(data, pos)

        next_match = min(
            (m for m in [do_match, dont_match, mul_match] if m),
            key = lambda m: m.start(),
            default = None
        )

        if not next_match:
            break
        
        if next_match == do_match:
            enabled = True
            pos = do_match.end()
        elif next_match == dont_match:
            enabled = False
            pos = dont_match.end()
        elif next_match == mul_match:
            if enabled:
                x, y = map(int, mul_match.groups())
                total += x * y
            pos = mul_match.end()
    
    return total
    

file = 'day3/input.txt'
print(extract_and_mul(file))
