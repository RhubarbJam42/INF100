#funksjon som bestemmer hvem som er eldst
def hvem_eldst(person_one_name, person_one_age, person_two_name, person_two_age):
    if person_one_age > person_two_age:
        return f'{person_one_name} er {person_one_age} år og eldst.'
    elif person_one_age < person_two_age:
        return f'{person_two_name} er {person_two_age} år og eldst.'
