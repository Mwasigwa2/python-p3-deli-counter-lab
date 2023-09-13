def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    else:
        line_status = "The line is currently:"
        for i, customer in enumerate(katz_deli, start=1):
            line_status += f" {i}. {customer}"
        return line_status

def take_a_number(katz_deli, customer_name):
    katz_deli.append(customer_name)
    position = len(katz_deli)
    return f"Welcome, {customer_name}. You are number {position} in line."

def now_serving(katz_deli):
    if not katz_deli:
        return "There is nobody waiting to be served!"
    else:
        serving_customer = katz_deli.pop(0)
        return f"Currently serving {serving_customer}."
