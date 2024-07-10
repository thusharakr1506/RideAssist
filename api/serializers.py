from rest_framework import serializers

from api.models import Customer,Work


class WorkSerializer(serializers.ModelSerializer):

    customer_object=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Work

        fields="__all__"

        read_only_fields=["id","customer_object", "created_date", "updated_date", "is_active"]



class CustomerSerializer(serializers.ModelSerializer):
    
    works=WorkSerializer(many=True,read_only=True)

    work_total=serializers.CharField(read_only=True)

    class Meta:

        model=Customer
        fields="__all__"
        read_only_fields=["id","created_date","updated_date","is_active"]
        