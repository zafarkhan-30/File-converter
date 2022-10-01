a = ['(a)', 'Sol. ', '(c)', 'Sol.', 'o-dihydroxy benzene or catechol.', '(b)', 
'Sol. Glycols are dihydric alcohols (having two hydroxyl groups). Ethylene glycol is the first member of this series.', ' ', '(c)', 
'Sol. Hydration of alkenes', 'Fermentation of sugars:', '\t', '(c)', 'Sol. .', '(b)', 'Sol. ', '(a)', 'Sol. ', '(b)', 'Sol. ', '(b)', 'Sol. ',
'If we take moistthen alcohol is formed ', '(a)', 'Sol. ', '(b)', 'Sol.andattacks only carbonyl group and reduce it into alcohol group. They do not attack on double bond.', 
'(a)', 'Sol. ', '(c)', 'Sol. ', '(a)', 'Sol. ', 'Since on oxidation same no. of carbon atoms are obtained in as therefore alcohol is primary ', '(c)', 'Sol.', 'Increasing acidic character',
'(b)', 'Sol. ', '(c)', 'Sol. ', ' reacts immediately ', ' reacts after 5 min.', ' reacts only on heating.', '(a)', 'Sol. ', '(b)', 'Sol. Tertiary alcohol readily reacts with halogen acid',
'Presence of 3 alkyl group increases electron density on carbon atom. Hencegroup is easily removed. After the removal ofgroupcarbonium ion is formed which is most stable', '(c)', 
'Sol. o-Nitrophenol has intramolecular H-bonding.', '(c)', 'Sol.', 'or ', '(a)', 'Sol. Secondary alcohol on dehydrogenation gives acetone ', '(c)', 'Sol. ',
'94 grams of phenol reacts with 480 gms. of .', '2 gm. of phenol—gms.', '(b)', 'Sol. A mixture of glyceryl trinitrate and glyceryl dinitrate when absorbed on kieselgurh is called dynamite.',
 '(c)', 'Sol. Groundnut oil.']


# for i in a:
#     print(i)

x = []
y = []
for i in a:
    if "(a)" in i:
        x.append(i)
    elif "(b)" in i:
        x.append(i)
    elif "(c)" in i:
        x.append(i)
    elif "(d)" in i:
        x.append(i)
    else:
        y.append(i)
# print(y)

for i in y:
    if " " in i:
        x=i.strip()
print(y)

# for i in y:
