def save_cars(manufacturer, model, **specs):
    """Build a dictonary containing all the specs about each car."""
    print(f"\nStoring details about a {manufacturer.title()} {model.title()} with the following specs:")
    print(f"{specs}")
     
save_cars('lamboghini', 'temerario', body='two-door', engine='electric', frame='aluminum') 
save_cars('chevrolet', 'corvette', body='two-door', fuel_type='gasoline', engine='v8')
save_cars('ford', 'mustang', drive_train='rear wheel drive')