def custom_dict(queries, values):
    ans = []

    d_ = {}

    for op, v in zip(queries, values):
        if op == 'Add':
            d_[v[0]] = v[1]

        elif op == 'Add_to_vals':
            for key in d_.keys():
                d_[key] += v[0]

        elif op == 'Add_to_keys':
            new_dict = {}
            for k, vl in d_.items():
                new_dict[k + v[0]] = vl
            d_ = new_dict

        elif op == 'Return':
            ans.append(d_[v[0]])

    return ans


print(custom_dict(["Add", "Add_to_vals", "Return", "Add", "Add_to_keys", "Add_to_vals", "Return"],
                  [[1, 2], [2], [1], [2, 3], [1], [-1], [3]]))
