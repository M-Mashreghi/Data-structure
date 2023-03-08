pirahan = {
  "kind": "pirahan",
  "color": [],
  "type": ['sadeh'],
  "h_price": 700000,
  "l_price": 200000}
kapshen = {
  "kind": "kapshen",
  "color": ['meshki'],
  "type": ['charm'],
  "h_price": 2000000,
  "l_price": 0}
shalvar = {
  "kind": "shalvar",
  "color": ['sabz','khakestari'],
  "type": ['katan','jean'],
  "h_price": 1000000,
  "l_price": 400000}
joorab = {
  "kind": "joorab",
  "color": ['sefid'],
  "type": ['nakhi'],
  "h_price": 0,
  "l_price": 0}

Bought_pirahan = 0
Bought_kapshen = 0
Bought_shalvar = 0
Bought_joorab = 0

num_of_contact = int(input())
for i in range(num_of_contact):
    line = input().split()
    if line[0] == 'pirahan':
        if line[3] == pirahan["type"][0]:
            if pirahan["l_price"] <  int(line[2]) < pirahan["h_price"]:
                    Bought_pirahan += 1

    if line[0] == 'kapshen':
            if kapshen["color"][0] == line[1]:
              if line[3] == kapshen["type"][0]:
                      if int(line[2]) < kapshen["h_price"]:
                          Bought_kapshen += 1

    if line[0] == 'shalvar':
         for i in shalvar["color"]:
            if i == line[1]:
                for j in shalvar["type"]:
                  if line[3] == j:
                      if shalvar["l_price"]<int(line[2])<shalvar["h_price"]:
                          Bought_shalvar += 1
    if line[0] == 'joorab':
      if  line[1] == joorab["color"][0]:
          if line[3] == joorab["type"][0]:
             Bought_joorab += 1
print(Bought_pirahan)
print(Bought_kapshen)
print(Bought_shalvar)
print(Bought_joorab)
