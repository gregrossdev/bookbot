with open("./books/frankenstein.txt") as f:
  file_contents = f.read() 
  words = file_contents.split()
  # print(len(words))
  
  text = ''.join(words).lower()
  character_counts = {}

  for char in text:
    if char.isalpha():
      character_counts[char] = character_counts.get(char, 0) + 1

  # print(character_counts)

  character_list = list(character_counts.items())
  character_list.sort()

  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{len(words)} words found in the document")
  print("")
  for char, count in character_list:
      print(f"The {char} character was found {count} times")
  print("--- End report ---")
  

