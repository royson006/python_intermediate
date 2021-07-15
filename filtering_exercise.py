#Make the list all_python_devs and all_platzo workers with map and filter
#Make the list old_people and adults with list comprehensions

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_platzi_workers=list(filter(lambda dev: dev["organization"]=="Platzi",DATA))
    all_platzi_workers=list(map(lambda dev: dev["name"],all_platzi_workers))
    print("Platzi workers: ",all_platzi_workers)

    all_python_devs= list(filter(lambda dev:dev["language"]=="python",DATA))
    all_python_devs= list(map(lambda dev:dev["name"],DATA))
    print("Python developers: ",all_python_devs)

    adults=[ adult["name"] for adult in DATA if adult["age"]>=18]
    print("Los adultos son",adults)

    ##To add dictionary to another with list comprehensions **object ,**{new objecte, key--value}
    old_people= [{**adult, **{"old": adult["age"] > 70}} for adult in DATA]
    print("Nueva caracteristica en dic",old_people)

if(__name__=="__main__"):
    run()