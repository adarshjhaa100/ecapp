from django.contrib import admin
from . models import pollingStation,facility,Candidate,pwd,ThirdGender,Suggestion,result,pickupPoint
from django.utils.safestring import mark_safe
import csv
from django.http import HttpResponse


class pollingStationAdmin(admin.ModelAdmin):
	def image_tag(self, obj):
		return mark_safe('<img src="{}" ,height = 300 , width = 400 /> '.format(obj.picture.url))

	image_tag.short_description = 'Image'
	readonly_fields = ['image_tag',]
	list_display=['pid','no','name']
	search_fields=['pid']
	actions=['export_as_csv']
admin.site.register(pollingStation,pollingStationAdmin)
admin.site.register(facility)

class pickupPointAdmin(admin.ModelAdmin):
	list_display=['name','address']
admin.site.register(pickupPoint,pickupPointAdmin)


class CandidateAdmin(admin.ModelAdmin):
	def tag_photo(self, obj):
		return mark_safe('<img src="{}" ,height = 180 , width = 140 /> '.format(obj.photo.url))
	def tag_party(self, obj):
		return mark_safe('<img src="{}" ,height = 60 , width = 60 /> '.format(obj.symbol.url))   
	
	tag_photo.short_description = 'Photo of Candidate'
	tag_party.short_description='Symbol of Party'
	readonly_fields = ['tag_photo','tag_party'] 
	list_display=['name','party']
	search_fields=['party']
admin.site.register(Candidate,CandidateAdmin)


admin.site.register(pwd)
admin.site.register(ThirdGender)


class SuggestionAdmin(admin.ModelAdmin):
	def has_add_permission(self,request):
		return False
	def has_delete_permission(self,request,obj=None):
		return False
	readonly_fields=['text','rating']
	list_display=['text','rating']
admin.site.register(Suggestion,SuggestionAdmin)