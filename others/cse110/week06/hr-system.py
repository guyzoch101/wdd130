with open('week06/hr_system.txt') as system:
    for list in system:
        parts = list.split()
        
        name = parts[0].strip()
        id = parts[1].strip()
        title = parts[2].strip()
        salary = float(parts[3].strip())
        
        bi_weekly_salary = salary / 24
        
        if title.lower() == 'engineer':
            bi_weekly_salary += 1000
        
        print(f'{name} (ID: {id}), {title} - ${bi_weekly_salary:.2f}')