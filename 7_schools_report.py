"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json

infile = open('school_data.json', 'r')

schools = json.load(infile)

conference_schools = [372, 108, 107, 130]

for info in schools:
    women_grad = info['Graduation rate  women (DRVGR2020)']
    inst_name = info['instnm']
    conf_num = info['NCAA']['NAIA conference number football (IC2020)']

    if women_grad is None:
        women_grad_conv = float(0)
    else:
        women_grad_conv = float(women_grad)
    
    if women_grad_conv > 75 and conf_num in conference_schools:
        print()
        print(f"University {inst_name}")
        print(f"Graduation Rate for Women: {women_grad}%")
        print()





