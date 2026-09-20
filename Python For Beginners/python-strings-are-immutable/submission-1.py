def remove_fourth_character(word: str) -> str:
     removed_fourth = word[:3] + word[4:]
     
     return removed_fourth


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
