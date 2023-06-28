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




