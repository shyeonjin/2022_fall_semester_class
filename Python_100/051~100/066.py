def rules(total,rule):
    answer = []
    count=0
    for k in total:
        a = rule.index(rule[0])
        for i in k:
            if i in rule:
                if a > rule.index(i):
                    answer.append("불가능")
                    count=1
                a = rule.index(i)
        
        if count==0:
            answer.append("가능")
        count=0
    return answer

total =["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
rule = "ABD"
print(rules(total,rule))