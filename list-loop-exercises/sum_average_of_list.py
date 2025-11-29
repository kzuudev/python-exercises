

def sum_and_average(numbers):

   total_sum = 0
   total_length = len(numbers)

   for number in numbers:
       total_sum += number # 0 + 2, 2 + 4, 6 + 6, 12 + 8 = 20

   average_list = total_sum / total_length
   print(total_sum)
   print(average_list)

sum_and_average([2,4,6,8])