import re
from rest_framework import serializers
from api.models import EquipmentType, Equipment


class EquipmentTypeSerializer(serializers.ModelSerializer):
    """ Equipment type serializer """
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    """ Equipment serializer """
    def validate(self, validated_data):
        equipment_type = validated_data.get('type')
        if not equipment_type:
            raise serializers.ValidationError('Тип оборудования не найден')
        regx = {
            'N': '[0-9]',
            'A': '[A-Z]',
            'a': '[a-z]',
            'X': '[A-Z0-9]',
            'Z': '[-|_|@]',
        }
        mask = r''.join([regx[letter] for letter in equipment_type.mask])
        if not bool(re.fullmatch(mask, validated_data.get('serial_number'))):
            raise serializers.ValidationError(
                f'Серийный номер "{validated_data.get("serial_number")}" не соответствует маске "{equipment_type.mask}"')
        return validated_data

    class Meta:
        model = Equipment
        fields = '__all__'
