def getMaxEqualIndices(inv1, inv2):
    n = len(inv1)
    max_surplus = 0
    count_surplus = [0] * (10001)  # Since surplus can be up to 10^4
    total_deficit_units = 0
    count = 0  # Number of indices where inv1[i] <= inv2[i]

    for i in range(n):
        if inv1[i] < inv2[i]:
            total_deficit_units += inv2[i] - inv1[i]
            count += 1
        elif inv1[i] > inv2[i]:
            surplus = inv1[i] - inv2[i]
            count_surplus[surplus] += 1
            if surplus > max_surplus:
                max_surplus = surplus
        else:
            # inv1[i] == inv2[i]
            count += 1

    # Process surplus units
    for surplus_units in range(1, max_surplus + 1):
        while count_surplus[surplus_units] > 0:
            if total_deficit_units >= surplus_units:
                total_deficit_units -= surplus_units
                count += 1
                count_surplus[surplus_units] -= 1
            else:
                # Cannot use more surplus units
                return count
    return count


inv1=[3,2,1]
inv2=[2,1,4]
print(getMaxEqualIndices(inv1, inv2))
