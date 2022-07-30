def solution(id_list, report, k):
    id_dic = {}
    num_dic = {}
    for user in id_list:
        id_dic[user] = set([])
        num_dic[user] = 0
    for rep in report:
        user, reuser = rep.split()
        id_dic[reuser].add(user)
    for reuser, user in id_dic.items():
        if len(user) >= k:
            for u in user:
                num_dic[u] += 1
    # print(num_dic)
    answer = []
    for user in id_list:
        answer.append(num_dic[user])
    return answer
