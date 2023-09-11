from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MetaData, SKUData


class LocationAPIView(APIView):

    def get(self, request):

        locations = MetaData.objects.all().select_related('location').values(
            'location_id', 'location__name'
        ).distinct()

        locations = [
            {'id': l.get('location_id'), 'name': l.get('location__name')}
            for l in locations
        ]
        return Response(
            {
                "status": True,
                "message": "Location fetched successfully",
                "data": sorted(locations, key=lambda x: x.get('id')),
                "error": None
            }
        )


class DepartmentAPIView(APIView):

    def get(self, request, location_id):
        departments = MetaData.objects.filter(
            location_id=location_id
        ).select_related('department').values(
            'department_id', 'department__name'
        ).distinct()
        departments = [
            {'id': d.get('department_id'), 'name': d.get('department__name')}
            for d in departments
        ]
        return Response(
            {
                "status": True,
                "message": "Department fetched successfully",
                "data": sorted(departments, key=lambda x: x.get("id")),
                "error": None
            }
        )


class CategoryAPIView(APIView):

    def get(self, request, location_id, department_id):
        categories = MetaData.objects.filter(
            location_id=location_id, department_id=department_id
        ).select_related('category').values(
            'category_id', 'category__name'
        ).distinct()
        categories = [
            {'id': d.get('category_id'), 'name': d.get('category__name')}
            for d in categories
        ]
        return Response(
            {
                "status": True,
                "message": "Category fetched successfully",
                "data": sorted(categories, key=lambda x: x.get("id")),
                "error": None
            }
        )


class SubCategoryAPIView(APIView):

    def get(self, request, location_id, department_id, category_id, subcategory_id=None):
        sub_categories = MetaData.objects.filter(
            location_id=location_id, department_id=department_id, category_id=category_id
        )
        if subcategory_id:
            sub_categories = sub_categories.filter(sub_category_id=subcategory_id)

        sub_categories = sub_categories.select_related('sub_category').values(
            'sub_category_id', 'sub_category__name'
        ).distinct()
        sub_categories = [
            {'id': d.get('sub_category_id'), 'name': d.get('sub_category__name')}
            for d in sub_categories
        ]
        return Response(
            {
                "status": True,
                "message": "SubCategory fetched successfully",
                "data": sorted(sub_categories, key=lambda x: x.get("id")),
                "error": None
            }
        )


class SKUDataAPIView(APIView):

    def get(self, request):
        sku_data = SKUData.objects.filter().select_related(
            'location', 'department', 'category', 'sub_category'
        )
        if request.GET.get('location'):
            sku_data = sku_data.filter(location__name=request.GET.get('location'))

        if request.GET.get('department'):
            sku_data = sku_data.filter(department__name=request.GET.get('department'))

        if request.GET.get('category'):
            sku_data = sku_data.filter(category__name=request.GET.get('category'))

        if request.GET.get('sub_category'):
            sku_data = sku_data.filter(sub_category__name=request.GET.get('sub_category'))

        sku_data = [
            {
                'sku': d.sku,
                'name': d.name,
                'location': d.location.name,
                'department': d.department.name,
                'category': d.category.name,
                'sub_category': d.sub_category.name
            }
            for d in sku_data
        ]

        return Response(
            {
                "status": True,
                "message": "SKU data fetched successfully",
                "data": sku_data,
                "error": None
            }
        )