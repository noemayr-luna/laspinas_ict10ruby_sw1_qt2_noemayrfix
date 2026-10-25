from pyscript import document

def candidate_checker(e):
    club_members = ['azul ashengrotto' , 'jade leech' , 'floyd leech' , 'idia shroud' , 'ortho shroud']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_checker = candidate.lower() in club_members
    messages= (f'Sorry lawl {candidate}, your name isnt on the list.',f'GG {candidate}, you are now apart of the treasure hunt club!!')

    document.getElementById('result').innerHTML = messages[member_checker]
