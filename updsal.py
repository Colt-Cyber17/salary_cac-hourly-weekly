def num(txt):
    txt_clean = txt.replace(',','')
    try:
        return int(txt_clean)
    except ValueError:
        return float(txt_clean)
def n():
    new = '\n'
    print(new)
n()
print('Welcome to the caculator\n[a]  salary\n[b]  hourly\n[c]  weekly\n[q]  quit')
while True:
    n()
    choice_1 = input('Enter your choice: ').lower().strip()
    if choice_1 == 'a':
        h_rate = num(input('Enter your hourly rate: '))
        wk_h = num(input('Enter your hours per week: '))
        sal = h_rate * wk_h
        sal_total = sal * 52
        print(f'salary = {sal_total:,.2f} per year')

    elif choice_1 == 'b':
        w_pay = num(input('Enter your weekly pay: '))
        h_wk = num(input('Enter your hours worked per week: '))
        total_hour = w_pay / h_wk
        print(f'hourly = {total_hour:,.2f} an hour')
        
    elif choice_1 == 'c':
        h_wk = num(input('Enter your hours worked per week: '))
        h_rate2 = num(input('Enter your per hour rate: '))
        wk_total = h_wk * h_rate2
        
        has_overtime = input('Did you work overtime? (y,n) ').strip()
        if has_overtime == 'y':
            over_r = num(input('Enter your overtime rate: '))
            over_h = num(input('Enter your overtime hours: '))
            over_r1 = over_r * h_rate2 * over_h
            over_total = over_r1 + wk_total
            print(f'overtime pay = {over_r1:,.2f}\ntotal = {over_total:,.2f}')
        
        elif has_overtime == 'n':
            print(f'weekly pay = {wk_total:,.2f}')
            break
        
    if choice_1 == 'q':
        break
        



        
    