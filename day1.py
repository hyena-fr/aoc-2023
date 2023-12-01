#Part 1
with open('input.txt', 'r') as file:
    total_sum = 0
    for line in file:
        extracted_nums = ''.join(filter(str.isdigit, line))
        if extracted_nums:
            total_sum += int(extracted_nums[0]) + int(extracted_nums[-1])
    print('Part 1:', total_sum)

#Part 2
num_mapping = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

with open('input.txt', 'r') as file:
    total_sum = 0
    for line in file:
        extracted_nums = ''
        current_word = ''
        for char in line:
            if char.isalpha():
                current_word += char
                if current_word in num_mapping:
                    extracted_nums += num_mapping[current_word]
                    current_word = ''
            else:
                current_word = ''
        if extracted_nums:
            total_sum += int(extracted_nums[0]) + int(extracted_nums[-1])
    print('Part 2:', total_sum)
