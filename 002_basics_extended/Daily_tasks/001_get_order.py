# def get_order(order: str) -> str:
#     menu = {
#         0: "Burger",
#         1: "Fries",
#         2: "Chicken",
#         3: "Pizza",
#         4: "Sandwich",
#         5: "Onionrings",
#         6: "Milkshake",
#         7: "Coke"
#     }
#
#     counted_order = {}
#     for key in menu:
#         current_count_dish = order.count(menu.get(key).lower())
#         if current_count_dish > 0:
#             counted_order.update({menu.get(key): current_count_dish})
#
#     result = []
#     for item in counted_order:
#         for i in range(counted_order[item]):
#             result.append(item)
#
#     return " ".join(result)
#
# get_order("burgersandwich")
# get_order("sandwichcokefriessandwichpizzaburger")

# def get_order(order: str) -> str:
#     menu = {
#         0: "Burger",
#         1: "Fries",
#         2: "Chicken",
#         3: "Pizza",
#         4: "Sandwich",
#         5: "Onionrings",
#         6: "Milkshake",
#         7: "Coke"
#     }
#
#     result = []
#     for key in menu:
#         current_count_dish = order.count(menu.get(key).lower())
#         if current_count_dish > 0:
#             for _ in range(current_count_dish):
#                 result.append(menu.get(key))
#
#     print(result)
#
#     return " ".join(result)
#
# get_order("burgersandwich")
# get_order("sandwichcokefriessandwichpizzaburger")

# ============================================================================
# def fix_string_case(word: str) -> str:
#     upper_case_chars_count = sum(1 for char in word if char.isupper())
#     lower_case_chars_count = sum(1 for char in word if char.islower())
#     return word.upper() if upper_case_chars_count > lower_case_chars_count else word.lower()
#
# print(fix_string_case("coDe"))
# print(fix_string_case("cODE"))
# print(fix_string_case("coDE"))
# print(fix_string_case("THAT'S fine, I STUDY here!"))

# ============================================================================
# def square_color(string: str, rank: int) -> str:
#     board = {}
#     isWhite = True
#     for i in range(8):
#         for j in range(8):
#             board.update({f"{chr(97 + i)}{abs(j - 8)}": isWhite})
#             isWhite = False if isWhite else True
#         isWhite = True if not isWhite else False
#
#     return "White" if board.get(f"{string}{rank}") else "Black"

# def square_color(string: str, rank: int) -> str:
#     isWhite = True
#     for i in range(8):
#         for j in range(8):
#             if f"{chr(97 + i)}{abs(j - 8)}" == string+str(rank):
#                 return "White" if isWhite else "Black"
#             isWhite = False if isWhite else True
#         isWhite = True if not isWhite else False

# print(square_color("a", 8))
# print(square_color("a", 1))
# print(square_color("b", 8))
# print(square_color("b", 1))
#
# print()
#
# print(square_color("d", 8))
# print(square_color("d", 1))
# print(square_color("e", 8))
# print(square_color("e", 1))
#
# print()
#
# print(square_color("c", 5))
# print(square_color("f", 5))

# ============================================================================
# def tribonacci(signature: list, number: int) -> list:
#     if number == 0:
#         return []
#
#     if number == 1:
#         return [signature[0]]
#
#     while len(signature) < number:
#         signature.append(sum(signature[-3:]))
#
#     print(signature)

# tribonacci([1, 1, 1], 10)  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
# tribonacci([0, 0, 1], 10)  # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
# tribonacci([0, 1, 1], 10)  # [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
# tribonacci([1, 0, 0], 10)  # [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
# tribonacci([0, 0, 0], 10)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# tribonacci([1, 2, 3], 10)  # [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
# tribonacci([3, 2, 1], 10)  # [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
# tribonacci([1, 1, 1], 1)  # [1]
# tribonacci([300, 200, 100], 0)  # []
# tribonacci([0.5, 0.5, 0.5], 30)  # [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5 ....]

# ============================================================================
# def partlist(lst: list) -> list:
#     result = []
#     for i in range(1, len(lst)):
#         result.append((" ".join(lst[0:i]), " ".join(lst[i:])))
#     return result

# def partlist(lst: list) -> list:
#     return [(" ".join(lst[0:i]), " ".join(lst[i:])) for i in range(1, len(lst))]

# print(partlist(["I", "wish", "I", "hadn't"]))

# ============================================================================
# def two_sum(nums: list, target: int) -> list:
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([3, 2, 4], 6))
# print(two_sum([3, 2, 3], 6))
# print(two_sum([9, 8, 8], 16))

# ============================================================================
# def jewels_and_stones(jewels: str, stones: str) -> int:
#     return sum([stones.count(char) for char in list(jewels)])
#
# jewels_and_stones("aA", "aAAbbbb")
# jewels_and_stones("z", "ZZ")
# jewels_and_stones("abcde", "abcd")

# ============================================================================ List Comparator
# def list_comparator(first: list, second: list) -> int:
#     count = 0
#     for item in first:
#         if item in second:
#             count += 1
#     return count

# ============================================================================ Is Leap year
# def is_leap_year(year: int) -> bool:
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# ============================================================================ Get Section id
# def get_section_id(scroll: int, sizes: list) -> int:
#     index = 0
#     for size in sizes:
#         scroll -= size
#         if scroll < 0:
#             return index
#         else:
#             index += 1
#     return -1

# print(get_section_id(300, [300, 200, 400]))
# print(get_section_id(1600, [300, 200, 400, 600, 100]))
# print(get_section_id(500, [300, 200, 400, 600, 100]))

# # ============================================================================ Convert to title
# def convert_to_title(num: int) -> str:
#     div = num // 26
#     mod = num % 26
#     # print(div)  # first letter
#     # print(mod)  # second letter
#     #
#     # # print(f"{chr(65)} = {ord('A')}")
#     # # print(f"{chr(90)} = {ord('Z')}")
#     #
#     # print(f"{chr(div + 64)} = {ord(chr(div + 64))}")
#     # print(f"{chr(mod + 64)} = {ord(chr(mod + 64))}")
#     div = num // 26
#     mod = num % 26
#     if div > 0 and mod > 0:
#         return f"{chr(div + 64)}{chr(mod + 64)}"
#     if div == 0 and mod > 0:
#         return chr(mod + 64)
#     if div > 0 and mod == 0:
#         return f"{chr(div - 1 + 64)}{chr(mod + 64 + 26)}" if div != 1 else chr(mod + 64 + 26)
#
#     # return chr(mod + 64) if div == 0 else f"{chr(div + 64)}{chr(mod + 64)}"
#
# print(convert_to_title(26))  # Z
# print("========================")
# print(convert_to_title(52))   # AZ
# print("========================")
# print(convert_to_title(78))   # BZ
# print("========================")
# print(convert_to_title(104))   # CZ
# print("========================")
# print(convert_to_title(28))  # AB
# print("========================")
# print(convert_to_title(701))  # ZY
# print("========================")
# print(convert_to_title(1))  # A
# print("========================")

# # ============================================================================ Rotate List IN PROCESS!!!!!
# from itertools import cycle
# def rotate_list(nums: list, steps: int) -> list:
#     len_nums = len(nums) + 1
#     count = 0
#     res = []
#     for num in cycle(nums):
#         if len_nums + steps == count:
#             break
#         res.append(num)
#         count += 1
#     return res[steps+1:]
#
#
# print(rotate_list([1, 2, 3, 4, 5, 6, 7], 3))
# print(rotate_list([-1, -100, 3, 99], 2))

# # ============================================================================ Count 9
# def count_nines(number: int) -> int:
#     s = ""
#     for i in range(1, number + 1):
#         s += str(i)
#     return s.count("9")
# print(count_nines(1000))

# # ============================================================================ Middle Char
# def middle_character(word: str) -> str:
#     len_word = len(word)
#     if len_word == 1:
#         return word
#     if len_word == 0:
#         return ""
#     middle = len_word // 2
#     return word[middle - 1] + word[middle] if len_word % 2 == 0 else word[middle]

# # ============================================================================ Multiple 3 5
# def multiples_3_5(number: int) -> int:
#     s = 0
#     for i in range(number):
#         if i % 15 == 0:
#             s += i
#             continue
#         elif i % 3 == 0 or i % 5 == 0:
#             s += i
#     return s
# print(multiples_3_5(10))

# # ============================================================================ Credit card issue checking
# def credit_card_issuer_checking(number: int) -> str:
#     str_num = str(number)
#     size = len(str_num)
#     if size < 13:
#         return "Unknown"
#
#     short_num = int(str(number)[:4])
#     first_num = int(short_num // 1000)
#
#     if first_num not in range(3, 6 + 1):
#         return "Unknown"
#
#     if (short_num // 100 == 34 or short_num // 100 == 37) and size == 15:
#         return "AMEX"
#     elif short_num == 6011 and size == 16:
#         return "Discover"
#     elif short_num // 100 in range(51, 55 + 1):
#         return "Mastercard"
#     elif first_num == 4 and (size == 13 or size == 16):
#         return "VISA"
#
#     return "Unknown"





