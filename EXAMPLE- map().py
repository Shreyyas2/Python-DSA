def get_name(person):
    return person['name']
person=[
    {'name':'shreyas','age':20},
    {'name':'krishna','age':20}]
name_got=list(map(get_name,person))
print(name_got)
