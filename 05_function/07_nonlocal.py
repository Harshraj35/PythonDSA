def update_order():
    chai_type = 'milk tea'
    def kitchen():
        nonlocal chai_type
        chai_type = 'green tea'
    kitchen() 
    print("After kitchen update", chai_type)  


update_order()    
