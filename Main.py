from collections import Counter
from bs4 import BeautifulSoup

# Load the HTML file
with open('file.html') as f:
    html_doc = f.read()

# Parse the HTML file using BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# Find all <li> tags with class="ball pastNum1" and get the mode
num1_list = soup.find_all('li', {'class': 'ball pastNum1'})
num1_modes = [num.get_text() for num in num1_list]
num1_modes_count = Counter(num1_modes).most_common()
num1_modes_perc = [(mode[0], round(mode[1] / len(num1_modes) * 100, 2)) for mode in num1_modes_count]

# Find all <li> tags with class="ball pastNum2" and get the mode
num2_list = soup.find_all('li', {'class': 'ball pastNum2'})
num2_modes = [num.get_text() for num in num2_list]
num2_modes_count = Counter(num2_modes).most_common()
num2_modes_perc = [(mode[0], round(mode[1] / len(num2_modes) * 100, 2)) for mode in num2_modes_count]

# Find all <li> tags with class="ball pastNum3" and get the mode
num3_list = soup.find_all('li', {'class': 'ball pastNum3'})
num3_modes = [num.get_text() for num in num3_list]
num3_modes_count = Counter(num3_modes).most_common()
num3_modes_perc = [(mode[0], round(mode[1] / len(num3_modes) * 100, 2)) for mode in num3_modes_count]

# Find all <li> tags with class="ball pastNum4" and get the mode
num4_list = soup.find_all('li', {'class': 'ball pastNum4'})
num4_modes = [num.get_text() for num in num4_list]
num4_modes_count = Counter(num4_modes).most_common()
num4_modes_perc = [(mode[0], round(mode[1] / len(num4_modes) * 100, 2)) for mode in num4_modes_count]

# Find all <li> tags with class="ball pastNum5" and get the mode
num5_list = soup.find_all('li', {'class': 'ball pastNum5'})
num5_modes = [num.get_text() for num in num5_list]
num5_modes_count = Counter(num5_modes).most_common()
num5_modes_perc = [(mode[0], round(mode[1] / len(num5_modes) * 100, 2)) for mode in num5_modes_count]

# Find all <li> tags with class="ball yellowBall pastNumMB" and get the mode
mb_list = soup.find_all('li', {'class': 'ball yellowBall pastNumMB'})
mb_modes = [num.get_text() for num in mb_list]
mb_modes_count = Counter(mb_modes).most_common()
mb_modes_perc = [(mode[0], round(mode[1] / len(mb_modes) * 100, 2)) for mode in mb_modes_count]

# Print the modes and their percentages
print("Past Num 1 Modes and Percentages: ", num1_modes_perc)
print("Past Num 2 Modes and Percentages: ", num2_modes_perc)
print("Past Num 3 Modes and Percentages: ", num3_modes_perc)
print("Past Num 4 Modes and Percentages: ", num4_modes_perc)
print("Past Num 5 Modes and Percentages: ", num5_modes_perc)
print("Past Num mb Modes and Percentages: ", mb_modes_perc)

