from datetime import datetime

currenttime = datetime.now()
print(f'yesterday: {currenttime.day - 1}th' f'\ntoday: {currenttime.day}th' f'\ntomorrow.: {currenttime.day + 1}th')


