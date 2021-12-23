from django.shortcuts import render
from city_distr.models import Rubric, Article

# Create your views here.
def show_genres(request):
    rubric = Rubric.objects.filter()
    rubric_test = Rubric.objects.filter(level=0).values('name', 'level', 'tree_id')
    rubric_test_2 = Rubric.objects.filter(level=1).values('name', 'level', 'tree_id')
    print('rubric')
    print(rubric)
    print(rubric_test)
    for rubric_test_s in rubric_test:
        print('1')
        print(rubric_test_s['name'])
        # print(rubric_test_s['level'])

    for rubric_test_s in rubric_test_2:
        print('2')
        print(rubric_test_s['name'])
        # print(rubric_test_s['level'])





    return render(request, "genres.html", {'rubrics': rubric})