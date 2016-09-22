from rest_framework import viewsets
from rest_framework.response import Response
from .models import NewCartItem, NewCart
from .serializers import NewCartSerializer



class NewCartViewSet(viewsets.ViewSet):
    """
    POST:
    Payload:
    {
      "created_date": "2016-09-16T14:32:09.638195",
      "items": [
        {
            "product": 4,
            "quantity": 11,
            "data": {}
        },
        {
            "product": 4,
            "quantity": 15,
            "data": {}
        },
        {
            "product": 5,
            "quantity": 1,
            "data": {}
        }
        ]
    }
    """
    def list(self, request):
        cart = NewCart()
        serializer = NewCartSerializer(cart, many=False)
        return Response(serializer.data)

    def create(self, request):
        # import ipdb; ipdb.set_trace()
        cart = NewCart(created_date=request.data.get('created_date'))
        items = request.data.get('items')

        if items:
            for item in items:
                try:
                    cart_item = cart.add_item(item.get('product'), item.get('quantity', 0), item.get('data', {}))
                except Exception as e:
                    raise
                    pass


        serializer = NewCartSerializer(cart, many=False)
        response = serializer.data
        # response['request'] = request.data
        # response['orig_items'] = items
        return Response(response)