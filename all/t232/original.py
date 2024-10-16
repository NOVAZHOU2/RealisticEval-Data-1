import re

# this function was generated by chatgpt also has a copy in /javascript
def convert_time_hms_string_to_ms(s):
  regex = r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?'
  match = re.search(regex, s)

  if not match:
    print(f'remindme.py: Cannot convert hms string "{s}" to ms!')

  hours = int(match.group(1)) if match.group(1) else 0
  minutes = int(match.group(2)) if match.group(2) else 0
  seconds = int(match.group(3)) if match.group(3) else 0

  ms = ((hours * 60 + minutes) * 60 + seconds) * 1000

  if ms > 86400000:
    print('remindme.py: Cannot exceed a total time greater than one day.')

  return ms