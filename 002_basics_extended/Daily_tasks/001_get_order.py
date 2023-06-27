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

# get_order("burgersandwich")
# get_order("sandwichcokefriessandwichpizzaburger")

# ============================================================================
# def fix_string_case(word: str) -> str:
#     upper_case_chars_count = sum(1 for char in word if char.isupper())
#     return word.upper() if len(word) / 2 < upper_case_chars_count else word.lower()

# print(fix_string_case("coDe"))
# print(fix_string_case("cODE"))
# print(fix_string_case("coDE"))

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
#
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
