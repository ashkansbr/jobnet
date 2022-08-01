from rest_framework import serializers
from ..models import JobCategory, JobRequest, Skill, Job


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title']


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'name']


class ReadJobSerializer(serializers.ModelSerializer):

    def get_company(self, obj):
        return {
            'id': obj.company.id,
            'name': obj.company.name
        }

    def get_city(self, obj):
        return {
            'id': obj.city.id,
            'name': obj.city.name
        }

    company = serializers.SerializerMethodField('get_company')
    city = serializers.SerializerMethodField('get_city')
    category = serializers.CharField(source='category.name')
    cooperation_type = serializers.CharField(source='get_cooperation_type_display')
    work_experience = serializers.CharField(source='get_work_experience_display')
    sex = serializers.CharField(source='get_sex_display')
    degree = serializers.CharField(source='get_degree_display')
    required_skill = serializers.StringRelatedField(many=True)
    military_status = serializers.CharField(source='get_military_status_display')

    class Meta:
        model = Job
        exclude = ['employer']


class WriteJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['employer', 'company', 'created_at', 'updated_at']
        