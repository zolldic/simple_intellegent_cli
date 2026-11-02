#!/usr/bin/python3


from pydantic import BaseModel


class Invoice(BaseModel):
    invoice_number: str
    total_amount: int
    currency: str
    due_date: str
