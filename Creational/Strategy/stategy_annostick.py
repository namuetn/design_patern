def get_price(original_price, type_promotion='default'):
    if type_promotion == 'pre_order':
        return original_price * 0.2
    
    # phá vỡ nguyễn tắc solid đầu tiên đó là nguyên tắc trách nghiệm duy nhất
    if type_promotion == 'promotion':
        return original_price * 0.3
    
    if type_promotion == 'back_friday':
        return original_price * 0.9
    
    if type_promotion == 'default':
        return original_price

    # nếu có 1 ctr khuyến mãi khác thì phải thêm if vào đây làm code rất rối
    # nếu 1 if lỗi là lỗi cả function

print(get_price(200, 'pre_order'))
print(get_price(200))