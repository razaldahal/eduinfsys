from rest_framework import serializers
from eis.models import student,grade,teacher


class studentSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = student
        fields = ('select_gender','full_name','address','grade','section','roll_no')

class gradeSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = grade
        fields = ('select_grade','select_section')

class teacherSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = teacher
        fields = ('full_name','address','phone_no','qualifications')
