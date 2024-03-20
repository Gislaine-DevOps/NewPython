# Writing the translation using functions
dict= {"Hello": "Bonjour", "Chair": "Chaise"}
def translation_en_fr(en_word: str, lang):
    if lang == "fr":
        if en_word in dict:
            return f"{en_word} into french is: {dict[en_word]}"
        else:
            return "this word is not in my dictionary"

a = translation_en_fr(en_word="Safou", lang="fr")
print(a)

a = translation_en_fr(en_word="Hello", lang="fr")
print(a)
