from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, TransactionSerializer
from .models import Category, Transaction

class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            serializer = CategorySerializer(category)
            return Response({"data": serializer.data})
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({"data": serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=201)
        return Response({"data": serializer.errors}, status=400)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"data": serializer.errors}, status=400)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response({"message": "Category deleted successfully"}, status=204)


class TransactionView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        if pk:
            transaction = get_object_or_404(Transaction, pk=pk)
            serializer = TransactionSerializer(transaction)
            return Response({"data": serializer.data})
        else:
            transactions = Transaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            return Response({"data": serializer.data})

    def post(self, request):
        serializer = TransactionSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=201)
        return Response({"data": serializer.errors}, status=400)

    def put(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"data": serializer.errors}, status=400)

    def delete(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        return Response({"message": "Transaction deleted successfully"}, status=204)
