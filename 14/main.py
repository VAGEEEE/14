from prime_checker import is_prime
num = 17
print(f"Число {num} є простим: {is_prime(num)}")
import os
os.makedirs('my_directory/sub_directory', exist_ok=True)
for i in range(1, 4):
    file_path = os.path.join('my_directory', f'file_{i}.txt')
    with open(file_path, 'w') as file:
        file.write(f"Це вміст файлу {i}")

print("Директорії та файли успішно створені.")

from my_package.string_utils import count_vowels
from my_package.number_utils import factorial
text = "Привіт, як справи?"
print(f"Кількість голосних у рядку: {count_vowels(text)}")
num = 5
print(f"Факторіал числа {num}: {factorial(num)}")
