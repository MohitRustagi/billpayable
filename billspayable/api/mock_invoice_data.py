import datetime
from decimal import Decimal
dummy_data =\
[
    [
        {
            "seller": "seller1",
            "invoice_no": "#123",
            "due_date": datetime.datetime.now().date(),
            "description": "test description..",
            "price": Decimal(1213.22),
            "qty": 2,
            "amount": Decimal(2423.44),
            "buyer": "buyer1",
            "tax_perc": Decimal(8)      
        },
        {
            "seller": "seller1",
            "invoice_no": "#123",
            "due_date": datetime.datetime.now().date(),
            "description": "test description..",
            "price": Decimal(2323),
            "qty": 1,
            "amount": Decimal(2323),
            "buyer": "buyer1",
            "tax_perc": Decimal(8)
        },
        {
            "seller": "seller1",
            "invoice_no": "#123",
            "due_date": datetime.datetime.now().date(),
            "description": "test description..",
            "price": Decimal(10000),
            "qty": 1,
            "amount": Decimal(12000),
            "buyer": "buyer1",
            "tax_perc": Decimal(8)        
        },
    ],
    [{
        "seller": "britannia",
        "invoice_no": "#2321",
        "due_date": datetime.datetime.now().date(),
        "description": "test description..",
        "price": Decimal(23412),
        "qty": Decimal(23),
        "amount": Decimal(333333),
        "buyer": "Dominos",
        "tax_perc": Decimal(22)        
    }],
    [{
        "seller": "Tata",
        "invoice_no": "#14123",
        "due_date": datetime.datetime.now().date(),
        "description": "test description..",
        "price": Decimal(1231.22),
        "qty": 2,
        "amount": Decimal(2432.44),
        "buyer": "xyz",
        "tax_perc": Decimal(8)
    }],
    [{
        "seller": "PolicyBazaar",
        "invoice_no": "#553",
        "due_date": datetime.datetime.now().date(),
        "description": "insurance policies for employees",
        "price": Decimal(15000),
        "qty": Decimal(20),
        "amount": Decimal(122389123),
        "buyer": "PlateIQ",
        "tax_perc": Decimal(8)        
    }]
]
