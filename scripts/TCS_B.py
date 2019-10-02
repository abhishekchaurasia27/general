distance1 = int(input())
fuel_cost1 = int(input())
showroom_price1 = int(input())
avg_monthly_rum1 = int(input())
maintenance1 = int(input())
horizon1 = int(input())
distance2 = int(input())
fuel_cost2 = int(input())
showroom_price2 = int(input())
avg_monthly_rum2 = int(input())
maintenance2 = int(input())
horizon2 = int(input())

run1 = avg_monthly_rum1 * horizon1
fuel_req1 = run1 / distance1
fuel_cost1 = fuel_req1 * fuel_cost1
petrol_cost = showroom_price1 + maintenance1 + fuel_cost1

run2 = avg_monthly_rum2 * horizon2
fuel_req2 = run2 / distance2
fuel_cost2 = fuel_req2 * fuel_cost2
diesel_cost = showroom_price2 + maintenance2 + fuel_cost2


if petrol_cost > diesel_cost:
    print("diesel")
else:
    print("petrol")


