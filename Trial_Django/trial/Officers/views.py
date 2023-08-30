from django.shortcuts import render
from .models import CommitteeOfficer
from django.http import JsonResponse

# Create your views here.
def hello(request):
    return render(request, 'index.html')

def all_officers(request):
    if request.method == 'GET':
        officers = CommitteeOfficer.objects.all()
        return_json = [officer.serialize() for officer in officers]
        return JsonResponse(return_json, safe=False)
    elif request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        hobby = request.POST.get('hobby')
        try:
            obj = CommitteeOfficer.create(
                name=name,
                year=year,
                hobby=hobby
            )
            obj.full_clean()
            obj.save()
            return JsonResponse(obj.serialize(), status=201, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def one_officer(request, officer_id):
    if request.method == 'GET':
        try:
            obj = CommitteeOfficer.objects.get(id=officer_id)
            return JsonResponse(obj.serialize(), safe=False)
        except CommitteeOfficer.DoesNotExist:
            return JsonResponse({'error': 'Officer not found'}, status=404)
    elif request.method == 'DELETE':
        try:
            obj = CommitteeOfficer.objects.get(id=officer_id)
            obj.delete()
            return JsonResponse(obj.serialize(), status=204, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)