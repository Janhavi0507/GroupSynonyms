class Synonyms:
  def Group(self, input:list[dict]):
    groups = []

    for i in input:
      if len(groups) == 0:
        groups.append(list([x for x in i.keys()] + [y for y in i.values()]))
        continue
      key, value = list(i.items())[0]
      for j in range(len(groups)):
        flag = False
        if (key in groups[j]) or (value in groups[j]):
          groups[j].append(key)
          groups[j].append(value)
          groups[j] = list(set(groups[j]))
          flag = True
          break
      if flag == False:
        groups.append([key, value])

    print(groups)

    
Synonyms().Group([ 
  {"Dg_set" : "Diesel_generator"}, 
  {"Organization" : "Organisation"}, 
  {"Group" : "Organization"}, 
  {"Orange" : "Kinnu"}, 
  {"Orange" : "narangi"} 
])
