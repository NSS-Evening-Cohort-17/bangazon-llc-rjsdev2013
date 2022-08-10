"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all


class ProductListOver1000(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            db_cursor.execute("""
                SELECT 
                    p.name as "product",
                    s.name as "store"
                FROM bangazon_api_product p
                JOIN bangazon_api_store s
                ON p.store_id = s.id
                WHERE p.price >= 1000
            """)
            
            dataset = dict_fetch_all(db_cursor)
        
        template = 'products/list_over_1000.html'
        
        context = {
            "product_list": dataset
        }

        return render(request, template, context)