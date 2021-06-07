word = str(input("Podaj słowo: ").lower())

if word[::-1] == word:
    print("Słowo %s to palindrom!" % word)
else:
    print("Słowo %s to nie palindrom!" % word)

# Udoskonalona wersja

word = str(input("Podaj słowo: ").lower())

print("Słowo %s to palindrom!" % word) if word[::-1] == word[::] else print("Słowo %s to nie palindrom!" % word)
