def camelcase_to_snakecase(sen):
    new_sen = ""
    i=0
    while i<len(sen):
        if sen[i] =="_":
            new_sen = sen[i+1].upper()
            i+=2
        else:
            new_sen +=sen[i]
            i+=1
    return new_sen

sc1 = camelcase_to_snakecase("hello")
sc2 = camelcase_to_snakecase("helloWorld")
sc3 = camelcase_to_snakecase("camelCaseToSnakeCase")
print(sc1)
print(sc2)
print(sc3)