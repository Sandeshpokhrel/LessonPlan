from django.contrib import admin
from . import models
from django.urls import reverse
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.db.models import F

# Register your models here.

admin.site.site_header = 'Lesson Plan Management'
admin.site.index_title = 'Admin'

#user
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject_count']
    search_fields = ['email']

    def subject_count(self, user):
        url = reverse('admin:core_subject_changelist') + '?' + urlencode({'user__id': str(user.id)})
        return format_html('<a href ="{}">{}</a>', url, user.subject_count)
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            subject_count = Count('subject')
        )


#subject
@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['sub_name', 'section_year_count']
    search_fields = ['sub_name']
    autocomplete_fields = ['user']

    def section_year_count(self, subject):
        url = reverse('admin:core_sectionyear_changelist') + '?' + urlencode({'subject__id': str(subject.id)})
        return format_html('<a href ="{}">{}</a>', url, subject.section_year_count)
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            section_year_count = Count('sectionyear')
        )
    

#section and year
@admin.register(models.SectionYear)
class SectionYearAdmin(admin.ModelAdmin):
    list_display = ['section', 'year', 'plan_count', 'chapter_count']
    search_fields = ['section']
    autocomplete_fields = ['subject']
    
    def plan_count(self, section_year):
        url = reverse('admin:core_plan_changelist') + '?' + urlencode({'section_year__id': str(section_year.id)})
        return format_html('<a href ="{}">{}</a>', url, section_year.plan_count)
    def chapter_count(self, section_year):
        url = reverse('admin:core_chapter_changelist') + '?' + urlencode({'section_year__id': str(section_year.id)})
        return format_html('<a href ="{}">{}</a>', url, section_year.chapter_count)
    def user_name(self, section_year):
        return section_year.user
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            plan_count = Count('plan'),
            chapter_count = Count('chapter')
        )
    

#plan
@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan_name', 'activity_count']
    search_fields = ['plan_name']
    autocomplete_fields = ['sectionyear', 'chapter']
    
    def activity_count(self, plan):
        url = reverse('admin:core_activity_changelist') + '?' + urlencode({'plan__id': str(plan.id)})
        return format_html('<a href ="{}">{}</a>', url, plan.activity_count)
    def test_count(self, plan):
        url = reverse('admin:core_test_changelist') + '?' + urlencode({'plan__id': str(plan.id)})
        return format_html('<a href ="{}">{}</a>', url, plan.test_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            activity_count = Count('activity'),
            test_count = Count('test')
        )


#activity
@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activity_detail']
    search_fields = ['activity_detail']
    autocomplete_fields = ['plan']


#test
@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['test_detail']
    search_fields = ['test_detail']
    autocomplete_fields = ['plan']


#chapter
@admin.register(models.Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['chapter_name', 'assignment_count', 'resource_count']
    search_fields = ['chapter_name']
    autocomplete_fields = ['section_year']
    
    def assignment_count(self, chapter):
        url = reverse('admin:core_assignment_changelist') + '?' + urlencode({'chapter__id': str(chapter.id)})
        return format_html('<a href ="{}">{}</a>', url, chapter.assignment_count)
    def resource_count(self, chapter):
        url = reverse('admin:core_resource_changelist') + '?' + urlencode({'chapter__id': str(chapter.id)})
        return format_html('<a href ="{}">{}</a>', url, chapter.resource_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            assignment_count = Count('assignment'),
            resource_count = Count('resource')
        )
    

#assignment
@admin.register(models.Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['assign_name', 'updated_date']
    search_fields = ['assign_name']
    autocomplete_fields = ['chapter']


#resource
@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['res_name', 'updated_date']
    search_fields = ['res_name']
    autocomplete_fields = ['chapter']

